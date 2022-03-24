#!/usr/bin/python3
"""
This method takes an employee id number and returns the
number of tasks done compared to the total number of tasks,
and lists the titles of the tasks completed. Then it saves the
task information for that user into a .csv file.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    # check for valid input, argument passed must be type int #
    if sys.argv[1].isdigit():

        # assign values to variables #
        user_id = sys.argv[1]
        employee = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(user_id)).json()
        to_do = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(user_id)).json()
        completed = []
        for done in to_do:
            if done.get("completed") is True:
                completed.append(done.get("title"))

        # print requested outputs #
        print("Employee {} is done with tasks({}/{}):".format(
            employee.get("name"), len(completed), len(to_do)))
        for title in completed:
            print("\t {}".format(title))

        # print requested values to CSV format file #
        with open("{}.csv".format(user_id), 'w') as file:
            csv_write = csv.writer(file, quoting=csv.QUOTE_ALL)
            for item in to_do:
                csv_write.writerow([
                    user_id, employee.get("username"),
                    item.get("completed"), item.get("title")])
