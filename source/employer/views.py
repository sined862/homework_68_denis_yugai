from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.urls import reverse, reverse_lazy

from employer.forms import JobForm
from employer.models import Job


class IndexView(ListView):
    template_name = 'index.html'
    model = Job
    context_object_name = 'jobs'


class JobCreate(CreateView):
    template_name = 'job_create.html'
    form_class = JobForm
    model = Job

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.object.pk})


class JobView(DetailView):
    template_name = 'job.html'
    model = Job


class JobUpdateView(UpdateView):
    template_name = 'job_update.html'
    form_class = JobForm
    model = Job
    context_object_name = 'job'

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.object.pk})


class JobDeleteView(DeleteView):
    template_name = 'job_confirm_delete.html'
    model = Job
    success_url = reverse_lazy('index')

