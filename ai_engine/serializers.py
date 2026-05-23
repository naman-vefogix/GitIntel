from rest_framework import serializers

class RepositorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(allow_null = True, required = False)
    language = serializers.CharField(allow_null = True, required = False)
    stargazers_count = serializers.IntegerField()
    topics = serializers.ListField(child = serializers.CharField(), required = False)


class LLMInsightRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    repositories = RepositorySerializer(many = True)