from flask import Blueprint, request, jsonify

restaurant_bp = Blueprint("restaurant_bp", __name__)

# -------------------------
# In-Memory Storage
# -------------------------

restaurants = []
restaurant_counter = 1

dishes = []
dish_counter = 1

feedback_list = []
feedback_counter = 1

orders = []
order_counter = 1


users = []
user_counter = 1


ratings = []
rating_counter = 1


# -------------------------
# 1️⃣ Register Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    global restaurant_counter

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Restaurant name required"}), 400

    for r in restaurants:
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant already exists"}), 409

    restaurant = {
        "id": restaurant_counter,
        "name": data["name"],
        "category": data.get("category"),
        "location": data.get("location"),
        "rating": data.get("rating", 0),
        "contact": data["contact"],
        "images": data["images"],
        "active": True,
        "approved": False
    }

    restaurants.append(restaurant)
    restaurant_counter += 1

    return jsonify(restaurant), 201


# -------------------------
# 2️⃣ View Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify(restaurant), 200


# -------------------------
# 3️⃣ Update Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    data = request.get_json()

    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant.update(data)

    return jsonify(restaurant), 200


# -------------------------
# 4️⃣ Disable Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["active"] = False

    return jsonify({"message": "Restaurant disabled"}), 200


# -------------------------
# 5️⃣ Add Dish
# -------------------------
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    global dish_counter

    data = request.get_json()

    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    required_fields = ["name", "type", "price", "available_time", "image"]

    if not data:
        return jsonify({"error": "Request body required"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    dish = {
        "id": dish_counter,
        "restaurant_id": restaurant_id,
        "name": data["name"],
        "type": data["type"],
        "price": data["price"],
        "available_time": data["available_time"],
        "image": data["image"],
        "enabled": True
    }

    dishes.append(dish)
    dish_counter += 1

    return jsonify(dish), 201


# -------------------------
# 6️⃣ Update Dish
# -------------------------
@restaurant_bp.route("/api/v1/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    data = request.get_json()

    dish = next((d for d in dishes if d["id"] == dish_id), None)

    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    dish.update(data)

    return jsonify(dish), 200


# -------------------------
# 7️⃣ Enable / Disable Dish
# -------------------------
@restaurant_bp.route("/api/v1/dishes/<int:dish_id>/status", methods=["PUT"])
def update_dish_status(dish_id):
    data = request.get_json()

    if not data or "enabled" not in data:
        return jsonify({"error": "enabled field required"}), 400

    dish = next((d for d in dishes if d["id"] == dish_id), None)

    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    dish["enabled"] = data["enabled"]

    return jsonify({
        "message": "Dish status updated",
        "dish_id": dish_id,
        "enabled": dish["enabled"]
    }), 200


# -------------------------
# 8️⃣ Delete Dish
# -------------------------
@restaurant_bp.route("/api/v1/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    global dishes

    dish = next((d for d in dishes if d["id"] == dish_id), None)

    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    dishes = [d for d in dishes if d["id"] != dish_id]

    return jsonify({"message": "Dish deleted"}), 200


# -------------------------
# 9️⃣ Admin Approve Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["approved"] = True

    return jsonify({
        "message": "Restaurant approved",
        "restaurant_id": restaurant_id
    }), 200


# -------------------------
# 🔟 Admin Disable Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/admin/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def admin_disable_restaurant(restaurant_id):
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["active"] = False

    return jsonify({
        "message": "Restaurant disabled by admin",
        "restaurant_id": restaurant_id
    }), 200


# -------------------------
# 1️⃣1️⃣ Admin View Feedback
# -------------------------
@restaurant_bp.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(feedback_list), 200


# -------------------------
# 1️⃣2️⃣ Admin View Order Status
# -------------------------
@restaurant_bp.route("/api/v1/admin/orders", methods=["GET"])
def view_orders():
    return jsonify(orders), 200


# -------------------------
# 1️⃣3️⃣ User Registration
# -------------------------
@restaurant_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    global user_counter

    data = request.get_json()

    required_fields = ["name", "email", "password"]

    if not data:
        return jsonify({"error": "Request body required"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Check duplicate email
    for user in users:
        if user["email"] == data["email"]:
            return jsonify({"error": "Email already registered"}), 409

    user = {
        "id": user_counter,
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]  # ⚠ plain text (only for demo)
    }

    users.append(user)
    user_counter += 1

    return jsonify(user), 201


# -------------------------
# 🔎 Search Restaurants
# -------------------------
@restaurant_bp.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():

    name = request.args.get("name")
    location = request.args.get("location")
    dish_name = request.args.get("dish")
    rating = request.args.get("rating")

    # Only approved & active restaurants
    results = [
        r for r in restaurants
        if r.get("approved") is True and r.get("active") is True
    ]

    # Filter by name
    if name:
        results = [
            r for r in results
            if r.get("name") and name.lower() in r["name"].lower()
        ]

    # Filter by location
    if location:
        results = [
            r for r in results
            if r.get("location") and location.lower() in r["location"].lower()
        ]

    # Filter by rating
    if rating:
        try:
            rating_value = float(rating)
            results = [
                r for r in results
                if float(r.get("rating", 0)) >= rating_value
            ]
        except ValueError:
            return jsonify({"error": "Invalid rating value"}), 400

    # Filter by dish
    if dish_name:
        filtered = []

        for r in results:
            for d in dishes:
                if (
                    d["restaurant_id"] == r["id"]
                    and d.get("enabled") is True
                    and dish_name.lower() in d["name"].lower()
                ):
                    filtered.append(r)
                    break

        results = filtered

    return jsonify(results), 200


# -------------------------
# 1️⃣4️⃣ Place Order
# -------------------------
@restaurant_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    global order_counter

    data = request.get_json()

    # ✅ Validate request body
    if not data:
        return jsonify({"error": "Request body required"}), 400

    required_fields = ["user_id", "restaurant_id", "dishes"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    user_id = data["user_id"]
    restaurant_id = data["restaurant_id"]
    dish_ids = data["dishes"]

    # ✅ Validate user exists
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 400

    # ✅ Validate restaurant exists
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 400

    # ✅ Check restaurant active & approved
    if not restaurant["active"] or not restaurant["approved"]:
        return jsonify({"error": "Restaurant not available"}), 400

    # ✅ Validate dishes
    order_dishes = []
    total_amount = 0

    for dish_id in dish_ids:
        dish = next(
            (d for d in dishes
             if d["id"] == dish_id
             and d["restaurant_id"] == restaurant_id
             and d["enabled"] is True),
            None
        )

        if not dish:
            return jsonify({"error": f"Dish {dish_id} not available"}), 400

        order_dishes.append({
            "id": dish["id"],
            "name": dish["name"],
            "price": dish["price"]
        })

        total_amount += dish["price"]

    # ✅ Create Order
    order = {
        "id": order_counter,
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "dishes": order_dishes,
        "total_amount": total_amount,
        "status": "Placed"
    }

    orders.append(order)
    order_counter += 1

    return jsonify(order), 201


# -------------------------
# 1️⃣4️⃣ Give Rating
# -------------------------
@restaurant_bp.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    global rating_counter

    data = request.get_json()

    required_fields = ["order_id", "rating", "comment"]

    if not data:
        return jsonify({"error": "Request body required"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Validate rating value
    try:
        rating_value = float(data["rating"])
        if rating_value < 1 or rating_value > 5:
            return jsonify({"error": "Rating must be between 1 and 5"}), 400
    except ValueError:
        return jsonify({"error": "Invalid rating value"}), 400

    # Check if order exists
    order = next((o for o in orders if o["id"] == data["order_id"]), None)

    if not order:
        return jsonify({"error": "Order not found"}), 400

    rating_obj = {
        "id": rating_counter,
        "order_id": data["order_id"],
        "restaurant_id": order["restaurant_id"],
        "rating": rating_value,
        "comment": data["comment"]
    }

    ratings.append(rating_obj)
    rating_counter += 1

    # 🔥 Update restaurant average rating
    restaurant = next(
        (r for r in restaurants if r["id"] == order["restaurant_id"]),
        None
    )

    if restaurant:
        restaurant_ratings = [
            r["rating"] for r in ratings
            if r["restaurant_id"] == restaurant["id"]
        ]
        restaurant["rating"] = round(
            sum(restaurant_ratings) / len(restaurant_ratings), 2
        )

    return jsonify(rating_obj), 201


# -------------------------
#  View Orders by Restaurant
# -------------------------
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>/orders", methods=["GET"])
def view_orders_by_restaurant(restaurant_id):

    # Check restaurant exists
    restaurant = next((r for r in restaurants if r["id"] == restaurant_id), None)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    # Filter orders by restaurant_id
    restaurant_orders = [
        order for order in orders
        if order["restaurant_id"] == restaurant_id
    ]

    return jsonify(restaurant_orders), 200

# -------------------------
# View Orders by User
# -------------------------
@restaurant_bp.route("/api/v1/users/<int:user_id>/orders", methods=["GET"])
def view_orders_by_user(user_id):

    # Check user exists
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Get orders for this user
    user_orders = [
        order for order in orders
        if order["user_id"] == user_id
    ]

    return jsonify(user_orders), 200