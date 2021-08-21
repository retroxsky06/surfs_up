# import dependencies
from flask import Flask

# Set up Flask
# Create first route
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'


