import json
import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
    return "Hello World!!\n"

#@app.route('/animals', methods=['GET'])
#def get_animals():
#    return json.dumps(get_data())

def get_data():
    with open("/app/animals.json", "r") as json_file:
        data_json = json.load(json_file)
    return data_json

test = get_data()
#print(type(test))

jsonList = test['animals']
#print(type(jsonList))

@app.route('/animals', methods=['GET'])
def get_all():
    return json.dumps(jsonList)

@app.route('/animals/head/bunny', methods=['GET'])
def head_bunny():
    bun = [x for x in jsonList if x['head'] == 'bunny']
    return json.dumps(bun)

@app.route('/animals/legs/6', methods=['GET'])
def sixLegs():
    six = [x for x in jsonList if x['legs'] == 6]
    return json.dumps(six)

@app.route('/animals/head/snake', methods=['GET'])
def sixLegs():
    snake = [x for x in jsonList if x['head'] == 'snake']
    return json.dumps(snake)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
