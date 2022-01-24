"""check_splitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.urls import urlpatterns as auth_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter

from receipts.views import CheckViewSet

router = DefaultRouter(trailing_slash=False)
router.register('checks', CheckViewSet, basename='checks')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ignore dj-rest-auth UserDetailsView
    path('auth/', include([url for url in auth_urls if url.name != 'rest_user_details'])),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('users/', include('users.urls')),
]

urlpatterns.extend(router.urls)

# Add django-silk URLs when DEBUG=True
if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

# Prefix all URLs with API prefix
urlpatterns = [path('api/', include(urlpatterns))]

# Serve media files using Django when DEBUG=True
if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
