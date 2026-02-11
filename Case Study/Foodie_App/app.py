from flask import Flask
from routes.restaurant_routes import restaurant_bp

app = Flask(__name__)
app.register_blueprint(restaurant_bp)

@app.route("/")
def home():
    return {"message": "Foodie App API Running Successfully"}

if __name__ == "__main__":
    app.run(debug=True)
