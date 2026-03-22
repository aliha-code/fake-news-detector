from flask import Flask, render_template, request, jsonify
from model import predict_news

app = Flask(__name__)
def explain(text):
    text = text.lower()

    if "shocking" in text or "breaking" in text:
        return "Contains clickbait or emotional words"

    elif text.isupper():
        return "Too many capital letters (suspicious)"

    elif len(text.split()) < 20:
        return "Very short news (less reliable)"

    else:
        return "Looks like normal news content"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']

    result, prob = predict_news(text)

    return jsonify({
        "prediction": "Real" if result == 1 else "Fake",
        "score": round(prob * 100, 2),
        "reason": explain(text)
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)