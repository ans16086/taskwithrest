from django.urls import path
from django.views.generic import TemplateView
from userprofapi.views import *

app_name = 'userprof'
urlpatterns = [


#path('',TemplateView.as_view(template_name = "userprof.html")),
path('userp/',userprofo) ,
path('userregis/',registrationuser) ,
path('login/',login),
path('data/',show_data),
path('data_p/',person_data.as_view()),
path('person/',person.as_view())

  ]