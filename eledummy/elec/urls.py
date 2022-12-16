from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('choose_course',views.choose_course,name="choose_course"),
    path('course_allotment',views.course_allotment,name="course_allotment"),
    path('display_profile',views.display_profile,name="display_profile"),
    path('update_profile',views.update_profile,name="update_profile"),

]
