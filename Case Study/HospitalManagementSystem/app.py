from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory patient storage
patients = []

# -------------------------------------------------
# Route 1: Open Patient Registration Web Page
# -------------------------------------------------
@app.route("/register")
def register_page():
    return render_template("register.html")


# -------------------------------------------------
# Route 2: Create Patient (from Web Form OR API)
# -------------------------------------------------
@app.route("/api/patients", methods=["POST"])
def add_patient():
    # If request is from HTML form
    if request.form:
        data = request.form
    else:
        # If request is from API (JSON)
        data = request.json

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    patient = {
        "id": len(patients) + 1,
        "name": data.get("name"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "contact": data.get("contact"),
        "disease": data.get("disease"),
        "doctor": data.get("doctor")
    }

    patients.append(patient)
    return jsonify(patient), 201


# -------------------------------------------------
# Route 3: Get All Patients
# -------------------------------------------------
@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200


# -------------------------------------------------
# Route 4: Get Patient By ID
# -------------------------------------------------
@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    for patient in patients:
        if patient["id"] == pid:
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404


# -------------------------------------------------
# Route 5: Update Patient By ID
# -------------------------------------------------
@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    data = request.json

    for patient in patients:
        if patient["id"] == pid:
            patient.update(data)
            return jsonify(patient), 200

    return jsonify({"error": "Patient not found"}), 404


# -------------------------------------------------
# Main
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
