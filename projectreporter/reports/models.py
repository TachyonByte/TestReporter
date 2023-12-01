from django.db import models
from django.contrib.auth.models import User
from projects.models import Feature
from cases.models import TestCase


class Report(models.Model):
    """
    Model to store information about Report of Feature Tests.

    Attributes:
        name (CharField): Name of report.
        features (ManyToManyField): The Feature that report relates to.
        created_by (ForeignKey): Creator of report.
        is_done (BooleanField): status of report.
        created_at (DateTimeField): Report created on(date and time).
    """
    name = models.CharField(max_length=90)
    features = models.ManyToManyField(Feature)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name



class TestResult(models.Model):
    """
    Model to store information about Results of Tests.

    Attributes:
        report (ForeignKey): report that result relates to.
        testcase (ForeignKey): report that test case relates to.
        comment (TextField): comment on the result.
        result (CharField): result(untested, passed, failed)
        tested_by (ForeignKey): Tester of the test case.
        created_at (DateTimeField): result created on.
        updated_at (DateTimeField): result updated on.
    """
    RESULT_C = [
        ('untested', 'untested'),
        ('passed', 'passed'),
        ('failed', 'failed'),
    ]
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    result = models.CharField(max_length=90, choices=RESULT_C,
                              default='untested')
    tested_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.testcase)
