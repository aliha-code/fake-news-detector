import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("Loading dataset...")

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

X = data["text"]
y = data["label"]

print("Training model...")

vectorizer = TfidfVectorizer(
    stop_words='english',
    max_df=0.7,
    ngram_range=(1, 2),
    max_features=5000
)
X = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved!")