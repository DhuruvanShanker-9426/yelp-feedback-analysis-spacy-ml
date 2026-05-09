import joblib
import streamlit as st
import time
from utils.text_preprocessing import text_preprocessing,text_to_vector

model=joblib.load("yelp_nlp_streamlit/model/yelp_analysis_model.pkl")

st.title("⭐ Yelp Review Sentiment Analysis")

st.info(
    "💬 This application analyzes customer reviews and predicts whether the feedback is Negative, Neutral, or Positive."
)

st.subheader("📝 Customer Review")

review = st.text_area(
    "Write a customer review below:",
    placeholder="Example: The food was amazing and the service was excellent!",
    height=120
)

if st.button("🔍 Predict Sentiment"):
    review = review.strip()

    if review == "":
        st.warning("⚠️ Please enter a customer review before predicting.")
        st.stop()

    with st.spinner("🔎 Analyzing the review... Please wait."):
        time.sleep(3)

        cleaned_review = text_preprocessing(review)
        review_to_vector = text_to_vector(cleaned_review)

        prediction = model.predict([review_to_vector])

        class_names = ["Negative", "Neutral", "Positive"]
        result = class_names[prediction[0]]

        st.markdown("---")
        st.subheader("📊 Prediction Results")

        st.info(f"Original Review: {review}")
        
        if result == "Negative":
            st.error(f"😞 Sentiment: {result}")
            st.error("⭐ Predicted Rating Category: 1 or 2 stars")

        elif result == "Positive":
            st.success(f"😊 Sentiment: {result}")
            st.success("⭐ Predicted Rating Category: 4 or 5 stars")

        else:
            st.warning(f"😐 Sentiment: {result}")
            st.warning("⭐ Predicted Rating Category: 3 stars")

        st.markdown("---")
        st.subheader("ℹ️ Model Information")

        st.markdown(
            """
            **Model Insights**:
            - ✅ This model predicts the sentiment category of a customer review.
            - ✅ The prediction is based on the text content of the review.
            - ✅ Rating categories are grouped as Negative, Neutral, and Positive.
            """
        )

        st.markdown("---")

st.caption("📌 This tool is built for educational and demonstration purposes.")
        
        
        