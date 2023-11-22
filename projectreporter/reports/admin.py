from django.contrib import admin
from .models import Report, TestResult


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["name", "created_by", "is_done", "created_at"]
    search_fields = ["name"]


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ["report", "testcase", "comment", "result", "tested_by",
                    "created_at", "updated_at"]
