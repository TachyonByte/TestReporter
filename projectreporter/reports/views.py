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

# Project List, Detail, Create, Update Views
class ProjectListView(LoginRequiredMixin, ListView):
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

# System List, Create, Update Views
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

    def get_initial(self):
        initial = super().get_initial()
        initial['project'] = Project.objects.get(pk=self.kwargs['pk'])
        return initial

class SystemUpdateView(LoginRequiredMixin, UpdateView):
    model = System
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_system"

# Feature List, Create, Update Views
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

    def get_initial(self):
        initial = super().get_initial()
        initial['project'] = Project.objects.get(pk=self.kwargs['pk'])
        return initial

class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Feature
    fields = ['name', 'description']
    template_name = "reports/project_update.html"
    context_object_name = "update_features"


class FeatureDetailView(LoginRequiredMixin, DetailView):
    model = Feature
    template_name = "reports/feature_detail.html"
    context_object_name = "feature_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["features"] = Feature.objects.filter(project=self.kwargs["pk"])
        context["testcases"] = TestCase.objects.filter(feature=self.kwargs["pk"])
        return context

# TestCases List, Create, Detail, Update

class TestCaseListView(LoginRequiredMixin, ListView):
    model = TestCase
    template_name = "reports/testcases.html"
    context_object_name = "testcases"

class TestCaseCreateView(LoginRequiredMixin, CreateView):
    model = TestCase
    fields = '__all__'
    template_name = "reports/testcase_create.html"
    context_object_name = "new_testcases"
    success_url = reverse_lazy('reports:testcases')

    def get_initial(self):
        initial = super().get_initial()
        initial['feature'] = Feature.objects.get(pk=self.kwargs['pk'])
        # initial['system'] = System.objects.get(pk=self.kwargs['spk'])
        return initial

class TestCaseDetailView(LoginRequiredMixin, DetailView):
    model = TestCase
    template_name = "reports/testcase_detail.html"
    context_object_name = "testcase_detail"
    

class TestCaseUpdateView(LoginRequiredMixin, UpdateView):
    model = TestCase
    fields = ['name', 'description']
    template_name = "reports/testcase_update.html"
    context_object_name = "update_testcases"

# Report List, Create, Detail, Update

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = "reports/reports.html"
    context_object_name = "reports"

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = '__all__'
    template_name = "reports/reports_create.html"
    context_object_name = "new_reports"
    success_url = reverse_lazy('reports:testcases')

class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = "reports/reports_detail.html"
    context_object_name = "reports_detail"
    

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    fields = ['name', 'description']
    template_name = "reports/reports_update.html"
    context_object_name = "update_reports"

# TestResult List, Create, Detail, Update

class TestResultListView(LoginRequiredMixin, ListView):
    model = TestResult
    template_name = "reports/reports.html"
    context_object_name = "reports"

class TestResultCreateView(LoginRequiredMixin, CreateView):
    model = TestResult
    fields = '__all__'
    template_name = "reports/reports_create.html"
    context_object_name = "new_reports"
    success_url = reverse_lazy('reports:testcases')

class TestResultDetailView(LoginRequiredMixin, DetailView):
    model = TestResult
    template_name = "reports/reports_detail.html"
    context_object_name = "reports_detail"
    

class TestResultUpdateView(LoginRequiredMixin, UpdateView):
    model = TestResult
    fields = ['name', 'description']
    template_name = "reports/reports_update.html"
    context_object_name = "update_reports"