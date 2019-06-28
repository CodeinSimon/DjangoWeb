# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save


# here is my database
#
#
#
#
#

# Create your models here.


class School(models.Model):
    school_id = models.CharField(primary_key=True, max_length=4, verbose_name='学院代码', unique=True, default='XXXX')
    school_name = models.CharField(max_length=50, unique=True, verbose_name='学院', default='aSchool')

    def __str__(self):
        return self.school_name


class Major(models.Model):
    major_id = models.CharField(primary_key=True, max_length=8, verbose_name='专业代码', unique=True, default='XXXX0001')
    major_name = models.CharField(max_length=50, verbose_name='专业', default='aMajor')
    major_school = models.ForeignKey('School', verbose_name='隶属', to_field='school_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.major_name


class Teacher(models.Model):
    teacher_id = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='工号', default='00000')
    teacher_name = models.CharField(max_length=50, verbose_name='姓名', default='aTeacher')
    teacher_sex = models.CharField(max_length=20, choices=(('male', '男'), ('female', '女')), verbose_name='性别',
                                   default='male')
    teacher_age = models.IntegerField(default=40, verbose_name='年龄')
    teacher_title = models.CharField(max_length=20, verbose_name='职称',
                                     choices=(
                                         ('Assistant', '助教'), ('Lecturer', '讲师'),
                                         ('Associate Professor', '副教授'), ('Professor', '教授')),
                                     default='Lecturer')
    teacher_salary = models.FloatField(verbose_name='月薪', default=8000.00)
    teacher_school = models.ForeignKey('School', verbose_name='就职学院', to_field='school_id',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=11, unique=True, verbose_name='学号', default='00000000000')
    stu_name = models.CharField(max_length=50, verbose_name='姓名', default='aStudent')
    stu_sex = models.CharField(max_length=20, verbose_name='性别', choices=(('male', '男'), ('female', '女')),
                               default='male')
    stu_age = models.IntegerField(default=20, verbose_name='年龄')
    stu_major = models.ForeignKey('Major', to_field='major_id', verbose_name='专业', default='计算机科学与技术',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.stu_name


class Classroom(models.Model):
    #  classroom_id = models.AutoField(primary_key=True, unique=True, verbose_name='编号')
    classroom_id = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='教室编号', default='X0000')
    classroom_capacity = models.IntegerField(verbose_name='教室容量', default=40)

    def __str__(self):
        return self.classroom_id


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=9, unique=True, verbose_name='课程代码', default='XXXX00000')
    course_name = models.CharField(max_length=50, unique=True, default='aCourse', verbose_name='课程')
    course_capacity = models.IntegerField(verbose_name='课程容量', default=40)
    course_teacher_id = models.ForeignKey('Teacher', to_field='teacher_id', verbose_name='授课教师（工号）',
                                          on_delete=models.CASCADE)
    course_classroom_id = models.ForeignKey('Classroom', to_field='classroom_id', verbose_name='上课教室',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class SelectCourse(models.Model):
    sc_stu_id = models.ForeignKey('Student', to_field='stu_id', verbose_name='学号', on_delete=models.CASCADE)
    sc_course_id = models.ForeignKey('Course', to_field='course_id', verbose_name='课程代码', on_delete=models.CASCADE)
    sc_score = models.IntegerField(verbose_name='成绩', default=60)


class PreCourse(models.Model):
    cur_course_id = models.OneToOneField('Course', to_field='course_id', unique=True, related_name='cur_course_id',
                                         verbose_name='课程代码', on_delete=models.CASCADE)
    pre_course_id = models.OneToOneField('Course', to_field='course_id', unique=True, related_name='pre_course_id',
                                         verbose_name='先修课程代码', on_delete=models.CASCADE)


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    user_belong = models.CharField(max_length=10,
                                   choices=(('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher')),
                                   default='admin')
    user_number = models.CharField(max_length=11, unique=True, verbose_name='绑定信息', default='000000')

    def __str__(self):
        return self.user.username
