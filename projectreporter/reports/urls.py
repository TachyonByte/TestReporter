from django.urls import path

from .views import (ProjectCreateView, ProjectListView,
                    ProjectDetailView, ProjectUpdateView, SystemCreateView,
                    SystemDetailView, SystemListView, SystemUpdateView,
                    FeatureCreateView, FeatureDetailView, FeatureListView, FeatureUpdateView)

app_name = "reports"

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('new-project/', ProjectCreateView.as_view(), name='new-project'),
    path('', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('Updatde-project/<int:pk>/', ProjectUpdateView.as_view(), name='update-project'),

    path('new-system/', SystemCreateView.as_view(), name='new-system'),
    path('systems/', SystemListView.as_view(), name='systems'),
    path('systems/<int:pk>/', SystemDetailView.as_view(), name='system_detail'),
    path('Updatde-project/<int:pk>/', SystemUpdateView.as_view(), name='update-system'),

    path('new-feature/', FeatureCreateView.as_view(), name='new-feature'),
    path('features/', FeatureListView.as_view(), name='features'),
    path('features/<int:pk>/', FeatureDetailView.as_view(), name='feature_detail'),
    path('Updatde-feature/<int:pk>/', FeatureUpdateView.as_view(), name='update-feature'),
]
