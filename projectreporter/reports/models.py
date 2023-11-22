from django.db import models
from django.contrib.auth.models import User
from projects.models import System, Feature, Project
from cases.models import TestCase

class Report(models.Model):
    name = models.CharField(max_length=90)
    features = models.ManyToManyField(Feature)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class TestResult(models.Model):
    RESULT_C=[
        ('untested', 'untested'),
        ('passed', 'passed'),
        ('failed', 'failed'),
    ]
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    comment = models.TextField()
    result = models.CharField(max_length=90, choices=RESULT_C, default='untested')
    tested_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.testcase)