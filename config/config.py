import os

class TestConfig:
    base_url = os.environ.get('BASE_URL') #http://dbankdemo.com/bank/login
    username = os.environ.get('USERNAME') #jsmith@demo.io
    password = os.environ.get('PASSWORD') #Demo123!
    