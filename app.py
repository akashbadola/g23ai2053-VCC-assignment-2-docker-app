from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello! Welcome to the Web Page of G23AI2053'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
