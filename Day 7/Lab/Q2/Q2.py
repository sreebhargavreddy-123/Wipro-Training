from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
items = [
    {"id": 1, "name": "Pen", "price": 10}
]

# Helper function to find item by id
def find_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None


# -----------------------------
# GET all items
# -----------------------------
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": items}), 200


# -----------------------------
# GET item by ID
# -----------------------------
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


# -----------------------------
# POST create new item
# -----------------------------
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = items[-1]["id"] + 1 if items else 1
    new_item = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"]
    }

    items.append(new_item)
    return jsonify({
        "message": "Item created successfully",
        "item": new_item
    }), 201


# -----------------------------
# PUT update item
# -----------------------------
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["price"] = data.get("price", item["price"])

    return jsonify({"message": "Item updated successfully"}), 200


# -----------------------------
# DELETE item
# -----------------------------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200


# -----------------------------
# Run the application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
