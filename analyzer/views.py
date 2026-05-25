import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GithubSerializer
from .services.github_service import extract_username, fetch_repos
from ai_engine.services.openai_service import generate_insights

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
            username = extract_username(github_url=github_url)
            repositories = fetch_repos(username=username)
            return Response({
                "username" : username,
                "repositories" : repositories
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GithubProfileAnalyzeView(APIView):
    def post(self,request):
        serializer = GithubSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        github_url = serializer.validated_data['github_url']
        username = extract_username(github_url=github_url)
        repositories = fetch_repos(username=username)

        llm_payload = {
            'username' : username,
            "repositories" : repositories
        } 
        insights = generate_insights(llm_payload)
        return Response(insights)
