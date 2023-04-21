from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.users import urls as user_url
from apps.projects import urls as project_url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include(user_url)),
    path("project/", include(project_url)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
