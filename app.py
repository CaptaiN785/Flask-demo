from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    print("inside index")
    return "<h1>This is demo of flask app</h1>"


if __name__ == '__main__':
    app.run(debug=True)