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

class LLMInsightResponseSerializer(serializers.Serializer):
    developer_type = serializers.CharField()
    experience_signal = serializers.CharField()
    summary = serializers.CharField()
    strengths = serializers.ListField(child = serializers.CharField())
    weaknesses = serializers.ListField(child = serializers.CharField())
    highlights_of_profile = serializers.CharField()
    recommendation = serializers.CharField()
    confidence = serializers.ChoiceField(choices = ['low', 'medium', 'high'])

class MetricsSerializer(serializers.Serializer):
    repo_count = serializers.IntegerField()
    forked_repo_count = serializers.IntegerField()
    original_repo_count = serializers.IntegerField()
    total_stars = serializers.IntegerField()
    top_languages = serializers.DictField(
        child = serializers.IntegerField()
    )

class ScoreResponseSerializer(serializers.Serializer):
    score = serializers.IntegerField()

class LLMInsightScoreRequestSerializer(serializers.Serializer):
    metrics = MetricsSerializer()
    repositories = RepositorySerializer(many = True)