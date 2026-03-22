import json

def search(keyword) -> list[dict[str, str]]:
    result = []
    with open('./data/movies.json') as file:
        f = json.load(file)
        for movie in f['movies']:
            if keyword in movie['title']:
                result.append(movie)
                if len(result) == 5:
                    break

    return result