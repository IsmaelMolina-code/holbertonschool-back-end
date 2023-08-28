#!/usr/bin/python3
"""Task 0 - Gather data from an API"""
import requests
import json
from sys import argv

if __name__ == '__main__':

    if len(argv) != 2:
        exit()

    users_request = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    users = json.loads(users_request.text)
    all_users_id = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    all_users_id = json.loads(all_users_id.text)

    tasks_completed = 0
    tasks_not_completed = 0

    for task in all_users_id:
        if task['completed'] is True:
            tasks_completed += 1
        else:
            tasks_not_completed += 1

    print(f"Employee {users['name']} is done with tasks"
          f"({tasks_completed}/{len(all_users_id)}):")

    for task in all_users_id:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
