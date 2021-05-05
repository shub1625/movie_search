from django.http import HttpResponse
from django.shortcuts import redirect
import functools


def unauthenticated_user(view_func):

    @functools.wraps(view_func)
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("view_movies")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_function


def authenticated_user(view_func):
    @functools.wraps(view_func)
    def wrapper_function(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_function




def allowed_hosts(allowed_roles=[]):
    def inner(view_func):
        @functools.wraps(view_func)
        def wrapper_function(request,*args,**kwargs):

            group = None

            print("*********")
            print(request.user.groups.all())
            if request.user.groups.exists():
                print("inside group is there")
                group = request.user.groups.all()[0].name
                print(group)
                print("Printed group")

            print(group)    
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
                # return HttpResponse("Wow logged in")
            else:
                return HttpResponse("You are not authorised to view this page")
        return wrapper_function
    return inner


def admin_only(view_func):
    @functools.wraps(view_func)
    def wrapper_function(request,*args,**kwargs):

        group = None 

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'user':
            return redirect("view_movies")
        
        if group == 'admin':
            return view_func(request,*args,**kwargs)
    return wrapper_function