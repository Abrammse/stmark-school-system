"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.views.static import serve
from school import settings
from student_managment_system import views,HodViews,StaffViews
from django.conf.urls import handler404


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.showloginPage,name="login"),
   path('dologin', views.doLogin,name='dologin'),
   path('index',HodViews.index, name='index'),
   path('all_events/', HodViews.all_events, name='all_events'),
   path('add_event/', HodViews.add_event, name='add_event'),
     path('update/', HodViews.update, name='update'),
   path('remove/', HodViews.remove, name='remove'),
   path('get_user', views.GetUserDetails),
    path('logout_user', views.logout_user,name='logout_user' ),
   path('add_staff', HodViews.add_staff, name="add_staff"),
   path('add_staff_save', HodViews.add_staff_save, name="add_staff_save"),
   path('delete_staff/<int:pk>/', HodViews.delete_staff, name='delete_staff'),
   path('delete_admin/<int:pk>/', HodViews.delete_admin, name='delete_admin'),
   path('add_admin', HodViews.add_admin, name="add_admin"),
   path('manage_admin', HodViews.manage_admin, name="manage_admin"),
    path('add_admin_save', HodViews.add_admin_save, name="add_admin_save"),
   path('delete_student/<int:pk>/', HodViews.delete_student, name="delete_student"),
    path('delete_course/<int:pk>/', HodViews.delete_course, name="delete_course"),
   path('add_course', HodViews.add_course, name="add_course"),
   path('add_min', HodViews.add_min, name="add_min"),
   path('staff_take_attendance_staff', HodViews.staff_take_attendance_staff, name="staff_take_attendance_staff"),
   path('staff_take_attendance_save_staff', HodViews.staff_take_attendance_save_staff, name="staff_take_attendance_save_staff"),
   path('staff_view_attendance_staff', HodViews.staff_view_attendance_staff, name="staff_view_attendance_staff"),
    path('export-excel/',HodViews.export_data_to_excel, name='export_excel'),
    path('delete_subject/<int:pk>/', HodViews.delete_subject, name="delete_subject"),
     path('add_student_saveexel', HodViews.add_student_saveexel, name="add_student_saveexel"),
     path('add_staff_saveexel', HodViews.add_staff_saveexel, name="add_staff_saveexel"),
 path('add_course_save', HodViews.add_course_save, name="add_course_save"),
   path('add_student', HodViews.add_student, name="add_student"),
   path('add_student_save', HodViews.add_student_save, name="add_student_save"),
   path('add_subject', HodViews.add_subject, name="add_subject"),
   path('add_subject_save', HodViews.add_subject_save, name="add_subject_save"),
   path('manage_staff', HodViews.manage_staff, name="manage_staff"),
   path('manage_student', HodViews.manage_student, name="manage_student"),
   path('manage_course', HodViews.manage_course, name="manage_course"),
   path('manage_subject', HodViews.manage_subject, name="manage_subject"),
   path('edit_staff/<int:staff_id>', HodViews.edit_staff, name="edit_staff"),
   path('edit_admin/<int:staff_id>', HodViews.edit_admin, name="edit_admin"),
   path('add_session', HodViews.add_session, name="add_session"),
   path('add_session_save', HodViews.add_session_save, name="add_session_save"),
   path('edit_student/<int:staff_id>', HodViews.edit_student, name="edit_student"),
   path('edit_admim_save', HodViews.edit_admin_save, name="edit_admim_save"),
   path('edit_student_save', HodViews.edit_student_save, name="edit_student_save"),
   path('edit_staff_save', HodViews.edit_staff_save, name="edit_staff_save"),
   path('edit_subject/<str:subject_id>', HodViews.edit_subject, name="edit_subject"),
   path('edit_subject_save', HodViews.edit_subject_save, name="edit_subject_save"),
   path('edit_course/<str:course_id>', HodViews.edit_course, name="edit_course"),
   path('edit_course_save', HodViews.edit_course_save, name="edit_course_save"),
   path('manage_session', HodViews.manage_session, name="manage_session"),
   path('chrange_settings', HodViews.chrange_settings, name="chrange_settings"),
   path('chrange_settings_save', HodViews.chrange_settings_save, name="chrange_settings_save"),
   path('chrange_setting2_save', HodViews.chrange_setting2_save, name="chrange_setting2_save"),
   path('chrange_settings2', HodViews.chrange_settings2, name="chrange_settings2"),

   #staff uls

   path('staff_panal', StaffViews.index, name='staff_panal'),
   path('staff_take_attendance', StaffViews.staff_take_attendance, name='staff_take_attendance'),

   path('staff_view_attendance', StaffViews.staff_view_attendance, name='staff_view_attendance'),

   path('staff_take_attendance_save', StaffViews.staff_take_attendance_save, name='staff_take_attendance_save'),

   path('staff_view_student', StaffViews.staff_view_student, name='staff_view_student'),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

     re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )




handler404 = 'student_managment_system.views.custom_404'


