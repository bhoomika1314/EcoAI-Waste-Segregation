from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EcoAI Smart Waste Segregation API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    # Temporary prediction for testing
    # AI model will be connected here later
    filename = image.filename.lower()

    if "plastic" in filename or "bottle" in filename:
        waste_type = "Plastic"
        message = "Plastic waste → Put it in the Recyclable Waste Bin."
    elif "paper" in filename:
        waste_type = "Paper"
        message = "Paper waste → Put it in the Recyclable Waste Bin."
    elif "glass" in filename:
        waste_type = "Glass"
        message = "Glass waste → Put it in the Recyclable Waste Bin."
    elif "metal" in filename or "can" in filename:
        waste_type = "Metal"
        message = "Metal waste → Put it in the Recyclable Waste Bin."
    elif "organic" in filename or "food" in filename:
        waste_type = "Organic"
        message = "Organic waste → Put it in the Compost/Wet Waste Bin."
    else:
        waste_type = "Unknown"
        message = "Unable to identify the waste."

    return jsonify({
        "waste_type": waste_type,
        "message": message
    })


if __name__ == "__main__":
    app.run(debug=True)
