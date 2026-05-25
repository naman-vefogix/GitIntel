import requests
from rest_framework import status
from rest_framework.response import Response

def extract_username(github_url):
    return github_url.rstrip('/').split('/')[-1]

def fetch_repos(username):
    api_url = f'https://api.github.com/users/{username}/repos'
    response  = requests.get(api_url)
    if response.status_code != 200:
        return None
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
    return repositories