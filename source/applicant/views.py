from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, View, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView

def index(request):
    return render(request, 'applicant/index.html')



class ProfileApplicantView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'applicant/profile.html'
    context_object_name = 'user_obj'
    fields =['username', 'first_name', 'phone', 'email', 'telegram', 'facebook', 'linkedin', 'avatar']

    def get_success_url(self):
        return reverse('profile_applicant', kwargs={'pk': self.request.user.id})

    # def get_absolute_url(self):
    #     return reverse('profile', pk=self.request.user.id)


class ProfileDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('login')


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("login")
    template_name = "applicant/password_change_form.html"