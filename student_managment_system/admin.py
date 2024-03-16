from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_managment_system.models import CustomUser
from .models import Events,Staffs,Students,Subjects,Courses,AdminHOD,SessionYearModel,Attendance,AttendanceReport,settings,setting2,AttendanceReportstaff,Attendancestaff,Events
from import_export.admin import ImportExportModelAdmin
class UserModel(UserAdmin ,ImportExportModelAdmin):
    pass

class studentAdmin(ImportExportModelAdmin,admin.ModelAdmin):

 admin.site.register(CustomUser,UserModel)
admin.site.register(Attendancestaff,studentAdmin)
admin.site.register(AttendanceReportstaff)
admin.site.register(Staffs,studentAdmin)
admin.site.register(Subjects)
admin.site.register(AdminHOD)
admin.site.register(Courses)
admin.site.register(Students,studentAdmin)
admin.site.register(Attendance)
admin.site.register(SessionYearModel)
admin.site.register(AttendanceReport)
admin.site.register(settings)
admin.site.register(setting2)
admin.site.register(Events)







