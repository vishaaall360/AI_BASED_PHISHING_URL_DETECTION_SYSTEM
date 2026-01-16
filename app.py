from flask import Flask, render_template, request
from predictor import predict_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None

    if request.method == "POST":
        url = request.form["url"]
        prediction, confidence = predict_url(url)
        result = "Phishing URL 🚨" if prediction == 1 else "Legitimate URL ✅"

    return render_template("index.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
