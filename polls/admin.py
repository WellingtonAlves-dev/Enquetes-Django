from django.contrib import admin
from .models import Options, Polls
# Register your models here.
@admin.register(Options)
class optionsView(admin.ModelAdmin):
    pass
@admin.register(Polls)
class PollsView(admin.ModelAdmin):
    title = "Enquete"
    search_fields = ["options__option"]
    readonly_fields = ['cover_preview']