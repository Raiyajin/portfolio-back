from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    """
    A class model about the projects completed
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=32, blank=False, null=False, verbose_name="Title")
    image = models.ImageField(verbose_name="Image", null=True, blank=True)
    description = models.CharField(max_length=32, blank=True, null=True, verbose_name="Description")
    tags = ArrayField(models.CharField(max_length=8, blank=False, null=False), size=5, verbose_name="Tags",blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")
    link = models.CharField(max_length=64, blank=True, null=True, verbose_name="Link")


class ProjectImageModel(models.Model):
    image_url = models.ImageField("images", blank=True, null=True)