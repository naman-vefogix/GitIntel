from django.urls import path
from . import views

urlpatterns = [
    path('analyze/',views.GithubAnalyzerAPIView.as_view(), name='github_analyzer'),
    path('repos/',views.GithubRepoFetchView.as_view(), name='github_repos'),
]