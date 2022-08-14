from math import prod
from django import views
from django.urls import path
from webapp.views import application, home,about, loginTeamMember, logoutUser,what_we_do,team,products,contactus,blog_indi,blogs,what_we_do_specific,career,applyjobs
app_name="mainweb"

urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('team/',team,name="team"),
    path('blogs/',blogs,name="blogs"),
    path('careers/',career,name="career"),
    path('application/',application,name="application"),
    path('login/',loginTeamMember,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('blogs/<str:blog_id>/',blog_indi,name="blogs_indi"),
    path('what-we-do/',what_we_do,name="what_we_do"),
    path('what-we-do/<str:typedev>/<str:typedevid>/',what_we_do_specific,name="what_we_do_specific"),
    path('our-products/',products,name="products"),
    path('contact-us/',contactus,name="contactus"),
    path('apply-jobs/',applyjobs,name="apply_jobs"),
]

