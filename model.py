import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("Loading dataset...")

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = 0
true["label"] = 1

# Combine datasets
data = pd.concat([fake, true])

print("Training model...")

# Input and output
X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

# Train model
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X, y)

print("Model trained successfully!")

# Prediction function
def predict_news(text):
    vec = vectorizer.transform([text])
    result = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]
    return result, prob