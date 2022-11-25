from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from employer.forms import JobForm
from employer.models import Job



class ProfileEmployertView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'employer/profile.html'
    context_object_name = 'user_obj'
    fields =['username', 'first_name', 'phone', 'email', 'telegram', 'facebook', 'linkedin', 'avatar']

    def get_success_url(self):
        return reverse('profile_applicant', kwargs={'pk': self.request.user.id})

class ProfileDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('login')


class IndexView(ListView):
    template_name = 'employer/index.html'
    model = Job
    context_object_name = 'jobs'


class JobsView(ListView):
    template_name = 'employer/jobs.html'
    model = Job
    context_object_name = 'jobs'


class JobCreate(CreateView):
    template_name = 'employer/job_create.html'
    form_class = JobForm
    model = Job

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.object.pk})


class JobView(DetailView):
    template_name = 'employer/job.html'
    model = Job


class JobUpdateView(UpdateView):
    template_name = 'employer/job_update.html'
    form_class = JobForm
    model = Job
    context_object_name = 'job'

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.object.pk})


class JobDeleteView(DeleteView):
    template_name = 'employer/job_confirm_delete.html'
    model = Job
    success_url = reverse_lazy('index')

