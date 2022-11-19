from django.urls import path
from applicant.views import index

urlpatterns = [
    path('', index, name='index_applicant')
]

