print("App is starting...")

import os
import requests
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import predict_news

app = Flask(__name__)

# 🔥 Enable CORS (VERY IMPORTANT)
CORS(app)


# Home route
@app.route('/')
def home():
    return render_template("index.html")


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']

    # Get prediction from model
    result, prob = predict_news(text)

    sources = []

    # Fetch real news sources if prediction is REAL
    if result == 1:
        try:
            api_key = os.getenv("NEWS_API_KEY")

            url = f"https://newsapi.org/v2/everything?q={text[:50]}&apiKey={api_key}"
            response = requests.get(url).json()

            for article in response.get("articles", [])[:3]:
                sources.append(article["url"])
        except:
            sources = []

    # Return response
    return jsonify({
    "prediction": "Real" if result == 1 else "Fake",
    "sources": sources
})


# Run app (Render compatible)
if __name__ == "__main__":
    print("Starting Flask server...")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)