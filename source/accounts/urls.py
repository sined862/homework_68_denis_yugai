﻿from django.urls import path
from accounts.views import RegisterView, LoginUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login')
]