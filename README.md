# ⭐ Yelp Feedback Analysis using spaCy and Machine Learning

## Project Overview

This project is a Natural Language Processing (NLP) and Machine Learning based web application that analyzes customer feedback from Yelp reviews.

The model predicts the customer's sentiment based on the review text and classifies it into:

- Negative
- Neutral
- Positive

The project uses **spaCy** for text preprocessing and text vectorization, **LightGBM / Machine Learning** for model training, and **Streamlit** for building the web application.

---

## Live Demo

You can try the deployed Streamlit web application here:

[Live Demo - Yelp Feedback Analysis App](https://yelp-feedback-analysis-spacy-ml-iuf5cjgm8rnq2tjmnppcwa.streamlit.app/)

---

## Dataset Source

The dataset used for this project is available on Hugging Face:

[Yelp Review Full Dataset - Hugging Face](https://huggingface.co/datasets/Yelp/yelp_review_full?utm_source=chatgpt.com)

---

## Objective

The main objective of this project is to analyze customer feedback and predict the sentiment category based on review text.

This helps in understanding whether a customer's feedback is poor, average, or good.

---

## Technologies Used

- Python
- spaCy
- Machine Learning
- LightGBM
- Scikit-learn
- NumPy
- Pandas
- Joblib
- Streamlit.

---

## Dataset

The dataset used for this project is the **Yelp Review Full Dataset**.

The dataset contains customer reviews and rating labels. These reviews are used to train a Machine Learning model to understand the relationship between review text and customer sentiment.

---

## Project Workflow

1. Data Collection
2. Data Preprocessing
3. Text Cleaning using spaCy
4. Text Vectorization using spaCy word vectors
5. Model Training
6. Model Evaluation
7. Model Saving using Joblib
8. Streamlit Web App Development
9. Deployment

---

## NLP Preprocessing Steps

The text preprocessing is done using spaCy.

The preprocessing steps include:

- Converting text into lowercase
- Removing punctuation
- Removing extra spaces
- Removing stopwords
- Keeping important negation words like `not`, `no`, and `never`
- Applying lemmatization
- Converting cleaned text into numerical vectors using spaCy word vectors

---

## Machine Learning Approach

After preprocessing the review text, spaCy word vectors are used to convert the text into numerical format.

The Machine Learning model is trained using these numerical vectors to classify customer feedback into sentiment categories.

The trained model is saved using Joblib and loaded inside the Streamlit application for prediction.

---

## Prediction Categories

The model predicts feedback into three categories:

| Prediction | Meaning | Rating Category |
|---|---|---|
| Negative | Poor feedback | 1 star or 2 stars |
| Neutral | Average feedback | 3 stars |
| Positive | Good feedback | 4 stars or 5 stars |

---

## Folder Structure

    yelp-feedback-analysis-spacy-ml/
    │
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── model/
    │   └── yelp_analysis_model.pkl
    │
    └── utils/
        └── text_preprocessing.py

---

## How the App Works

1. User enters customer feedback in the Streamlit app.
2. The entered text is passed to the preprocessing function.
3. spaCy cleans the text by removing unwanted words, punctuation, and spaces.
4. The cleaned text is converted into numerical vectors using spaCy word vectors.
5. The trained Machine Learning model predicts the sentiment category.
6. The predicted result is displayed on the app.

---

## Streamlit App Features

- Simple and user-friendly interface
- Accepts customer feedback as input
- Cleans and processes text using spaCy
- Converts text into numerical vectors
- Predicts customer sentiment
- Displays predicted rating category
- Shows basic model information

---

## Example Inputs

### Positive Review

    The food was amazing and the service was excellent.

Expected output:

    Positive

### Negative Review

    The food was cold and the staff was rude.

Expected output:

    Negative

### Neutral Review

    The food was okay, nothing special.

Expected output:

    Neutral

---

## Requirements

The required libraries are listed in the `requirements.txt` file.

    streamlit
    scikit-learn
    pandas
    numpy
    joblib
    spacy
    lightgbm
    https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.8.0/en_core_web_md-3.8.0-py3-none-any.whl

---

## Run the Project Locally

Clone the repository:

    git clone <your-repository-link>

Move into the project folder:

    cd yelp-feedback-analysis-spacy-ml

Install the required packages:

    uv pip install -r requirements.txt

Run the Streamlit app:

    streamlit run app.py

---

## Model Information

The model is trained using Yelp customer review data.

The review text is preprocessed and converted into numerical vectors using spaCy. These vectors are then passed into a Machine Learning model to classify the customer feedback as Negative, Neutral, or Positive.

The trained model is saved using Joblib and reused in the Streamlit app for predictions.

---

## Future Improvements

- Improve model accuracy
- Add prediction confidence score
- Improve the Streamlit user interface
- Add more visual insights
- Try deep learning models
- Add more customer feedback analysis features

---

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be used to analyze customer feedback.

It covers the complete workflow from text preprocessing and vectorization to model training, model saving, and Streamlit app development.

This project is created for learning and educational purposes.