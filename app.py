from flask import Flask, render_template, request, jsonify
from model import predict_news

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']

    result, prob = predict_news(text)

    return jsonify({
        "prediction": "Real" if result == 1 else "Fake",
        "score": round(prob * 100, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
