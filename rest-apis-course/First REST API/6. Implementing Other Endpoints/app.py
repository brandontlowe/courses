from flask import Flask, jsonify

app = Flask(__name__)

# From the perspective of the server
# POST - used to receive data
# GET - used to send data back only

# Structure of the store:
stores = [
    {
        "name": "My Wonderful Store",
        "items": [{
            "name": "My item",
            "price": 15.99
        }]
    }
]
# We send data to and from the API using JSON. Flask has a built-in jsonify
# method that converts dictionaries to JSON, and front-end JavaScript
# applications can also convert JSONs into objects and vice-versa.

# POST - /store {data: name:} - create store with given name
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET - /store/<string:name> - respond with some data about store with given name
@app.route('/store/<string:name>')
def get_store(name):
    pass
# GET - /store - return list of all stores
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})
# POST - /store/<string:name>/item {name: price} - create item inside store with given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass
# GET - /store/<string:name>/item - get item inside store with given name
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass



app.run(port=5000)