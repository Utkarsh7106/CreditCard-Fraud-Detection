# Credit Card Fraud Detection

A machine learning project to detect fraudulent credit card transactions using Logistic Regression.

## Overview

Credit card fraud detection is a classic imbalanced classification problem. This project tackles it by undersampling the majority class (legitimate transactions) to balance the dataset, then training a Logistic Regression model.

## Dataset

- 284,807 transactions with 30 anonymized features (V1–V28), Amount, and Time
- Only 492 fraud cases (0.17% of data) — highly imbalanced
- Source: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Approach

1. Separated legitimate and fraudulent transactions
2. Undersampled legitimate transactions to match fraud count (492 each)
3. Split into 80/20 train-test with stratification
4. Trained a Logistic Regression model

## Results

| Dataset  | Accuracy |
|----------|----------|
| Training | 94.79%   |
| Testing  | 93.40%   |

## Files

- `CreditCardScamDetection.ipynb` — Full analysis and model training notebook
- `test.py` — Streamlit web app for live fraud prediction

## Tech Stack

Python, NumPy, pandas, scikit-learn, Streamlit

## Run the Web App

```bash
pip install streamlit scikit-learn pandas numpy
streamlit run test.py
```
> Note: Place `creditcard.csv` in the same directory before running.
