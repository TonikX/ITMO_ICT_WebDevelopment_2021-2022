"""hospital_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from hospital_app import views



router = DefaultRouter()
router.register(r'cabinetofficer', views.CabinetOfficerAPIView)
router.register(r'visit', views.VisitAPIView)
router.register(r'patient', views.PatientAPIView)
router.register(r'doctor', views.DoctorAPIView)
router.register(r'specialization', views.SpecializationAPIView)
router.register(r'cabinet', views.CabinetAPIView)
router.register(r'pricelist', views.PriceListAPIView)
router.register(r'medicalcard', views.MedicalCardAPIView)
router.register(r'scheduleofdoctor', views.ScheduleOfDoctorAPIView)
router.register(r'scheduleofcabinet', views.ScheduleOfCabinetAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital_app.urls')),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path(r'docs/', include('django_mkdocs.urls', namespace='documentation')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
