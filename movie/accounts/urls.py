"""
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
from django.urls import path,include
from accounts import views


urlpatterns = [
     path('',views.home,name='home'),
    path('view-movies',views.view_movies, name = "view_movies"),
    path('create-user',views.create_user,name='create-user'),
    path('login',views.login_user,name='login_user'),
    path('logout',views.logout_user,name='logout_user'),
    path("add_movies", views.add_movies, name="add_movies"),
    path("update_movies/<str:pk>/",views.update_movies,name="update_movies"),
    path("delete_movies/<str:pk>/",views.delete_movies,name="delete_movies")

]