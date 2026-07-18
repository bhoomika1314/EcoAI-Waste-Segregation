from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({
            "error": "Please select an image"
        }), 400

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(image_path)

    # Temporary prediction for testing
    prediction = "Plastic"

    return jsonify({
        "prediction": prediction,
        "message": "Waste identified successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)
