from dotenv import load_dotenv
import os

load_dotenv()

class TestConfig:
    base_url = os.environ.get('BASE_URL')
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    #base_url = "http://dbankdemo.com/bank/login"
    #username = "jsmith@demo.io"
    #password = "Demo123!"