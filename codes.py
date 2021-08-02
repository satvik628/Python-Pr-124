from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Rohan',
        'Contact': u'1234567890', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Varun',
        'Contact': u'1234567891', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Welcome to my flask app !Enter '/get-data' to url for navigating to data screen ."

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!ERROR ocuur not found ."
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name :--'],
        'Contact': request.json.get('Contact :--', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully to flask app!  : )"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run()
