from flask import Flask

# New flask instance
app = Flask(__name__)

# Define starting point
@app.route('/')
def hello_world():
    return 'Hello world'
