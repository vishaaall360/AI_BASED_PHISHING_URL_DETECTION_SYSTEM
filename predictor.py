import joblib
from feature_extractor import extract_features

model = joblib.load("model/phishing_model.pkl")

def predict_url(url):
    features = extract_features(url)
    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0]) * 100
    return prediction, round(confidence, 2)
