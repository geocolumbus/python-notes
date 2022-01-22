# https://docs.python-requests.org/en/latest/

import requests
from pprint import pprint
import inspect
import json


def example():
    # GET - read resource
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("\n------ GET ------\n")
    print(f"{response.status_code} {response.reason}\n")
    print(f"{response.url}\n")
    pprint(response.json())

    #   print("\n-------------------------\n")
    #   pprint(vars(response))
    #   print("\n-------------------------\n")
    #   pprint(dir(response))
    #   print("\n-------------------------\n")
    #   pprint(inspect.getmembers(response))

    # POST - Create resource
    my_data = {"title": "foo", "body": "bar", "userId": 1}
    my_headers = {"Content-Type": "application/json; charset=UTF-8"}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=json.dumps(my_data),
        headers=my_headers,
    )
    print("\n------ POST ------\n")
    print(f"{response.status_code} {response.reason}\n")
    print(f"{response.url}\n")
    pprint(response.json())
