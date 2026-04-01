print("App is starting...")
import os
import requests
from flask import Flask, render_template, request, jsonify
from model import predict_news

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
# from model import predict_news

    sources = []

    if result == 1:
        try:
            api_key = os.getenv("NEWS_API_KEY")

            url = f"https://newsapi.org/v2/everything?q={text[:50]}&apiKey={api_key}"
            response = requests.get(url).json()

            for article in response.get("articles", [])[:3]:
                sources.append(article["url"])
        except:
            sources = []

    return jsonify({
        "prediction": "Real" if result == 1 else "Fake",
        "score": round(prob * 100, 2),
        "sources": sources
    })
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)