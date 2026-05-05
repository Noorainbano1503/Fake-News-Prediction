# -*- coding: utf-8 -*-


#import libraries
import streamlit as st
import pickle
import re

#LOaad model vectorizer
model = pickle.load(open("/Users/noorainbano/Documents/fakenews/model.pkl", "rb"))
vectorizer = pickle.load(open("/Users/noorainbano/Documents/fakenews/vectorizer.pkl", "rb"))

#text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

#prediction function
def predict_news(news):
    news = clean_text(news)
    vectorized = vectorizer.transform([news])
    prediction = model.predict(vectorized)
    
    if prediction[0] == 1:
        return "Real News "
    else:
        return "Fake News "
def main():
#page configeration
    st.set_page_config(page_title="Fake News Detector", layout="centered")
    
    #title
    st.title(" Fake News Detection App")
    st.markdown("### Detect whether a news article is **Fake or Real**")
    
    
    #  USER INPUT
    
    news_input = st.text_area(" Enter News Text Here:", height=200)
    #  BUTTON
    
    if st.button("Predict"):
        
        if news_input.strip() == "":
            st.warning(" Please enter some text")
        
        else:
            result = predict_news(news_input)
            
            if "Real" in result:
                st.success(result)
            else:
                st.error(result)
    
    #  EXTRA FEATURES 
    
    st.markdown("---")
    st.subheader(" About this Project")
    
    st.write("""
    - Uses Machine Learning (TF-IDF + Classifier)
    - Trained on Fake & Real News Dataset
    - Supports real-time prediction
    """)
    #  FOOTER
    st.markdown("---")
    st.markdown("Made with using Streamlit")

if __name__ == "__main__":
    main()