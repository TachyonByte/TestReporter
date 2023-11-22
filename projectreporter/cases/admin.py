from django.contrib import admin
from .models import TestCase, ChildTestCase


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ["system", "feature", "name", "description", "created_at",
                    "updated_at"]

@admin.register(ChildTestCase)
class ChildAdmin(admin.ModelAdmin):
    list_display = ["parent", "name", "description", "created_by",
                    "created_at", "updated_at"]
