from flask import Flask

app = Flask(__name__)
@app.route('/hello')
def hello_world():
    return 'hello test'
@app.route('/')
def hello_b():
    return 'fadad'
if __name__ == '__main__':
    app.run()