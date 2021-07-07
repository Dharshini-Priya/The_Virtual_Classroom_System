"""loginSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from loginapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name='welcome'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('teacher',views.teacher,name='teacher'),
    path('sturegister',views.sturegister,name='sturegister'),
    path('student',views.student,name='student'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('stulogin',views.stulogin,name='stulogin'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('course',views.course,name='course'),
    path('createcourse',views.createcourse,name='createcourse'),
    path('coursestu',views.coursestu,name='coursestu'),
    path('coursedetails',views.coursedetails,name='coursedetails'),
    path('ex_home',views.ex_home,name='ex_home'),
    path('ass_home',views.ass_home,name='ass_home'),
    path('ass_create',views.ass_create,name='ass_create'),
    path('ex_create',views.ex_create,name='ex_create'),
    path('stu_exam',views.stu_exam,name='stu_exam'),
    path('stu_ass',views.stu_ass,name='stu_ass'),
    path('stu_ass_answer',views.stu_ass_answer,name='stu_ass_answer'),
    path('stu_exam_answer',views.stu_exam_answer,name='stu_exam_answer'),
    path('tea_sub',views.tea_sub,name='tea_sub'),
    path('ass_submit',views.ass_submit,name='ass_submit'),
    path('ex_submit',views.ex_submit,name='ex_submit'),
    path('ass_grade',views.ass_grade,name='ass_grade'),
    path('ex_grade',views.ex_grade,name='ex_grade'),
    path('stu_grade',views.stu_grade,name='stu_grade'),
    path('stu_ex_grade',views.stu_ex_grade,name='stu_ex_grade'),
    path('stu_ass_grade',views.stu_ass_grade,name='stu_ass_grade'),
    path('stu_resource',views.stu_resource,name='stu_resource'),
    path('stu_article',views.stu_article,name='stu_article'),
    path('stu_book',views.stu_book,name='stu_book'),
    path('book',views.book,name='book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

