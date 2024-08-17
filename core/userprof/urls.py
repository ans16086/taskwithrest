from django.urls import path
from django.views.generic import TemplateView

app_name = 'userprof'
urlpatterns = [
path('',TemplateView.as_view(template_name = "userprof.html"))
]