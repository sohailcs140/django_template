# some description
from django.contrib import admin
from django.urls import path
from django.core import *

urlpatterns = [
    path('admin/', admin.site.urls),
]
