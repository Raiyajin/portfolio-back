from django.urls import path
from .views import ProjectCreate, ProjectRetrieveUpdateDestroy

urlpatterns = [
    path("", ProjectCreate.as_view(), name="project-list-create"),
    path("<int:pk>/", ProjectRetrieveUpdateDestroy.as_view(), name="project-retrieve-update-destroy"),
]
