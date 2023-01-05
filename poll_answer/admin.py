from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Answers_poll)
class Poll_answerView(admin.ModelAdmin):

    readonly_fields = ["email_user", "answers", "poll"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass
