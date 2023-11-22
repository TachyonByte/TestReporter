from django.shortcuts import render
from django.urls import reverse_lazy
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["systems"] = System.objects.filter(project=self.kwargs["pk"])
        context["features"] = Feature.objects.filter(project=self.kwargs["pk"])
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = "reports/project_create.html"
    context_object_name = "new_project"
    success_url = reverse_lazy('reports:projects')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_project"

class SystemListView(LoginRequiredMixin, ListView):
    model = System
    template_name = "reports/project_detail.html"
    context_object_name = "systems"

class SystemCreateView(LoginRequiredMixin, CreateView):
    model = System
    fields = ['name', 'description', 'project']
    template_name = "reports/system_create.html"
    context_object_name = "new_system"
    success_url = reverse_lazy('reports:projects')



class SystemUpdateView(LoginRequiredMixin, UpdateView):
    model = System
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_system"

class FeatureListView(LoginRequiredMixin, ListView):
    model = Feature
    template_name = "reports/pages.html"
    context_object_name = "features"

class FeatureCreateView(LoginRequiredMixin, CreateView):
    model = Feature
    fields = '__all__'
    template_name = "reports/feature_create.html"
    context_object_name = "new_features"
    success_url = reverse_lazy('reports:projects')

class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Feature
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_features"