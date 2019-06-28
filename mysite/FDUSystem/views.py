from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect, Http404, HttpResponse
from FDUSystem import models
from FDUSystem.models import Student, Teacher, Classroom, Course, PreCourse, School, Major, SelectCourse
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def index(request):
    # return HttpResponse("Hello, world!")
    return render(request, './index.html')


def signin(request):
    print("into sign")
    if request.method == 'POST':
        print("get here")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = my_authenticate(username, password)
        if user is not None and user.is_active:
            print("is ok")
            auth.login(request, user)
            request.session['is_login'] = '1'
            print("now come to home")
            return HttpResponseRedirect('home.html', {'msg': 'login success!'})
        else:
            print("sign in failed")
            return render(request, 'signin.html', locals())
    print("log in failed here")
    return render(request, 'signin.html', locals())


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        usertype = request.POST.get('usertype')
        IDNumber = request.POST.get('IDNumber')
        username_check = User.objects.filter(username=username)
        email_check = User.objects.filter(email=email)
        print(usertype)
        # general check
        if len(username_check) > 0:
            return HttpResponseRedirect('./signup.html', {'msg': 'User exists!'})
        if len(email_check) > 0:
            print('email already exists!')
            return HttpResponseRedirect('./signup.html', {'msg': 'email exists!'})
        if password != password2:
            print('psd not same')
            return HttpResponseRedirect('./signup.html', {'msg': 'Recheck your password!'})

        # register different type
        if usertype == "admin":
            admin_check = models.UserExtension.objects.filter(user_number=IDNumber)
            if len(admin_check) > 0:
                print('admin already exists!')
                return HttpResponseRedirect('./signup.html', {'msg': 'admin already exists!'})
            user = User.objects.create_superuser(username=username, email=email, password=password)
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            user_extension = models.UserExtension(user=user)
            user_extension.user_number = IDNumber
            user_extension.user_belong = 'admin'
            user_extension.save()
            return HttpResponseRedirect('./signin.html', {'msg': 'register success!'})
        elif usertype == "student":
            stuNumber_check = models.Student.objects.filter(stu_id=IDNumber)
            if len(stuNumber_check) == 0:
                print("stu not exists!")
                return HttpResponseRedirect('signup.html', {'msg': 'student not exists!'})
            user = User.objects.create_user(username=username, email=email, password=password)
            group = Group.objects.get(name='student')
            user.groups.add(group)
            user_extension = models.UserExtension(user=user)
            user_extension.user_number = IDNumber
            user_extension.user_belong = 'student'
            user_extension.save()
            return HttpResponseRedirect('./signin.html', locals())
        elif usertype == "teacher":
            teacherNumber_check = models.Teacher.objects.filter(teacher_id=IDNumber)
            if len(teacherNumber_check) == 0:
                print("teacher exists!")
                return HttpResponseRedirect('signup.html', {'msg': 'teacher not exists!'})
            user = User.objects.create_user(username=username, email=email, password=password)
            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            user_extension = models.UserExtension(user=user)
            user_extension.user_number = IDNumber
            user_extension.user_belong = 'teacher'
            user_extension.save()
            return HttpResponseRedirect('./signin.html', locals())
        else:
            return HttpResponse("here means you are failed")
    print("you are here")
    return render(request, './signup.html', locals())



@login_required
def home(request):
    schools = School.objects.all()
    majors = Major.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    courses = Course.objects.all()
    classrooms = Classroom.objects.all()
    precourses = []
    prec = PreCourse.objects.all()
    for i in prec:
        pre = Course.objects.get(course_id=i.pre_course_id_id)
        cur = Course.objects.get(course_id=i.cur_course_id_id)
        precourses.append((i, pre, cur))
    user_belong = request.user.extension.user_belong
    mycourses = []
    myteachcourses = []
    scorelist = []
    if user_belong == 'admin':
        selectcourse = SelectCourse.objects.all()
        for i in selectcourse:
            course = Course.objects.get(course_id=i.sc_course_id_id)
            student_name = Student.objects.get(stu_id=i.sc_stu_id_id)
            teacher_name = Teacher.objects.get(teacher_id=course.course_teacher_id_id)
            scorelist.append((i.sc_course_id_id, course.course_name, course.course_teacher_id_id, teacher_name,
                              i.sc_stu_id_id, student_name, i.sc_score))
        # for j in scorelist:
        #     print(j[0])
    elif user_belong == 'student':
        print(request.user.extension.user_number)
        selectedcourses = SelectCourse.objects.filter(sc_stu_id_id=request.user.extension.user_number)
        for i in selectedcourses:
            course = Course.objects.get(course_id=i.sc_course_id_id)
            teacher = Teacher.objects.get(teacher_id=course.course_teacher_id_id)
            mycourses.append((i, course, teacher))
    elif user_belong == 'teacher':
        print(request.user.extension.user_number)
        myteach = Course.objects.filter(course_teacher_id=request.user.extension.user_number)
        for i in myteach:
            sc = SelectCourse.objects.filter(sc_course_id=i.course_id)
            for j in sc:
                student = Student.objects.get(stu_id=j.sc_stu_id_id)
                myteachcourses.append((i.course_id, i.course_name, j.sc_stu_id_id, student.stu_name, j.sc_score))
    return render(request, './home.html', locals())


@login_required
def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('./index.html')


def resetpsd(request):
    return render(request, './resetpsd.html')


def my_authenticate(username, password):
    user = User.objects.filter(username=username).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            print('password error！')
            return None
    else:
        print('user not exist!')
        return None


def deleteSelected(request):
    if request.method == 'POST':
        if request.path == '/deleteSelected/schools':
            print('get in here')
            lst = request.POST.getlist('select_one_school')
            print(lst)
            for i in lst:
                School.objects.filter(school_id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/majors':
            print('get in delete majors')
            lst = request.POST.getlist('select_one_major')
            print(lst)
            for i in lst:
                Major.objects.filter(major_id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/teachers':
            print('get in delete teachers')
            lst = request.POST.getlist('select_one_teacher')
            print(lst)
            for i in lst:
                Teacher.objects.filter(teacher_id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/students':
            print('get in delete students')
            lst = request.POST.getlist('select_one_student')
            print(lst)
            for i in lst:
                Student.objects.filter(stu_id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/courses':
            print('get in delete courses')
            lst = request.POST.getlist('select_one_course')
            print(lst)
            for i in lst:
                Course.objects.filter(course_id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/classrooms':
            print('get in delete classroom')
            lst = request.POST.getlist('select_one_classroom')
            print(lst)
            for i in lst:
                Classroom.objects.filter(classroom_id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/precourses':
            print('get in delete precourse')
            lst = request.POST.getlist('select_one_precourse')
            print(lst)
            for i in lst:
                PreCourse.objects.filter(id=i).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        elif request.path == '/deleteSelected/scorelists':
            print('get in delete scorelist')
            lst = request.POST.getlist('select_one_scorelist')
            print(lst)
            for i in lst:
                a = i.split(',')
                SelectCourse.objects.filter(sc_course_id=a[0], sc_stu_id=a[1]).delete()
            print('delete done')
            return HttpResponseRedirect('../home.html', locals())
        else:
            print('not success')
    return render(request, 'home.html')


def search(request):
    print("in search")
    if request.method == 'POST':
        print('in search post')
        if request.path == '/search/schools':
            print('in search school')
            id = request.POST.get('searchSchoolByID')
            name = request.POST.get('searchSchoolByName')
            schools = School.objects.filter(Q(school_id__icontains=id) & Q(school_name__icontains=name))
            return render(request, 'search.html', locals())
        elif request.path == '/search/majors':
            print('in search major')
            id = request.POST.get('searchMajorByID')
            name = request.POST.get('searchMajorByName')
            school_id = request.POST.get('searchMajorBySchoolID')
            majors = Major.objects.filter(Q(major_id__icontains=id) & Q(major_name__icontains=name) & Q(
                major_school__school_id__icontains=school_id))
            return render(request, 'search.html', locals())
        elif request.path == '/search/teachers':
            print('in search teacher')
            name = request.POST.get('searchTeacherByName')
            sex = request.POST.get('searchTeacherBySex')
            age = request.POST.get('searchTeacherByAge')
            title = request.POST.get('searchTeacherByTitle')
            if age:
                age = int(age)
            else:
                age = 0
            if not sex:
                sex = None
            print(name)
            print(age)
            print(sex)
            print(title)
            school_id = request.POST.get('searchTeacherBySchoolID')
            teachers = Teacher.objects.filter(Q(teacher_age__gte=age) & Q(teacher_name__icontains=name)
                                              & Q(teacher_title=title) & Q(teacher_sex=sex) &
                                              Q(teacher_school__school_id__contains=school_id))
            for i in teachers:
                print(i)
            return render(request, 'search.html', locals())
        elif request.path == '/search/students':
            print('in search student')
            name = request.POST.get('searchStudentByName')
            sex = request.POST.get('searchStudentBySex')
            age = request.POST.get('searchStudentByAge')
            s_m_name = request.POST.get('searchStudentByMajorName')
            if age:
                age = int(age)
            else:
                age = 0
            students = Student.objects.filter(Q(stu_name__icontains=name) & Q(stu_sex=sex)
                                              & Q(stu_age__gte=age)
                                              & Q(stu_major__major_name__icontains=s_m_name))
            for i in students:
                print(i)
            return render(request, 'search.html', locals())
        elif request.path == '/search/courses':
            print('in search course')
            name = request.POST.get('searchByCourseName')
            c_id = request.POST.get('searchByCourseID')
            cap = request.POST.get('searchByCapacity')
            classroom_id = request.POST.get('searchByClassroomID')
            t_id = request.POST.get('searchByTeacherID')
            print(classroom_id)
            print(t_id)
            courses = Course.objects.filter(Q(course_id__icontains=c_id) & Q(course_name__icontains=name)
                                            & Q(course_capacity__gte=cap)
                                            & Q(course_classroom_id__classroom_id__icontains=classroom_id)
                                            & Q(course_teacher_id__teacher_id__icontains=t_id))
            for i in courses:
                print(i)
            if not courses:
                print('null')
            return render(request, 'search.html', locals())
        elif request.path == '/search/classrooms':
            print('in search classroom')
            id = request.POST.get('searchClassroomByID')
            cap = request.POST.get('searchClassroomByCapacity')
            classrooms = Classroom.objects.filter(Q(classroom_id__icontains=id)
                                                  & Q(classroom_capacity__gte=cap))
            for i in classrooms:
                print(i)
            if not classrooms:
                print('null')
            return render(request, 'search.html', locals())
        elif request.path == '/search/precourses':
            print('in search precourses')
            id = request.POST.get('searchByID')
            cur_name = request.POST.get('searchByCurName')
            pre_name = request.POST.get('searchByPreName')
            if id:
                id = int(id)
            else:
                id = 0
            prec = PreCourse.objects.filter(Q(id__gte=id)
                                            & Q(pre_course_id__course_name__icontains=cur_name)
                                            & Q(pre_course_id__course_name__icontains=pre_name))
            for i in prec:
                print(i)
            if not prec:
                print('null')
            precourses = []
            for i in prec:
                pre = Course.objects.get(course_id=i.pre_course_id_id)
                cur = Course.objects.get(course_id=i.cur_course_id_id)
                precourses.append((i, pre, cur))
            return render(request, 'search.html', locals())
        elif request.path == '/search/myteachcourses':
            print('in search my teach course')
            c_id = request.POST.get('searchMyteachcourseByCID')
            c_name = request.POST.get('searchMyteachcourseByCName')
            s_id = request.POST.get('searchMyteachcourseBySID')
            s_name = request.POST.get('searchMyteachcourseBySName')
            score = request.POST.get('searchByStuScore')
            t_id = request.user.extension.user_number
            selectcourse = SelectCourse.objects.filter(Q(sc_course_id__course_teacher_id__exact=t_id)
                                                       & Q(sc_course_id__course_id__icontains=c_id)
                                                       & Q(sc_course_id__course_name__icontains=c_name)
                                                       & Q(sc_stu_id__stu_id__icontains=s_id)
                                                       & Q(sc_stu_id__stu_name__icontains=s_name)
                                                       & Q(sc_score__gte=score))
            myteachcourses = []
            for i in selectcourse:
                student = Student.objects.get(stu_id=i.sc_stu_id_id)
                course = Course.objects.get(course_id=i.sc_course_id_id)
                myteachcourses.append(
                    (course.course_id, course.course_name, i.sc_stu_id_id, student.stu_name, i.sc_score))
            return render(request, 'search.html', locals())
        elif request.path == '/search/mycourses':
            print('in search mycourse')
            c_id = request.POST.get('searchByCourseID')
            c_name = request.POST.get('searchByCourseName')
            t_name = request.POST.get('searchByTeacherName')
            score = request.POST.get('searchByScore')
            s_id = request.user.extension.user_number
            selectcourse = SelectCourse.objects.filter(Q(sc_stu_id=s_id)
                                                       & Q(sc_course_id__course_id__icontains=c_id)
                                                       & Q(sc_course_id__course_name__icontains=c_name) & Q(
                sc_course_id__course_teacher_id__teacher_name__icontains=t_name)
                                                       & Q(sc_score__gte=score))
            mycourses = []
            for i in selectcourse:
                course = Course.objects.get(course_id=i.sc_course_id_id)
                teacher = Teacher.objects.get(teacher_id=course.course_teacher_id_id)
                mycourses.append((i, course, teacher))
            return render(request, 'search.html', locals())
        elif request.path == '/search/scorelists':
            print('in search scorelists')
            c_id = request.POST.get('searchScorelistByCourseID')
            c_name = request.POST.get('searchScorelistByCourseName')
            t_id = request.POST.get('searchScorelistByTeacherID')
            t_name = request.POST.get('searchScorelistByTeacherName')
            s_id = request.POST.get('searchScorelistByStudentID')
            s_name = request.POST.get('searchScorelistByStudentName')
            score = request.POST.get('searchScorelistByScore')
            print(score)
            selectcourse = SelectCourse.objects.filter(Q(sc_course_id__course_id__icontains=c_id)
                                                       & Q(sc_course_id__course_name__icontains=c_name)
                                                       & Q(sc_stu_id__stu_id__icontains=s_id)
                                                       & Q(sc_stu_id__stu_name__icontains=s_name)
                                                       & Q(sc_course_id__course_teacher_id__teacher_id__icontains=t_id)
                                                       & Q(
                sc_course_id__course_teacher_id__teacher_name__icontains=t_name)
                                                       & Q(sc_score__gte=score))
            scorelist = []
            for i in selectcourse:
                course = Course.objects.get(course_id=i.sc_course_id_id)
                student_name = Student.objects.get(stu_id=i.sc_stu_id_id)
                teacher_name = Teacher.objects.get(teacher_id=course.course_teacher_id_id)
                scorelist.append((i.sc_course_id_id, course.course_name, course.course_teacher_id_id, teacher_name,
                                  i.sc_stu_id_id, student_name, i.sc_score))
            return render(request, 'search.html', locals())
    else:
        return HttpResponseRedirect('../home.html')


def addpage(request):
    print("in add")
    if request.method == 'POST':
        print("in here")
        if request.path == '/add/schools':
            id = request.POST.get('inputSchoolID')
            name = request.POST.get('inputSchoolName')
            check_name = School.objects.filter(school_id=id)
            if len(check_name) > 0:
                render(request, 'add.html')
            else:
                School.objects.create(school_id=id, school_name=name)
                print('create success!')
                return HttpResponseRedirect('/add/schools', locals())
        elif request.path == '/add/majors':
            id = request.POST.get('inputMajorID')
            name = request.POST.get('inputMajorName')
            school_id = request.POST.get('inputSchoolID')
            check_name = Major.objects.filter(major_id=id)
            check_school = School.objects.filter(school_id=school_id)
            if check_name or not check_school:
                render(request, 'add.html')
            else:
                Major.objects.create(major_id=id, major_name=name, major_school_id=school_id)
                print('create success!')
                return HttpResponseRedirect('/add/majors', locals())
        elif request.path == '/add/teachers':
            id = request.POST.get('inputTeacherID')
            name = request.POST.get('inputTeacherName')
            sex = request.POST.get('inputTeacherSex')
            age = request.POST.get('inputTeacherAge')
            title = request.POST.get('inputTeacherTitle')
            salary = request.POST.get('inputTeacherSalary')
            school_id = request.POST.get('inputTeacherSchoolID')
            check_name = Teacher.objects.filter(teacher_id=id)
            check_school = School.objects.filter(school_id=school_id)
            if check_name or not check_school:
                render(request, 'add.html')
            else:
                Teacher.objects.create(teacher_id=id, teacher_name=name, teacher_sex=sex, teacher_age=age,
                                       teacher_title=title, teacher_salary=salary, teacher_school_id=school_id)
                print('create success!')
                return HttpResponseRedirect('/add/teachers', locals())
        elif request.path == '/add/students':
            id = request.POST.get('inputStudentID')
            name = request.POST.get('inputStudentName')
            sex = request.POST.get('inputStudentSex')
            age = request.POST.get('inputStudentAge')
            major_id = request.POST.get('inputStudentMajorID')
            check_name = Student.objects.filter(stu_id=id)
            check_major = Major.objects.filter(major_id=major_id)
            if check_name or not check_major:
                render(request, 'add.html')
            else:
                Student.objects.create(stu_id=id, stu_name=name, stu_age=age, stu_sex=sex,
                                       stu_major_id=major_id)
                print('add student success!')
                return HttpResponseRedirect('/add/students', locals())
        elif request.path == '/add/courses':
            print("in add courses")
            id = request.POST.get('inputCourseID')
            name = request.POST.get('inputCourseName')
            c_room = request.POST.get('inputCourseClassroomID')
            cap = request.POST.get('inputCourseCapacity')
            t_id = request.POST.get('inputCourseTeacherID')
            check_name = Course.objects.filter(course_id=id)
            check_teacher = Teacher.objects.filter(teacher_id=t_id)
            check_classroom = Classroom.objects.filter(classroom_id=c_room)
            if check_name:
                print("name exists!")
            if not check_teacher:
                print('teacher not exists !')
            if not check_classroom:
                print('class room not exists!')
            if check_name or not check_teacher or not check_classroom:
                render(request, 'add.html')
            else:
                Course.objects.create(course_id=id, course_name=name, course_classroom_id_id=c_room,
                                      course_capacity=cap, course_teacher_id_id=t_id)
                print('add course success!')
                return HttpResponseRedirect('/add/courses', locals())
        elif request.path == '/add/classrooms':
            print("in add classroom")
            id = request.POST.get('inputClassroomID')
            cap = request.POST.get('inputClassroomCapacity')
            check_name = Classroom.objects.filter(classroom_id=id)
            if check_name:
                print("name exists!")
            if check_name:
                render(request, 'add.html')
            else:
                Classroom.objects.create(classroom_id=id, classroom_capacity=cap)
                print('add classroom success!')
                return HttpResponseRedirect('/add/classrooms', locals())
        elif request.path == '/add/precourses':
            print("in add precourse")
            id = request.POST.get('inputID')
            cur_id = request.POST.get('inputCurID')
            pre_id = request.POST.get('inputPreID')
            check_name = PreCourse.objects.filter(id=id)
            check_cur = Course.objects.filter(course_id=cur_id)
            check_pre = Course.objects.filter(course_id=pre_id)
            if check_name:
                print("name exists!")
            if check_name or not check_cur or not check_pre:
                render(request, 'add.html')
            else:
                PreCourse.objects.create(id=id, pre_course_id_id=pre_id, cur_course_id_id=cur_id)
                print('add precourse success!')
                return HttpResponseRedirect('/add/precourses', locals())
        elif request.path == '/add/mycourses':
            print("in add mycourse")
            c_id = request.POST.get('inputCourseID')
            s_id = request.user.extension.user_number
            check_name = SelectCourse.objects.filter(sc_stu_id=s_id, sc_course_id=c_id)
            if check_name:
                print("name exists!")
                return render(request, 'add.html')
            else:
                SelectCourse.objects.create(sc_course_id_id=c_id, sc_stu_id_id=s_id, sc_score=999)
                print('add select course success!')
                return HttpResponseRedirect('/add/mycourses', locals())
        elif request.path == '/add/scorelists':
            print("in add scorelist")
            id = request.POST.get('inputID')
            c_id = request.POST.get('inputCID')
            s_id = request.POST.get('inputSID')
            score = request.POST.get('inputScore')
            check_name = SelectCourse.objects.filter(id=id)
            if check_name:
                print("name exists!")
            if check_name:
                render(request, 'add.html')
            else:
                SelectCourse.objects.create(id=id, sc_course_id_id=c_id, sc_stu_id_id=s_id, sc_score=score)
                print('add select course success!')
                return HttpResponseRedirect('/add/scorelists', locals())

    else:
        pass
    return render(request, 'add.html', locals())


def edit(request):
    print('get in edit')
    if request.method == 'GET':
        print('get in get')
        id = request.GET.get('id')
        id1 = request.GET.get('id1')
        id2 = request.GET.get('id2')
        if id or id1 or id2:
            print(id)
            if 'edit/schools/' in request.path:
                obj = School.objects.get(school_id=id)
                print(obj.school_name)
                return render(request, './edit.html', locals())
            elif 'edit/majors/' in request.path:
                obj = Major.objects.get(major_id=id)
                print(obj.major_name)
                return render(request, './edit.html', locals())
            elif 'edit/teachers/' in request.path:
                obj = Teacher.objects.get(teacher_id=id)
                print(obj.teacher_name)
                return render(request, './edit.html', locals())
            elif 'edit/students/' in request.path:
                obj = Student.objects.get(stu_id=id)
                print(obj.stu_name)
                return render(request, './edit.html', locals())
            elif 'edit/courses/' in request.path:
                obj = Course.objects.get(course_id=id)
                print(obj.course_id)
                return render(request, './edit.html', locals())
            elif 'edit/classrooms/' in request.path:
                obj = Classroom.objects.get(classroom_id=id)
                print(obj.classroom_id)
                return render(request, './edit.html', locals())
            elif 'edit/precourses/' in request.path:
                obj = PreCourse.objects.get(id=id)
                print(obj.id)
                return render(request, './edit.html', locals())
            elif 'edit/myteachcourses/' in request.path:
                print('in muuuu')
                print(id1)
                print(id2)
                t_id = request.user.extension.user_number
                sc = SelectCourse.objects.get(sc_course_id=id1, sc_stu_id=id2)
                print(t_id)
                print(sc)
                student = Student.objects.get(stu_id=sc.sc_stu_id_id)
                course = Course.objects.get(course_id=sc.sc_course_id_id)
                return render(request, './edit.html', locals())
        else:
            pass
    elif request.method == 'POST':
        if '/edit/schools' in request.path:
            print('get in post')
            s_name = request.POST.get('inputSchoolName')
            s_id = request.POST.get('inputSchoolID')
            print(s_name)
            School.objects.filter(school_id=s_id).update(school_name=s_name)
            print('update over!')
            return HttpResponseRedirect('../../home.html', {'msg', 'update over!'})
        elif 'edit/majors' in request.path:
            print('get in post edit majors')
            m_name = request.POST.get('inputMajorName')
            m_id = request.POST.get('inputMajorID')
            m_s_id = request.POST.get('inputMajorSchoolID')
            Major.objects.filter(major_id=m_id).update(major_name=m_name)
            Major.objects.filter(major_id=m_id).update(major_school_id=m_s_id)
            print('update over')
            return HttpResponseRedirect('../../home.html', {'msg', 'update over!'})
        elif 'edit/students' in request.path:
            print('get in post edit students')
            s_name = request.POST.get('inputStudentName')
            s_sex = request.POST.get('inputStudentSex')
            s_age = request.POST.get('inputStudentAge')
            s_id = request.POST.get('inputStudentID')
            s_m_id = request.POST.get('inputStudentMajorID')
            Student.objects.filter(stu_id=s_id).update(stu_name=s_name, stu_age=s_age,
                                                       stu_sex=s_sex, stu_major_id=s_m_id)
            print('update over')
            return HttpResponseRedirect('../../home.html', {'msg', 'update over!'})
        elif 'edit/courses' in request.path:
            print('get in post edit courses')
            id = request.POST.get('inputCourseID')
            name = request.POST.get('inputCourseName')
            c_id = request.POST.get('inputCourseClassroomID')
            cap = request.POST.get('inputCourseCapacity')
            t_id = request.POST.get('inputCourseTeacherID')
            Course.objects.filter(course_id=id).update(course_name=name, course_capacity=cap,
                                                       course_classroom_id_id=c_id,
                                                       course_teacher_id_id=t_id)
            print('update over')
            return HttpResponseRedirect('../../home.html', {'msg', 'update over!'})
        elif 'edit/precourses' in request.path:
            print('get in post edit precourses')
            id = request.POST.get('inputID')
            cur_id = request.POST.get('inputCurID')
            pre_id = request.POST.get('inputPreID')
            PreCourse.objects.filter(id=id).update(pre_course_id_id=pre_id, cur_course_id_id=cur_id)
            print('update over')
            return HttpResponseRedirect('../../home.html', {'msg', 'update over!'})
        elif 'edit/myteachcourses' in request.path:
            print('get in post edit my teach courses')
            c_id = request.POST.get('inputCID')
            s_id = request.POST.get('inputSID')
            s_score = request.POST.get('inputStuScore')
            SelectCourse.objects.filter(sc_stu_id=s_id, sc_course_id=c_id).update(sc_score=s_score)
            print('update over')
            return HttpResponseRedirect('../../home.html', {'msg', 'update over!'})
    else:
        pass
    print('pass here')
    return render(request, 'edit.html', locals())
