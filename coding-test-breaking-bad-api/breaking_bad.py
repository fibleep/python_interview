import requests

BREAKING_BAD_URL: str = 'https://www.breakingbadapi.com/api'


def call(query) -> list:
    """
    Using the Breaking Bad API, searches for character appearances in episodes of Breaking Bad
    :param query: (str / str[]) Character name(s) to look for in the episodes
    :return:(list): All episodes in which the character(s) appear
    """
    if not query: return []
    if not isinstance(query, list): query: list = [query]
    try:
        api_response: dict = requests.get(BREAKING_BAD_URL + "/episodes/?category=Breaking+Bad").json()
    except ConnectionError as ce:
        return []

    appearances: list = []
    for episode in api_response:
        if all(character in episode["characters"] for character in query):
            season_number: str = f'0{str(episode["season"]).lstrip()}'
            episode_number: str = f'0{str(episode["episode"])}'
            title: str = episode["title"]
            appearances.append(f'S{season_number}{episode_number[len(episode_number) - 2::]} - {title}')
    return appearances
