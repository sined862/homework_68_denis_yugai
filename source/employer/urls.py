from django.urls import path

from employer.views import IndexView, JobCreate, JobUpdateView, JobDeleteView, JobView, ProfileEmployertView, ProfileDeleteView, JobsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jobs/add/', JobCreate.as_view(), name='job_add'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('jobs/<int:pk>/confirm-delete/', JobDeleteView.as_view(), name='confirm_delete'),
    path('jobs/', JobsView.as_view(), name='jobs'),
    path('jobs/<int:pk>', JobView.as_view(), name='job_detail'),
    path('profile/<int:pk>', ProfileEmployertView.as_view(), name='profile_employer'),
    path('profile/<int:pk>/del', ProfileDeleteView.as_view(), name='profile_del'),
]
