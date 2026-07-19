from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EcoAI Backend is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]

    # Temporary prediction
    prediction = "Plastic"

    return jsonify({
        "prediction": prediction,
        "message": "Recycle in Plastic Bin ♻️"
    })

if __name__ == "__main__":
    app.run(debug=True)
