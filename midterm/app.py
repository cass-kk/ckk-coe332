import json
import random
import uuid, datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
    return "Hello World!!\n"

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
def snake():
    snake = [x for x in jsonList if x['head'] == 'snake']
    return json.dumps(snake)

# Additional Routes

@app.route('/animals/created on', methods=['GET'])
def daterange():
    start = request.args.get('start_time')
    sdate = datetime.datetime.strptime(start, "%Y-%m-%d_%H:%M:%S.%f")
    end = request.arges.get('end_time')
    edate = datetime.datetime.strptime(end, "%Y-%m-%d_%H:%M:%S.%f")

    s = datetime.datetime.strptime(x['created_on'], "%Y-%m-%d_%H:%M:%S.%f")
    e = datetime.datetime.strptime(x['created_on'], "%Y-%m-%d_%H:%M:%S.%f")
    dates = [x for x in test if(s>=sdate and e<=edate)]
    return json.dumps(dates)

@app.route('/animals/uid/<u_id>', methods=['GET'])
def uids(u_id):
    unique = [x for x in jsonList if x['uid'] == u_id]
    return json.dumps(unique)

@app.route('/edit/<u_id>', methods=['GET'])
def edits(u_id):
    ani = [x for x in jsonList if x['uid'] == u_id]
    d = dict(ani)
    t = d['tails']
    if t >= 15:
        d['tails'] == 10
    elif t < 15:
        d['tails'] == 20;
    animal = list(d)
    return json.dumps(animal)

@app.route('/created on/delete', methods=['GET'])
def delrange():

    start = request.args.get('start_time')
    sdate = datetime.datetime.strptime(start, "%Y-%m-%d_%H:%M:%S.%f")
    end = request.arges.get('end_time')
    edate = datetime.datetime.strptime(end, "%Y-%m-%d_%H:%M:%S.%f")
    s = datetime.datetime.strptime(x['created_on'], "%Y-%m-%d_%H:%M:%S.%f")
    e = datetime.datetime.strptime(x['created_on'], "%Y-%m-%d_%H:%M:%S.%f")
    dates = [x for x in test if(s>=sdate and e<=edate)]

    animals.remove(dates[0])
    return json.dumps(jsonList)

@app.route('/animals/average_legs', methods=['GET'])
def avglegs():
    six = [x for x in jsonList if x['legs'] == 6]
    num_legs = 0
    count = 0
    for x in jsonList:
        num_legs = num_legs + x['legs']
        count = count + 1
    avg_legs = num_legs/count
    return str(avg_legs)

@app.route('/totalcount', methods=['GET'])
def total():
    count = 0
    for x in jsonList:
        count = count + 1
    return str(count)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
