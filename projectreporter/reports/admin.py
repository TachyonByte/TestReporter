from django.contrib import admin
from .models import Report, TestResult


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["name", "features", "created_by", "is_done", "created_at"]


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ["report", "testcase", "comment", "result", "tested_by",
                    "created_at", "updated_at"]
