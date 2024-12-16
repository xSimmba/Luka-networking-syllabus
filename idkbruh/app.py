from flask import Flask, Blueprint, jsonify, request 

app = Flask(__name__)




bp = Blueprint('items', __name__)

# In-memory database (just for example purposes)
items = []

# GET endpoint to retrieve all items
@bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# POST endpoint to create a new item
@bp.route('/items', methods=['POST'])
def create_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

# PUT endpoint to update an existing item by ID
@bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(request.json)
        return jsonify(item), 200
    return '', 404

# DELETE endpoint to remove an item by ID
@bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return '', 204




@app.route('/')
def hello_world():
    return 'Hello from container!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


    