import streamlit as st
import pickle
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

model = pickle.load(
    open('models/svm_sentiment_model.pkl', 'rb')
)

vectorizer = pickle.load(
    open('models/tfidf_vectorizer.pkl', 'rb')
)

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

def clean_text(text):

    text = str(text).lower()

    # remove urls
    text = re.sub(r'http\S+', '', text)

    # keep only alphabets
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

st.title("Flipkart Review Sentiment Analysis")

st.write(
    "Analyze whether a Flipkart product review is Positive or Negative."
)

review = st.text_area(
    "Enter Your Review",
    height=150
)

if st.button("Predict Sentiment"):

    cleaned_review = clean_text(review)

    review_vector = vectorizer.transform([cleaned_review])

    prediction = model.predict(review_vector)[0]

    if prediction == 1:
        st.success("Positive Review")

    else:
        st.error("Negative Review")