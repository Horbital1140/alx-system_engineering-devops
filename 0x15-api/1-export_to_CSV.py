#!/usr/bin/python3
"""Returns the to-do list information for a given employee ID."""
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    api_response = requests.get(url + "users/{}".format(user_id)).json()
    username = api_response.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
            