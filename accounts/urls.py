from . import views
from django.urls import path , include

app_name = 'job'

urlpatterns = [
    path('signup', views.signup , name = 'signup'),

    
]
