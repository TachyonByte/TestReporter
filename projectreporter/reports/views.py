from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,
                                    DeleteView, CreateView, UpdateView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from cases.models import TestCase, ChildTestCase
from projects.models import Project, System, Feature
from reports.models import Report, TestResult



# class HomePageView(TemplateView):
#     template_name = "reports/dashboard.html"

class ProjectListView( ListView):
    model = Project
    template_name = "reports/dashboard.html"
    context_object_name = "projects"

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "reports/project_detail.html"
    context_object_name = "project_detail"

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = "reports/project_create.html"
    context_object_name = "new_project"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_project"

class SystemListView(LoginRequiredMixin, ListView):
    model = System
    template_name = "reports/pages.html"
    context_object_name = "systems"

class SystemDetailView(LoginRequiredMixin, DetailView):
    model = System
    template_name = "reports/system_detail.html"
    context_object_name = "system_detail"

class SystemCreateView(LoginRequiredMixin, CreateView):
    model = System
    fields = ['name', 'description']
    template_name = "reports/project_create.html"
    context_object_name = "new_system"


class SystemUpdateView(LoginRequiredMixin, UpdateView):
    model = System
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_system"

class FeatureListView(LoginRequiredMixin, ListView):
    model = Feature
    template_name = "reports/pages.html"
    context_object_name = "features"

class FeatureDetailView(LoginRequiredMixin, DetailView):
    model = Feature
    template_name = "reports/project_detail.html"
    context_object_name = "features_detail"

class FeatureCreateView(LoginRequiredMixin, CreateView):
    model = Feature
    fields = ['name', 'description']
    template_name = "reports/project_create.html"
    context_object_name = "new_features"

class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Feature
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_features"