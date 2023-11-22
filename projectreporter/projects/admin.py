from django.contrib import admin
from .models import Project, System, Feature


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at"]


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ["project", "name", "description", "created_at"]


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ["project", "name", "description", "created_at",
                    "created_by"]
