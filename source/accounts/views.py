from django.contrib.auth import login, logout
from accounts.forms import CustomUserCreationForm, LoginUserForm
from django.views.generic import TemplateView, CreateView, View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView


def logout_view(request):
    logout(request)
    return redirect('login')

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = '/'
    extra_context = {'title': 'Регистрация пользователя'}

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Авторизация пользователя'}
    

class Profile(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_employer:
            return redirect ('index_employer')
        else:
            return redirect ('index_applicant')





