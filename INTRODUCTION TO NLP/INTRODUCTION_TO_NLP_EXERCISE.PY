"""Q1) Perform Text Preprocessing on SMSSpamCollection Dataset. The dataset can be downloaded
from https://www.kaggle.com/datasets"""

import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")

# 1) Load Dataset
df = pd.read_csv("SMSSpamCollection", sep="\t", header=None, names=["label", "message"])
print(df.head())

# 2) Initialize Stemmer & Stopwords
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

# 3) Preprocessing Function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

# 4) Apply Preprocessing
df["clean_message"] = df["message"].apply(preprocess_text)

print("\nSample Preprocessed Messages:\n", df[["message", "clean_message"]].head())
