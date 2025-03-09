from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

app = Flask(__name__)
@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, 'text' is required"}), 400
    text = data['text']
    sentiment = analyzer.polarity_scores(text)
    x = sentiment['compound']
    if x <= -0.05:
        return jsonify({"sentiment": "negative"}), 200
    if x >= 0.05:
        return jsonify({"sentiment": "positive"}), 200
 
    return jsonify({"sentiment": "neutral"}), 200

if __name__ == '__main__':
    app.run(debug=True)
