from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.forms import CreateUserForm,MovieForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from accounts.models import Movie,MovieUser
from django.contrib import messages
from .filters import MovieFilter
from .decorators import admin_only,allowed_hosts,unauthenticated_user,authenticated_user
from django.contrib.auth.decorators import login_required
# Create your views here.


# @authenticated_user
@allowed_hosts(allowed_roles=['user','admin'])
def view_movies(request):
    movies = Movie.objects.all()  

    myFilter = MovieFilter(request.GET,queryset=movies)
    movies = myFilter.qs

 
    context = {'movies':movies,'myFilter':myFilter}
    return render(request,'accounts/viewmovies.html',context)


@unauthenticated_user
def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Opps Username already taken')
                    return redirect('create-user')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error((request,'Opps Email already exists'))
                        return redirect('create-user')
                    else:
                        user = form.save()
                        group = Group.objects.get(name='user')
                        user.groups.add(group)
                        print("%%%%%")
                        print(user.groups.all())
                        user.save()
                        MovieUser.objects.create(
                            user=user,
                            username = username,
                            email = email
                        )
                        
                        messages.success(request, 'Account was created for ' + username)
                        return redirect('login_user')
            else:
                print("came here")
                messages.error(request,'Password Don\'t match' )
                return redirect('create-user')
        else:
            print("came in outer else")
            messages.error(request,"What is this")
    context = {
        'form': form
    }
    return render(request,'accounts/create-user.html',context)


@unauthenticated_user
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request,'accounts/login.html',context)


def logout_user(request):
    logout(request)
    return redirect('login_user')

def home(request):
    if request.user.is_authenticated:
        return redirect("view_movies")
    return render(request,'accounts/home.html')


@login_required(login_url="login_user")
@allowed_hosts(allowed_roles=['admin'])
def add_movies(request):
    movie_user = request.user.movieuser
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)    
        if form.is_valid():
            f = form.save(commit=False)
            f.username = movie_user
            f.save()

            
            
    context = {'form': form}
    return render(request,"accounts/add_movies.html",context)

@login_required(login_url="login_user")
# @admin_only
# @allowed_hosts(allowed_roles=['admin'])
def update_movies(request,pk):
    print("*******")
    print(pk)
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('view_movies')

    context = {'form':form}
    return render(request,'accounts/add_movies.html',context)

@login_required(login_url="login_user")
# @allowed_hosts(allowed_roles=['admin'])
def delete_movies(request,pk):
    movie = Movie.objects.get(id=pk)

    if request.method == 'POST':
        movie.delete()
        return redirect('view_movies')
    
    context = {'movie':movie}

    return render(request,"accounts/delete.html",context)