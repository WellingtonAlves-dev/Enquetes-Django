from django.db import models
from django_quill.fields import QuillField
from django.utils.html import mark_safe

# Create your models here.
class Options(models.Model):
    option = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option

class Polls(models.Model):
    title = models.CharField(max_length=255)
    description = QuillField(null=True)
    is_published = models.BooleanField(default=False)
    options = models.ManyToManyField(Options)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cover_preview(self):
        if self.cover:
            return mark_safe("<img src='{}' width='300px' height='300px'/>".format(self.cover.url))
        return ""
    def __str__(self):
        return self.title