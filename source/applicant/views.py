from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, View, DeleteView, UpdateView, CreateView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from applicant.models import Resume, WorkExperience, Education
from applicant.forms import work_experience_formset, ResumeForm, education_formset, WorkForm
from accounts.models import Account
from django.forms import formset_factory

def index(request):
    return render(request, 'applicant/index.html')



class ProfileApplicantView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'applicant/profile.html'
    context_object_name = 'user_obj'
    fields =['username', 'first_name', 'phone', 'email', 'telegram', 'facebook', 'linkedin', 'avatar']

    def get_success_url(self):
        return reverse('profile_applicant', kwargs={'pk': self.request.user.id})



class ProfileDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('login')


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("login")
    template_name = "applicant/password_change_form.html"


class ResumeCreationView(View):
    def get(self, *args, **kwargs):
        form_resume = ResumeForm
        form_work = work_experience_formset(queryset=WorkExperience.objects.none())
        form_education = education_formset(queryset=Education.objects.none())
        return render(self.request, 'applicant/resume_add.html', {'form_resume': form_resume, 'form_work': form_work, 'form_education': form_education})

    def post(self, *args, **kwargs):
        form_resume = ResumeForm(self.request.POST)
        form_work = work_experience_formset(data=self.request.POST, queryset=WorkExperience.objects.none())
        form_education = education_formset(data=self.request.POST, queryset=Education.objects.none())
        if all([form_resume.is_valid(), form_work.is_valid(), form_education.is_valid()]):
            resume = form_resume.save(commit=False)
            author = get_object_or_404(Account, pk=self.request.user.id)
            resume.author = author
            resume.save()
            for form in form_work.cleaned_data:
                if form:
                    begin_date = form['begin_date']
                    end_date = form['end_date']
                    position = form['position']
                    organization = form['organization']
                    responsibility = form['responsibility']
                    resume_id = resume
                    work = WorkExperience.objects.create(begin_date=begin_date, end_date=end_date, position=position, organization=organization, responsibility=responsibility, resume=resume_id)
                    work.save()
            for form in form_education.cleaned_data:   
                if form:
                    title = form['title']
                    faculty = form['faculty']
                    speciality = form['speciality']
                    end_date_education = form['end_date_education']
                    resume_id = resume
                    education = Education.objects.create(title=title, faculty=faculty, speciality=speciality, end_date_education=end_date_education, resume=resume_id)
                    education.save()
            return redirect('index_applicant')
        else:
            form_resume = ResumeForm(self.request.POST)
            form_work = work_experience_formset(self.request.POST)
            form_education = education_formset(self.request.POST)
            return render(self.request, 'applicant/resume_add.html', {'form_resume': form_resume, 'form_work': form_work, 'form_education': form_education})



class ResumesView(LoginRequiredMixin, ListView):
    template_name = 'applicant/resumes.html'
    model = Resume
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.filter(author=self.request.user, is_published=True)



class ResumeDetailView(DetailView):
    template_view = 'applicant/resume_detail.html'
    model = Resume