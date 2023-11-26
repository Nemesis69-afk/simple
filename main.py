from dotenv.main import load_dotenv
import os

load_dotenv()

favorite_language = os.environ['LANGUAGE']

print("My favorite programming language is: " + favorite_language)
# Prints My favorite programming language is: Python
