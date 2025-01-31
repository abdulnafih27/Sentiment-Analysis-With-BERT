from flask import Flask, request, render_template
from transformers import BertForSequenceClassification, BertTokenizer
import torch
import gdown
gdown.download_folder("https://drive.google.com/drive/folders/1-1dLepbjgcLbCyUanFNU711ca9pCojbW?usp=sharing", output="bert_sentimental_model", quiet=False)

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and tokenizer
model_path = './bert_sentiment_model'  # Replace with your model path
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained(model_path)

# Define a function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    return "Positive" if prediction == 1 else "Negative"

# Home route (web page)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        sentiment = predict_sentiment(text)
        return render_template("index.html", sentiment=sentiment, text=text)
    return render_template("index.html", sentiment=None)

if __name__ == "__main__":
    app.run(debug=True)
