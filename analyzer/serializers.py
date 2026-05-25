from rest_framework import serializers

class GithubSerializer(serializers.Serializer):
    github_url = serializers.URLField()
