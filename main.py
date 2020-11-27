from flask import Flask

from constants import VERSION

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'MY APP Version {}'.format(VERSION)

if __name__ == "__main__":
    app.run(port=5000)
