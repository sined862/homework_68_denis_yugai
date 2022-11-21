from django.urls import path

from employer.views import IndexView, JobCreate, JobUpdateView, JobDeleteView, JobView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jobs/add/', JobCreate.as_view(), name='job_add'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('jobs/<int:pk>/confirm-delete/', JobDeleteView.as_view(), name='confirm_delete'),
    path('jobs/', IndexView.as_view()),
    path('jobs/<int:pk>', JobView.as_view(), name='job_detail')
]
