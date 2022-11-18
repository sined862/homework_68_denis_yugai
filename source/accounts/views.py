from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from accounts.forms import CustomUserCreationForm, LoginUserForm
from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

# class LoginView(TemplateView):
#     template_name = 'login.html'
#     form = LoginForm

#     def get(self, request, *args, **kwargs):
#         next = request.GET.get('next')
#         form_data = {} if not next else {'next': next}
#         form = self.form(form_data)
#         context = {'form': form}
#         return self.render_to_response(context)

#     def post(self, request, *args, **kwargs):
#         form = self.form(request.POST)
#         if not form.is_valid():
#             return redirect('login')
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         next = form.cleaned_data.get('next')
#         user = authenticate(request, username=username, password=password)
#         if not user:
#             return redirect('login')
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('profile')

class ProfileView(TemplateView):
    template_name = 'profile.html'

