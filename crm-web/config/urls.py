from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page

urlpatterns = [
    path("", landing_page),
    path("admin/", admin.site.urls),
    path("leads/", include("leads.urls", namespace="leads")),
]