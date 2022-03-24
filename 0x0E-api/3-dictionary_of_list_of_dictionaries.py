#!/usr/bin/python3
"""
This method exports the todo list for all users to
a json file.
"""
import json
import requests


if __name__ == '__main__':
    # assign values to variables #
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    to_dos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    # export information to the json file #
    with open("todo_all_employees.json", 'w') as file:
        todo_dict = {employee.get('id'): [{
                'task': task.get('title'),
                'username': employee.get('username'),
                'completed': task.get('completed')
            } for task in to_dos if employee.get('id') == task.get('userId')
            ] for employee in users}
        json.dump(todo_dict, file)
