# 📰 Fake News Detection System

## 📌 Overview

This project aims to classify news articles as **Fake** or **Real** using Natural Language Processing (NLP) and Machine Learning techniques.
The system is trained on a labeled dataset and deployed as an interactive web application using Streamlit.

---
## 📂 Files
notebook.ipynb: Main Jupyter Notebook with data analysis, preprocessing,feature extraction,model buildingand result<br>
app.py: Streamlit app for interactive fake news prediction<br>
download_dataset.py: Dataset  "true.csv" and "fake.csv" 
appscreenshot

## 📂 Dataset
 Due to GitHub file size limitations, the dataset is not included in this repository

* Source: Kaggle Fake News Dataset
Run the following to download it:
```bash
pip install kaggle
python download_data.py
```

## ⚙️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * pandas, numpy
  * scikit-learn
  * nltk (for preprocessing)
  * matplotlib, seaborn (visualization)
  * streamlit (deployment)

---
## 📊 Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~98%     |
| Naive Bayes         | ~93%     |
| Random Forest       | ~99%     |
| SVM                 | ~99%     |
| PassiveAggressive   | ~99%     |

## 🚀 Deployment

The model is deployed using **Streamlit** to provide an interactive UI.

### ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
---

## ❓ Why this project?

- Misinformation spreads rapidly online, making it hard to identify trustworthy news.<br>
- Uses Machine Learning and NLP to classify news as **Fake  or **Real .<br>
- Demonstrates a real-world ML pipeline from preprocessing to deployment.<br>

