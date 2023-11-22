from django.db import models
from django.contrib.auth.models import User
from projects.models import System, Feature, Project


class TestCase(models.Model):
    """
    Model to store information about test cases.

    Attributes:
        system (ForeignKey): The system that test relates to.
        feature (ForeignKey): The feature that test relates to.
        name (CharField): Name of test case.
        description (TextField): Info of the test case.
        created_by (ForeignKey): Creator of the test case.
        created_at (DateTimeField): Test created on(date and time).
        updated_at (DateTimeField): Test updated on(date and time).
    """
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ChildTestCase(models.Model):
    """
    Model to store sub tests of TestCase instances.

    Attributes:
        parent (ForeignKey): Testcase that this test is related to.
        name (CharField): Name of the test.
        description (TextField): information of the test.
        created_by (ForeignKey): Creator of the test case.
        created_at (DateTimeField): Test created on(date and time).
        updated_at (DateTimeField): Test updated on(date and time).
    """
    parent = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
