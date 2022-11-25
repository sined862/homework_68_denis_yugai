from django.urls import path
from applicant.views import ProfileApplicantView, ProfileDeleteView, CustomPasswordChangeView, ResumeCreationView, ResumesView, ResumeDetailView, ApplicantIndexView


urlpatterns = [
    path('', ApplicantIndexView.as_view(), name='index_applicant'),
    path('profile/<int:pk>', ProfileApplicantView.as_view(), name='profile_applicant'),
    path('profile/<int:pk>/del', ProfileDeleteView.as_view(), name='profile_del'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('resume_add/', ResumeCreationView.as_view(), name='resume_add'),
    path('resumes/', ResumesView.as_view(), name='resumes'),
    path('resume_detail/<int:pk>', ResumeDetailView.as_view(), name='resume_detail')
]

