# Sentiment Analysis using BERT

This project implements a sentiment analysis model using BERT (Bidirectional Encoder Representations from Transformers) and serves it via a Flask web application. The model is trained on the IMDb dataset to classify movie reviews as positive or negative.

## Features
- Uses a pre-trained BERT model for sentiment classification.
- Fine-tuned on the IMDb dataset.
- Flask-based web interface for user interaction.
- API endpoint for sentiment prediction.

## Dataset
The project uses the IMDb dataset, which consists of 50,000 movie reviews labeled as positive (1) or negative (0).

## Installation
### Prerequisites
Ensure you have Python 3.7 or later installed.

### Clone the Repository
```bash
git clone https://github.com/abdulnafih27/Sentimental-Analysis-With-BERT.git
cd Sentimental-Analysis-With-BERT
```

### Install Dependencies
```bash
pip install flask torch transformers gdown
```

## Download the Model from Google Drive
The trained model is stored in Google Drive. Download it by running the following Python script:

```bash
python download_model.py
```

This will download the model files into the `bert_sentiment_model` folder in your project.

## Usage
### Run the Flask App
```bash
python app.py
```

### Access the Web Interface
Once the server is running, open your browser and go to:
```
http://127.0.0.1:5000
```

### API Endpoint
The API also provides a sentiment analysis endpoint:
#### Endpoint: `/predict`
- **Method:** POST
- **Request:** JSON `{ "text": "This movie was amazing!" }`
- **Response:** JSON `{ "sentiment": "positive" }`

## Project Structure
```
├── app.py                      # Flask application
├── download_model.py           # Script to download model from Google Drive
├── bert_sentiment_model/       # Folder containing trained model files (downloaded from Google Drive)
├── templates/                  # HTML templates
├── README.md                   # Project documentation
```

## Future Improvements
- Deploy using Docker and cloud services.
- Improve UI/UX with better frontend design.
- Add support for multiple languages.

## License
This project is licensed under the MIT License.
```

This updated `README.md` now reflects the change to use `download_model.py` for downloading the model files. Let me know if you need any further changes!