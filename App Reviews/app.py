from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'I like spaghetti'

@app.route('/beans', methods=['GET', 'POST'])
def beans():
    if request.method == 'GET':
        return 'BUY BEANS'
    else:
        return 'SELL BEANS'