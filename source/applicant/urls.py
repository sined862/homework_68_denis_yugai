from django.urls import path
from applicant.views import ProfileApplicantView, ProfileDeleteView, CustomPasswordChangeView, ResumeCreationView, ResumesView, ResumeDetailView, IndexApplicantView, EmployerDetailView, JobDetailView, ResponsesView, ResponseApplicantDetailView


urlpatterns = [
    path('', IndexApplicantView.as_view(), name='index_applicant'),
    path('profile/<int:pk>', ProfileApplicantView.as_view(), name='profile_applicant'),
    path('profile/<int:pk>/del', ProfileDeleteView.as_view(), name='profile_del'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('resume_add/', ResumeCreationView.as_view(), name='resume_add'),
    path('resumes/', ResumesView.as_view(), name='resumes'),
    path('resume_detail/<int:pk>', ResumeDetailView.as_view(), name='resume_detail'),
    path('employer_detail/<int:pk>', EmployerDetailView.as_view(), name='employer_detail'),
    path('job_detail/<int:pk>', JobDetailView.as_view(), name='job_detail_response'),
    path('responses/', ResponsesView.as_view(), name='responses_applicant'),
    path('response_detail/<int:pk>', ResponseApplicantDetailView.as_view(), name='response_detail_applicant')
]

