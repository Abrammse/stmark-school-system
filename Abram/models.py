from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
    use_type=models.CharField(default=1,choices=user_type_data,max_length=10)
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    Subject_name=models.CharField(max_length=255)
    course_id= models.ForeignKey(Courses,on_delete=models.CASCADE)
    staff_id= models.ForeignKey(Staffs,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    gender= models.CharField(max_length=255)
    profile_pic= models.FileField()
    session_start_year=models.DateTimeField()
    session_end_year=models.DateTimeField()
    address= models.TextField()
    course_id= models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()





class Attandance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id= models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_data= models.DateTimeField(auto_now_add=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id= models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    leave_data= models.CharField(max_length=255)
    leave_message= models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id= models.ForeignKey(Staffs,on_delete=models.DO_NOTHING)
    leave_data= models.TextField()
    leave_message= models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class feedbackStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id= models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    feedback= models.CharField(max_length=255)
    feedback_reply= models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()




class NotificationStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id= models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()




class NotificationStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id= models.ForeignKey(Staffs,on_delete=models.DO_NOTHING)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class feedbackStaffs(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id= models.ForeignKey(Staffs,on_delete=models.DO_NOTHING)
    feedback= models.TextField()
    feedback_reply= models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects=models.Manager()





class AttandanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id= models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id= models.ForeignKey(Attandance,on_delete=models.DO_NOTHING)
    status=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)


