from django.contrib import admin
from accounts.models import Movie,MovieUser
# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieUser)