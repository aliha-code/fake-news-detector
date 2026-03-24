import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_news(text):
    vec = vectorizer.transform([text])
    result = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]
    return result, prob