from django.urls import path

from .views import (ProjectCreateView, ProjectListView,
                    ProjectDetailView, ProjectUpdateView,

                    SystemCreateView, SystemListView,
                    SystemUpdateView,

                    FeatureCreateView, FeatureListView,
                    FeatureUpdateView, FeatureDetailView,

                    TestCaseCreateView, TestCaseListView,
                    TestCaseUpdateView,

                    ReportCreateView, ReportDetailView,
                    ReportListView, ReportUpdateView,

                    TestResultListView, TestResultCreateView,
                    TestResultUpdateView,
                    )

app_name = "reports"

urlpatterns = [
    # Project Urls
    path('new-project/', ProjectCreateView.as_view(), name='new-project'),
    path('', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(),
         name='project_detail'),
    path('Updatde-project/<int:pk>/',
         ProjectUpdateView.as_view(), name='update-project'),

    # System Urls
    path('new-system/<int:pk>/', SystemCreateView.as_view(),
         name='new-system'),
    path('systems/', SystemListView.as_view(), name='systems'),
    path('Updatde-system/<int:pk>/',
         SystemUpdateView.as_view(), name='update-system'),

    # Feature Urls
    path('new-feature/<int:pk>/', FeatureCreateView.as_view(),
         name='new-feature'),
    path('features/', FeatureListView.as_view(), name='features'),
    path('Updatde-feature/<int:pk>/',
         FeatureUpdateView.as_view(), name='update-feature'),
    path('feature/<int:pk>/', FeatureDetailView.as_view(),
         name="feature-detail"),


    # TestCase Urls
    path('new-testcase/<int:pk>/',
         TestCaseCreateView.as_view(), name="new-testcase"),
    path('testcases/', TestCaseListView.as_view(), name="testcases"),
    path('Updatde-testcase/<int:pk>/',
         TestCaseUpdateView.as_view(), name="update-testcase"),

    # Report Urls
    path('new-report/', ReportCreateView.as_view(), name='new-report'),
    path('reports/', ReportListView.as_view(), name='reports'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('Updatde-report/<int:p_pk>/<int:pk>/',
         ReportUpdateView.as_view(), name='update-report'),

    # TestResult Urls
    path('new-testresult/', TestResultCreateView.as_view(),
         name='new-testresult'),
    path('testresult', TestResultListView.as_view(), name='testresults'),
    path('Updatde-testresult/<int:pk>/',
         TestResultUpdateView.as_view(), name='update-testresult'),
]
