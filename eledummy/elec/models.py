from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=30, null=True, blank=True)
    dept_short=models.CharField(max_length=5, null=True, blank=True)
    strength =models.IntegerField()
    course_offered =models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.dept_name

class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_code=models.CharField(max_length=8, null=True, blank=True)
    course_name = models.CharField(max_length=50, null=True, blank=True)
    course_dept=models.CharField(max_length=30, null=True, blank=True)
    syllabus =models.FileField(upload_to='syllabus',null=True )
    total_seats =models.IntegerField(default=60)
    filled_seats=models.IntegerField(default=0)
    vacancy=models.IntegerField(default=60)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    user = models.CharField(max_length=8,unique=True, blank=True)
    name=models.CharField(max_length=13, null=True, blank=True)
    mail=models.EmailField()
    mobile = models.CharField(max_length=13, null=True, blank=True)
    department=models.CharField(max_length=30, null=True, blank=True)
    course_chosen =models.CharField(max_length=50, null=True, blank=True)
    course_alloted=models.CharField(max_length=50, null=True, blank=True)
    updated_at =models.TimeField(auto_now=True)

    def __str__(self):
        return self.user

