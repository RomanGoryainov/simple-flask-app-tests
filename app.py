# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/howareyou')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(debug = False, host="0.0.0.0", port=8080)