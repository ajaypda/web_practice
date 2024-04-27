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