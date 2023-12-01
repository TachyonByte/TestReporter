from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from cases.models import TestCase
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
        context["reports"] = Report.objects.filter(features=self.kwargs["pk"])
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
    success_url = reverse_lazy('reports:projects')

# System List, Create, Update Views


class SystemListView(LoginRequiredMixin, ListView):
    model = System
    template_name = "reports/project_detail.html"
    context_object_name = "systems"


class SystemCreateView(LoginRequiredMixin, CreateView):
    model = System
    fields = ['name', 'description']
    template_name = "reports/system_create.html"
    context_object_name = "new_system"

    def get_success_url(self):
        return reverse_lazy('reports:project_detail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class SystemUpdateView(LoginRequiredMixin, UpdateView):
    model = System
    fields = "__all__"
    template_name = "reports/system_update.html"
    context_object_name = "update_system"

    def get_success_url(self):
        referer_url = self.request.META.get("HTTP_REFERER")
        if referer_url:
            return referer_url
        else:
            return reverse_lazy('reports:projects')

# Feature List, Create, Update Views


class FeatureListView(LoginRequiredMixin, ListView):
    model = Feature
    template_name = "reports/pages.html"
    context_object_name = "features"


class FeatureCreateView(LoginRequiredMixin, CreateView):
    model = Feature
    fields = ['name', 'description',]
    template_name = "reports/feature_create.html"
    context_object_name = "new_features"

    def get_success_url(self):
        return reverse_lazy('reports:project_detail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Feature
    fields = ['name', 'description']
    template_name = "reports/feature_update.html"
    context_object_name = "update_features"

    def get_success_url(self):
        referer_url = self.request.META.get("HTTP_REFERER")
        if referer_url:
            return referer_url
        else:
            return reverse_lazy('reports:projects')


class FeatureDetailView(LoginRequiredMixin, DetailView):
    model = Feature
    template_name = "reports/feature_detail.html"
    context_object_name = "feature_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["features"] = Feature.objects.filter(project=self.kwargs["pk"])
        context["testcases"] = TestCase.objects.filter(
            feature=self.kwargs["pk"])
        return context

# TestCases List, Create, Detail, Update


class TestCaseListView(LoginRequiredMixin, ListView):
    model = TestCase
    template_name = "reports/testcases.html"
    context_object_name = "testcases"


class TestCaseCreateView(LoginRequiredMixin, CreateView):
    model = TestCase
    fields = ['system', 'name', 'description',]
    template_name = "reports/testcase_create.html"
    context_object_name = "new_testcases"

    def get_success_url(self):
        return reverse_lazy('reports:feature-detail',
                            kwargs={'pk': self.kwargs['pk']})
   
    def form_valid(self, form):
        form.instance.feature = Feature.objects.get(pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TestCaseUpdateView(LoginRequiredMixin, UpdateView):
    model = TestCase
    fields = ['name', 'description']
    template_name = "reports/testcase_update.html"
    context_object_name = "update_testcases"
    success_url = reverse_lazy("reports:projects")

# Report List, Create, Detail, Update


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = "reports/reports.html"
    context_object_name = "reports"


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ['name', 'features',]
    template_name = "reports/report_create.html"
    context_object_name = "new_reports"

    def get_success_url(self):
        return reverse_lazy('reports:project_detail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        obj = Report.objects.get(name=form.cleaned_data.get('name'))
        test_cases = TestCase.objects.filter(
            feature__in=form.cleaned_data.get('features'))
        for test in test_cases:
            test_result = TestResult.objects.create(
                report=obj, testcase=test,
            )
            test_result.save()
        return super().form_valid(form)


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = "reports/report_detail.html"
    context_object_name = "reports_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["result"] = TestResult.objects.filter(report=self.kwargs["pk"])
        return context


class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    fields = ["is_done"]
    template_name = "reports/reports_update.html"
    context_object_name = "update_reports"

    def get_success_url(self):
        return reverse_lazy('reports:project_detail',
                            kwargs={'pk': self.kwargs['p_pk']})

# TestResult List, Create, Detail, Update


class TestResultListView(LoginRequiredMixin, ListView):
    model = TestResult
    template_name = "reports/result.html"
    context_object_name = "result"


class TestResultCreateView(LoginRequiredMixin, CreateView):
    model = TestResult
    fields = '__all__'
    template_name = "reports/testresult_create.html"
    context_object_name = "new_testresult"
    success_url = reverse_lazy('reports:report')


class TestResultUpdateView(LoginRequiredMixin, UpdateView):
    model = TestResult
    fields = '__all__'
    template_name = "reports/testresult_update.html"
    context_object_name = "update_result"
    success_url = reverse_lazy("reports:projects")
