from . import views , api
from django.urls import path , include

app_name = 'job'

urlpatterns = [
    path('', views.job_list , name = 'job_list'),
    path('add', views.add_job , name = 'add_job'),
    path('<str:slug>', views.job_details , name = 'job_detail'),
    path('api/jobs', api.job_list_api , name = 'job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api , name = 'job_detail_api'),
]
