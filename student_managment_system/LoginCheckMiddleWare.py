from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_managment_system.HodViews":
                    pass
                elif modulename == "student_managment_system.views" or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename == "django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("index"))
            elif user.user_type == "2":
                if modulename == "student_managment_system.StaffViews":
                    pass
                elif modulename == "student_managment_system.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_panal"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("dologin") or modulename == "student_managment_system.views" :
                pass
            else:
                return HttpResponseRedirect(reverse("login"))