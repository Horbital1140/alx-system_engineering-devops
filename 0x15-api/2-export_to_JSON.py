#!/usr/bin/python3
"""Returns the to-do list information for a given employee ID."""
import requests
import sys
import csv
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    api_response = requests.get(url + "users/{}".format(user_id)).json()
    username = api_response.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
