from django.urls import path
from . import views

urlpatterns=[
    path('studenthome/' , views.studenthome , name = 'studenthome'),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
    path('response/',views.response,name='response'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('postquestion/',views.postquestion,name='postquestion'),
    path('postanswer/<qid>',views.postanswer,name='postanswer'),
    path('postans/',views.postans,name='postans'),
    path('viewanswer/<qid>',views.viewanswer,name='viewanswer'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('viewsmat/',views.viewsmat,name='viewsmat'),
    path('viewassign/',views.viewassign,name='viewassign'),
    
]