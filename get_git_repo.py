import requests
import json


url = "https://api.github.com/user/repos"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",
}
params = {
    "visibility": "all"
}

repositories = requests.get(url, headers=headers, params=params)

print("retrieved data from user" if repositories.status_code == 200 else "retrieval unsuccessful. status code {}".format(repositories.status_code))

if repositories.status_code == 200:
    for repo in repositories.json():
        print(repo.keys(), end='\n\n')
