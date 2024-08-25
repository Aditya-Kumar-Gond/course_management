"""
URL configuration for courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_course', views.all_courses, name='all_courses'),
    path('add_course',views.add_course,name='add_course'),
    path('del_course/<int:course_id>', views.del_course, name='delete course'),

    path('del_course_ins/<int:course_id>', views.del_course_ins, name='delete course instance'),

    path('all_courseIns', views.all_courses_ins, name='all_coursesIns'),
    path('add_courseIns',views.add_course_ins,name='add_courseIns'),
    path('show_selected_data/<int:course_id>',views.show_selected_data,name='show_selected_data'),
    path('show_selected_data_ins/<int:course_id>', views.show_selected_data_ins, name='show_selected_data_ins'),

]
