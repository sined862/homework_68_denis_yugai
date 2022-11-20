from django.urls import path
from accounts.views import RegisterView, LoginUserView, Profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
]