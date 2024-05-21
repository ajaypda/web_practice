**Today's class we learn the virtual environment in python.
Each virtual environment has its own Python binary, independent package installation directories, and can have different sets of installed packages without interfering with each other or with the system-wide Python installation.**

## Creating a Virtual Environment:
`python -m venv <venv_name_or_porject_name>`

## Activating the Virtual Environment:
`myenv\Scripts\activate`

## Installing requiredpackages:
`pip install <package_name>`

## Deactivating the Virtual Environment:
`myenv\Scripts\deactivate`


## PIP commands:
pip install <package_name>
pip uninstall <package_name>


## requests:

requests is used to send http request to given host enclosed into the url.

```
from requests import get
HTTP_STATUS_OK = 200

url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
word ="happy"

# Send a GET request
response = get(url + word)

if response.status_code == HTTP_STATUS_OK:
    # Print the response content
    print(response.text)
else:
    print("Error:", response.status_code)
```

## static variable:

```
DA00046:class6 ajayp$ cat test.py

class Test:
    COUNT = 0

    def __init__(self, name, age):
        self.name=name
        self.age=age

DA00046:class6 ajayp$ python3
Python 3.10.8 (main, Oct 13 2022, 10:17:43) [Clang 14.0.0 (clang-1400.0.29.102)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from test import Test
>>> t = Test("Rahul", 42)
>>> t.__dict__
{'name': 'Rahul', 'age': 42}
>>> t.COUNT
0
>>> t.__dict__
{'name': 'Rahul', 'age': 42}
>>> t.COUNT = 5
>>> t.__dict__
{'name': 'Rahul', 'age': 42, 'COUNT': 5}
>>> t.COUNT
5
>>> Test.COUNT
0
>>>
```