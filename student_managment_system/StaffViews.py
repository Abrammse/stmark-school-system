from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from student_managment_system.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .models import Events,Staffs,Students,Subjects,Courses,AdminHOD,CustomUser,SessionYearModel,Attendance,AttendanceReport,settings,setting2
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
def index(request):
    all_events = Events.objects.all()
    admin_hod = Staffs.objects.get(admin=request.user)
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    course_id_list = []
    for subject in subjects:
        course = Courses.objects.get(id=subject.course_id.id)
        course_id_list.append(course.id)

    final_course = []
    # removing Duplicate Course ID
    for course_id in course_id_list:
        if course_id not in final_course:
            final_course.append(course_id)

    students_count = Students.objects.filter(course_id__in=final_course).count()

    # Fetch All Attendance Count
    attendance_count = Attendance.objects.filter(subject_id__in=subjects).count()
    subjects=Subjects.objects.filter(staff_id=request.user.id).count()
    course= Subjects.objects.filter(staff_id=request.user.id).values('course_id').distinct().count()

    setting=settings.object.last()
    settin=setting2.object.last()

    course_ids = Subjects.objects.filter(staff_id=request.user.id).values_list('course_id', flat=True).distinct()

    students_countty = Students.objects.filter(course_id__in=course_ids).count()

    context = {
        "events": all_events,
        "admin_hod":admin_hod,
        "settin":settin,
        "setting":setting,
        "subjects":subjects,
        "course":course,
        "students_count":students_count,
        "attendance_count":attendance_count,
        "students_countty":students_countty



    }
    return render(request, 'staff.html',context)


def staff_take_attendance(request):
    setting=settings.object.last()
    staff_id=Staffs.objects.get(admin=request.user.id)
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYearModel.object.filter(id__in=subjects.values_list('session_year_id', flat=True))
    action=request.GET.get('action')
    session_obj=None
    subject_obj=None
    students=None
    if action is  not None:
        if request.method== "POST":
            subject=request.POST.get("subject")
            session=request.POST.get("session")

            subject_obj=Subjects.objects.get(id=subject)
            session_obj=SessionYearModel.object.get(id=session)
            subjects=Subjects.objects.filter(id=subject)
            for i in subjects:
                student_id=i.course_id.id
                students=Students.objects.filter(course_id=student_id)

    return render(request,"add Attandance.html",{"subjects":subjects,"session_years":session_years ,"subject_obj":subject_obj , "session_obj":session_obj,"action":action,"students":students,"setting":setting,})
def staff_view_student(request):
    setting=settings.object.last()
    staff_id=Staffs.objects.get(admin=request.user.id)
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYearModel.object.filter(id__in=subjects.values_list('session_year_id', flat=True))
    action=request.GET.get('action')
    session_obj=None
    subject_obj=None
    students=None
    if action is  not None:
        if request.method== "POST":
            subject=request.POST.get("subject")
            session=request.POST.get("session")

            subject_obj=Subjects.objects.get(id=subject)
            session_obj=SessionYearModel.object.get(id=session)
            subjects=Subjects.objects.filter(id=subject)
            for i in subjects:
                student_id=i.course_id.id
                students=Students.objects.filter(course_id=student_id)

    return render(request,"view student staff.html",{"subjects":subjects,"session_years":session_years ,"subject_obj":subject_obj , "session_obj":session_obj,"action":action,"students":students,"setting":setting,})

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Attendance, AttendanceReport, Subjects, Students, SessionYearModel

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Subjects, SessionYearModel, Attendance, AttendanceReport, Students

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Subjects, SessionYearModel, Attendance, AttendanceReport, Students

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Subjects, SessionYearModel, Attendance, AttendanceReport, Students

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Subjects, SessionYearModel, Attendance, AttendanceReport, Students

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Subjects, SessionYearModel, Attendance, AttendanceReport, Students


def staff_take_attendance_save(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject")
        session = request.POST.get("session")
        attendance_date = request.POST.get("attendance_date")
        selected_student_ids = request.POST.getlist("student_id")  # Retrieve list of selected student IDs

        # Retrieve subject and session objects
        get_subject = Subjects.objects.get(id=subject_id)
        get_session_year = SessionYearModel.object.get(id=session)

        # Check if attendance for the given subject, session, and date already exists
        attendance, created = Attendance.objects.get_or_create(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year
        )

        # Get existing attendance reports for the given attendance
        existing_reports = AttendanceReport.objects.filter(attendance_id=attendance)

        # Create a dictionary to store existing reports by student ID
        existing_reports_dict = {report.student_id.id: report for report in existing_reports}

        # Iterate through selected student IDs
        for student_id in selected_student_ids:
            student = Students.objects.get(id=student_id)

            # Check if the student has an existing report
            if student.id in existing_reports_dict:
                # If the student already has a report, update its status
                existing_report = existing_reports_dict[student.id]
                existing_report.status = True
                existing_report.save()
            else:
                # If the student doesn't have a report, create a new one with status=True
                AttendanceReport.objects.create(
                    student_id=student,
                    attendance_id=attendance,
                    status=True,
                )

        messages.success(request, "Attendance successfully recorded")
        return HttpResponseRedirect(reverse("staff_take_attendance"))
    else:
        # Handle GET request
        pass


from .models import Students  # Update the import statement

def staff_view_attendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYearModel.object.filter(
        id__in=subjects.values_list('session_year_id', flat=True))

    attendance = Attendance.objects.filter(subject_id__in=subjects, session_year_id__in=session_years)

    action = request.GET.get('action')
    subject_obj = None
    session_obj = None
    attendance_obj = None
    attendance_report = None
    students_not_found = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject")
            session_id = request.POST.get("session")
            attendance_id = request.POST.get("attendance")

            subject_obj = Subjects.objects.get(id=subject_id)
            session_obj = SessionYearModel.object.get(id=session_id)
            attendance_obj = Attendance.objects.get(id=attendance_id)

            attendance = Attendance.objects.filter(subject_id=subject_obj,
                                                   attendance_date=attendance_obj.attendance_date)

            attendance_report = AttendanceReport.objects.filter(attendance_id=attendance_id)

            # Get the list of students who are supposed to attend the course
            students_registered = Students.objects.filter(course_id=subject_obj.course_id, session_year_id=session_obj)

            # Get the list of students who attended the class
            students_attended = [report.student_id for report in attendance_report]

            # Find students who are absent and not found in the attendance report
            students_not_found = students_registered.exclude(admin__in=[student.admin for student in students_attended])

    return render(request, "view Attandance.html", {
        "subjects": subjects,
        "session_years": session_years,
        "subject_obj": subject_obj,
        "session_obj": session_obj,
        "attendance":attendance,
        "action": action,
        "attendance_obj": attendance_obj,
        "attendance_report": attendance_report,
        "students_not_found": students_not_found
    })
