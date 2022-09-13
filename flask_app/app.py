from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name":"My Wonderful Store",
        "items":[
            {
                "name": "My Item", 
                "price": 15.99, 
            },
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET - used to get data back only
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over store 
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({"message": "Invalid store name"})




@app.route('/store')
def get_stores():
    return jsonify({"stores":stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price'], 
            }
            store["items"].append(new_item)
            return jsonify(store)
        return jsonify({"message": "Invalid store name"})

@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items":store['items']})
    return jsonify({"error": "Invalid store name"})



if __name__ == '__main__':
    app.run(port=5000) 