#!/usr/bin/python3
"""Returns the to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    api_response = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    employee_completed_task = [t.get("title")
                               for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        api_response.get("name"), len(employee_completed_task), len(todos)))

    [print("\t {}".format(c)) for c in employee_completed_task]
