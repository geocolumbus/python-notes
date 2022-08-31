# https://docs.python-requests.org/en/latest/

import requests
from pprint import pprint
import inspect
import json
from utility import printDir

result = """
####################################################################################################

------ GET ------
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
200 OK

https://jsonplaceholder.typicode.com/posts/1

{'body': 'quia et suscipit\n'
         'suscipit recusandae consequuntur expedita et cum\n'
         'reprehenderit molestiae ut ut quas totam\n'
         'nostrum rerum est autem sunt rem eveniet architecto',
 'id': 1,
 'title': 'sunt aut facere repellat provident occaecati excepturi optio '
          'reprehenderit',
 'userId': 1}

------ POST ------
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=json.dumps(my_data), 
headers=my_headers, )
my_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
201 Created
response.url = https://jsonplaceholder.typicode.com/posts
"response.json() = {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}"

# Requests functions
ConnectTimeout                ConnectionError               DependencyWarning
FileModeWarning               HTTPError                     JSONDecodeError
NullHandler                   PreparedRequest               ReadTimeout
Request                       RequestException              RequestsDependencyWarning
Response                      Session                       Timeout
TooManyRedirects              URLRequired                   adapters
api                           auth                          certs
chardet_version               charset_normalizer_version    check_compatibility
codes                         compat                        cookies
delete                        exceptions                    get
head                          hooks                         logging
models                        options                       packages
patch                         post                          put
request                       session                       sessions
ssl                           status_codes                  structures
urllib3                       utils                         warnings
####################################################################################################
"""


def example():
    # GET - read resource
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("\n------ GET ------")
    print('response = requests.get("https://jsonplaceholder.typicode.com/posts/1")')
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
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=json.dumps(my_data),
                             headers=my_headers, )
    print("\n------ POST ------")
    print('response = requests.post("https://jsonplaceholder.typicode.com/posts", '
          'data=json.dumps(my_data), headers=my_headers, )')
    print(f"my_data = {my_data}")
    print(f"{response.status_code} {response.reason}")
    print(f"response.url = {response.url}")
    pprint(f"response.json() = {response.json()}")

    print("\n# Requests functions")
    printDir(requests)


example()
