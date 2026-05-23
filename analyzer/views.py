import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GithubSerializer

# Create your views here.

class GithubAnalyzerAPIView(APIView):
    def post(self, request):
        serializer = GithubSerializer(data = request.data)
        if serializer.is_valid():
            github_url = serializer.validated_data['github_url']
            username = github_url.rstrip('/').split('/')[-1]
            api_url = f'https://api.github.com/users/{username}'
            response = requests.get(api_url)
            if response.status_code == 200:
                github_data = response.json()
                return Response(github_data)
            return Response({'error' : 'Github user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GithubRepoFetchView(APIView):
    def post(self,request):
        serializer = GithubSerializer(data = request.data)
        if serializer.is_valid():
            github_url = serializer.validated_data['github_url']
            username = github_url.rstrip('/').split('/')[-1]
            api_url = f'https://api.github.com/users/{username}/repos'
            response  = requests.get(api_url)
            if response.status_code == 200:
                github_data = response.json()
                repositories = []
                for repo in github_data:
                    repositories.append({
                        'name': repo.get('name'),
                        'description': repo.get('description'),
                        'language': repo.get('language'),
                        'languages_url': repo.get('languages_url'),
                        'stargazers_count': repo.get('stargazers_count'),
                        'topics': repo.get('topics'),
                        'commits_url': repo.get('commits_url'),
                    })
                return Response({
                    'username': username,
                    'repositories': repositories
                })
            return Response({'error' : 'Github user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    