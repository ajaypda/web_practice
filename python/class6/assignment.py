# Create 3 examples of classes without static variables
# Create 3 more examples of classes with static variables

class Logger:
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    TOTAL_INSTANCE_CREATED=0

    def __init__(self, level, name):
        self.log_level = level
        self.log_name= name
        Logger.TOTAL_INSTANCE_CREATED += 1

# Using logger
logger = Logger(Logger.ERROR, "looger1")
Logger(Logger.DEBUG, "looger2")
print("log level:",logger.log_level)
print("logger name:",logger.log_name)
print("total log instances : ", logger.TOTAL_INSTANCE_CREATED)


class NetworkConfig:
    SERVER_ADDRESS = "127.0.0.1"
    DEFAULT_PORT = 65500
    DEFAULT_TIMEOUT = 30

    def __init__(self, port=None, timeout=None):
        self.port = port if port is not None else NetworkConfig.DEFAULT_PORT
        self.timeout = timeout if timeout is not None else NetworkConfig.DEFAULT_TIMEOUT

nconf =NetworkConfig()
print("Server address:", nconf.SERVER_ADDRESS)
print("Port:", nconf.port)
print("timeout:", nconf.timeout)


nconf1 =NetworkConfig(22, 15)
print("Server address:", nconf1.SERVER_ADDRESS)
print("Port:", nconf1.port)
print("timeout:", nconf1.timeout)

# requests practice

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
