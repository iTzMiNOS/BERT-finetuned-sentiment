import streamlit as st
import pandas as pd
import numpy as np

from transformers import pipeline

st.title("Fine Tuned BERT")

st.subheader("Tweets Multi-Class Sentiment Analysis")

classifier = pipeline('text-classification', model='model')

text = st.text_area("Enter Tweet Here:", placeholder="Start Typing...")

if st.button("Predict"):
    result = classifier(text)
    st.markdown("## Sentiment: " + result[0]['label'])
    st.markdown("#### Accuracy: %" + str(round(result[0]['score'] * 100, 1)))