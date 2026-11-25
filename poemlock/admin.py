from django.contrib import admin
from .models import Poem, Task


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ("title", "active", "created_at")
    list_filter = ("active", "created_at")
    search_fields = ("title", "body")
    ordering = ("-created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("order", "question", "digit")
    list_editable = ("digit",)
    ordering = ("order",)
    search_fields = ("question",)
