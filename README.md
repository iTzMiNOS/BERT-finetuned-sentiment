# BERT Fine-Tuned Sentiment Analysis Model for Tweets

This repository contains a fine-tuned BERT (uncased) model for sentiment analysis, specifically trained on a dataset of 30,000 tweets. The model is capable of predicting one of six sentiments: **joy**, **anger**, **surprise**, **sadness**, **love**, and **fear**.

## Model Overview

The model is based on the BERT architecture (uncased) and was fine-tuned on a dataset of 30,000 labeled tweets. Each tweet is classified into one of the following sentiment categories:

- **Joy**
- **Anger**
- **Surprise**
- **Sadness**
- **Love**
- **Fear**

## Try It Out

You can try the fine-tuned model in an interactive environment using Streamlit. It is hosted on Hugging Face and can be accessed via the following link:

[**BERT Fine-Tuned Sentiment Analysis for Tweets**](https://bert-finetuned-sentiment-tweets.streamlit.app/)

## Installation

To run the model locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bert-finetuned-sentiment-tweets.git
    cd bert-finetuned-sentiment-tweets
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

The app will launch in your browser, allowing you to interact with the model.

## Usage

Once you have the app running, you can input a tweet into the provided text box, and the model will classify the sentiment of the tweet into one of the six categories mentioned earlier.

## Model Details

- **Model Architecture:** BERT (uncased)
- **Fine-Tuning Dataset:** 30,000 labeled tweets with sentiments: joy, anger, surprise, sadness, love, and fear.
- **Hugging Face Model Hub:** [Link to your model on Hugging Face]

## Requirements

- Python 3.x
- Streamlit
- Transformers
- PyTorch or TensorFlow (depending on the framework used for fine-tuning)

## Credits

- **Hugging Face** for providing the BERT model and hosting platform.
- **Streamlit** for providing an easy-to-use interface for deploying machine learning models.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
