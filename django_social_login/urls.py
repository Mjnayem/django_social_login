
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user_auth.views import user_landing, custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_landing, name="user_landing"),
    path('custom_login', user_landing, name='custom_login'),

    path('accounts/', include('allauth.urls')),
    path('auth/', include('user_auth.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
