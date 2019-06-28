function showSchool() {
    document.getElementById("School").style.display = "block";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showMajor() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "block";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showTeacher() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "block";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showStudent() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "block";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showCourse() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "block";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showClassroom() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "block";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showPreCourse() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "block";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showMyCourse() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "block";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "none";

}

function showMyTeachCourse() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "block";
    document.getElementById("ScoreList").style.display = "none";

}

function showScoreList() {
    document.getElementById("School").style.display = "none";
    document.getElementById("Major").style.display = "none";
    document.getElementById("Teacher").style.display = "none";
    document.getElementById("Student").style.display = "none";
    document.getElementById("Course").style.display = "none";
    document.getElementById("Classroom").style.display = "none";
    document.getElementById("PreCourse").style.display = "none";
    document.getElementById("MyCourse").style.display = "none";
    document.getElementById("MyTeachCourse").style.display = "none";
    document.getElementById("ScoreList").style.display = "block";

}

function selectAllSchool() {
    const select_all = document.querySelector('#select_all_school')
    const all_select_schools = document.querySelectorAll('.select_one_school')
    if (select_all.checked)
        all_select_schools.forEach(value => value.checked = true)
    else
        all_select_schools.forEach(value => value.checked = false)
}

function selectAllMajor() {
    const select_all = document.querySelector('#select_all_major')
    const all_select_majors = document.querySelectorAll('.select_one_major')
    if (select_all.checked)
        all_select_majors.forEach(value => value.checked = true)
    else
        all_select_majors.forEach(value => value.checked = false)
}

function selectAllTeacher() {
    const select_all = document.querySelector('#select_all_teacher')
    const all_select_teachers = document.querySelectorAll('.select_one_teacher')
    if (select_all.checked)
        all_select_teachers.forEach(value => value.checked = true)
    else
        all_select_teachers.forEach(value => value.checked = false)
}

function selectAllStudent() {
    const select_all = document.querySelector('#select_all_student')
    const all_select_student = document.querySelectorAll('.select_one_student')
    if (select_all.checked)
        all_select_student.forEach(value => value.checked = true)
    else
        all_select_student.forEach(value => value.checked = false)
}

function selectAllCourse() {
    const select_all = document.querySelector('#select_all_course')
    const all_select_courses = document.querySelectorAll('.select_one_course')
    if (select_all.checked)
        all_select_courses.forEach(value => value.checked = true)
    else
        all_select_courses.forEach(value => value.checked = false)
}

function selectAllClassroom() {
    const select_all = document.querySelector('#select_all_classroom')
    const all_select_classrooms = document.querySelectorAll('.select_one_classroom')
    if (select_all.checked)
        all_select_classrooms.forEach(value => value.checked = true)
    else
        all_select_classrooms.forEach(value => value.checked = false)
}

function selectAllPreCourse() {
    const select_all = document.querySelector('#select_all_precourse')
    const all_select_pre = document.querySelectorAll('.select_one_precourse')
    if (select_all.checked)
        all_select_pre.forEach(value => value.checked = true)
    else
        all_select_pre.forEach(value => value.checked = false)
}

function selectAllMyCourse() {
    const select_all = document.querySelector('#select_all_mycourse')
    const all_select_mycourses = document.querySelectorAll('.select_one_mycourse')
    if (select_all.checked)
        all_select_mycourses.forEach(value => value.checked = true)
    else
        all_select_mycourses.forEach(value => value.checked = false)
}

function selectAllMyTeachCourse() {
    const select_all = document.querySelector('#select_all_myteachcourse')
    const all_select_myteachcourse = document.querySelectorAll('.select_one_myteachcourse')
    if (select_all.checked)
        all_select_myteachcourse.forEach(value => value.checked = true)
    else
        all_select_myteachcourse.forEach(value => value.checked = false)
}

function selectAllScoreList() {
    const select_all = document.querySelector('#select_all_scorelist')
    const all_select_scorelist = document.querySelectorAll('.select_one_scorelist')
    if (select_all.checked)
        all_select_scorelist.forEach(value => value.checked = true)
    else
        all_select_scorelist.forEach(value => value.checked = false)
}


window.onload = function () {
    const lasturl = window.document.referrer;
    console.log({lasturl});
    if (lasturl.indexOf('/schools') !== -1)
        showSchool();
    else if (lasturl.indexOf('/majors') !== -1)
        showMajor();
    else if (lasturl.indexOf('/teachers') !== -1)
        showTeacher();
    else if (lasturl.indexOf('/students') !== -1)
        showStudent();
    else if (lasturl.indexOf('/courses') !== -1)
        showCourse();
    else if (lasturl.indexOf('/classrooms') !== -1)
        showClassroom();
    else if (lasturl.indexOf('/precourses') !== -1)
        showPreCourse();
    else if (lasturl.indexOf('/mycourses') !== -1)
        showMyCourse();
    else if (lasturl.indexOf('/myteachcourses') !== -1)
        showMyTeachCourse();
    else if (lasturl.indexOf('/scorelist') !== -1)
        showScoreList();
    else;
}