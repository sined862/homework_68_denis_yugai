from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import logout_view, is_autorization

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout_view, name='logout'),
    path("auth/", include('accounts.urls')),
    path("applicant/", include('applicant.urls')),
    path('employer/', include('employer.urls')),
    path('', is_autorization, name='is_autorization')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
