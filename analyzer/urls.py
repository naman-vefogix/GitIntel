from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('analyze/',views.GithubAnalyzerAPIView.as_view(), name='github_analyzer'),
    path('repos/',views.GithubRepoFetchView.as_view(), name='github_repos'),
    path('insights/', views.GithubProfileAnalyzeView.as_view(), name="github_profile_insights")
]