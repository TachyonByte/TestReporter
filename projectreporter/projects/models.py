from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """
    Model to store information about Project.

    Attributes:
        name (CharField): Name of Project.
        description (TextField): Info of the project.
        created_at (DateTimeField): Project created on(date and time).
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class System(models.Model):
    """
    Model to store information about particular system of project.

    Attributes:
        project (ForeignKey): The project that system relates to.
        name (CharField): Name of system.
        description (TextField): Info of the system.
        created_at (DateTimeField): system created on(date and time).
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    """
    Model to store information about particular feature of system related
    to project.

    Attributes:
        project (ForeignKey): The project that feature relates to.
        name (CharField): Name of feature.
        description (TextField): Info of the feature.
        created_at (DateTimeField): feature created on(date and time).
        created_by (ForeignKey): Creator of feature.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
