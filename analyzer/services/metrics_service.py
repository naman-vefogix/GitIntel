from collections import Counter
 
def calculate_metrics(repositories):

    metrics = {}

    metrics['repo_count'] = len(repositories)

    metrics['forked_repo_count'] = sum(
        1 for repo in repositories
        if repo.get('fork')
    )

    metrics['original_repo_count'] = (
        metrics['repo_count']
        - metrics['forked_repo_count']
    )

    metrics['total_stars'] = sum(
        repo.get('stargazers_count', 0)
        for repo in repositories
    )

    language_counter = Counter()

    for repo in repositories:

        language = repo.get('language')

        if language:
            language_counter[language] += 1

    metrics['top_languages'] = (
        dict(language_counter)
    )

    return metrics