from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "This is a Dashboard...."

if __name__ == '__main__':
    app.run(debug=True)
