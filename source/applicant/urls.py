from django.urls import path
from applicant.views import index, ProfileApplicantView, ProfileDeleteView, CustomPasswordChangeView


urlpatterns = [
    path('', index, name='index_applicant'),
    path('profile/<int:pk>', ProfileApplicantView.as_view(), name='profile_applicant'),
    path('profile/<int:pk>/del', ProfileDeleteView.as_view(), name='profile_del'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change')
]

