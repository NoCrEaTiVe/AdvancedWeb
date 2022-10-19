from django.db import models
from core.models import CustomUser
# Create your models here.


class Student(CustomUser):
    USER_TYPE = 'student'
    group = models.ForeignKey('StudentGroup', null=True, on_delete=models.DO_NOTHING)


class UniversityStaff(CustomUser):
    USER_TYPE = 'staff'


class Specialization(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class StudentGroup(models.Model):
    name = models.CharField(max_length=255, null=False)
    curator = models.ForeignKey(UniversityStaff, null=True, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=255, null=False)
    specialization = models.ManyToManyField(Specialization)


class Courses(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(UniversityStaff, null=True, on_delete=models.DO_NOTHING)


class Exams(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    description = models.TextField()


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.DO_NOTHING)
    question = models.TextField()
    max_score = models.IntegerField()
    correct_option = models.CharField(max_length=255)


class ExamQuestionResults(models.Model):
    option = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    exam_question = models.ForeignKey(ExamQuestion, on_delete=models.DO_NOTHING)


class Appeals(models.Model):
    exam_question_result = models.F
    message = models.TextField()
    status = models.IntegerField()
    add_score = models.IntegerField()
    appealed_by = models.ForeignKey(Student, on_delete=models.CASCADE)


class CommentAppeals(models.Model):
    commented_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE)
    message = models.TextField()
    appeal = models.ForeignKey(Appeals, on_delete=models.CASCADE)
