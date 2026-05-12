# 💳 Credit Card Fraud Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

A machine learning project that detects fraudulent credit card transactions using **Logistic Regression**, built on a real-world dataset of 284,807 transactions.

---

## 🧠 Problem Statement

Credit card fraud is a critical problem in the financial industry. The challenge lies in the **extreme class imbalance** — only 0.17% of transactions are fraudulent. This project addresses that with undersampling and binary classification.

---

## 📊 Dataset

| Property | Value |
|---|---|
| Total Transactions | 284,807 |
| Fraudulent | 492 (0.17%) |
| Legitimate | 284,315 |
| Features | 30 anonymized (V1–V28) + Amount + Time |

> Source: [Kaggle — Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## ⚙️ Approach

1. **EDA** — Explored class distribution, transaction amounts, and feature statistics
2. **Undersampling** — Sampled 492 legitimate transactions to balance the classes
3. **Train/Test Split** — 80/20 split with stratification
4. **Model Training** — Logistic Regression (scikit-learn)
5. **Evaluation** — Accuracy on both training and test sets

---

## 📈 Results

| Dataset | Accuracy |
|---|---|
| Training | **94.79%** |
| Testing | **93.40%** |

---

## 🗂️ Project Structure

```
├── CreditCardScamDetection.ipynb   # EDA + model training notebook
├── test.py                         # Streamlit web app for live prediction
└── .gitignore
```

---

## 🚀 Run the Web App

```bash
pip install streamlit scikit-learn pandas numpy
streamlit run test.py
```

> ⚠️ Place `creditcard.csv` in the same directory before running.

---

## 🛠️ Tech Stack

- **Language** — Python
- **Libraries** — NumPy, pandas, scikit-learn
- **Web App** — Streamlit

---

## 👤 Author

**Utkarsh** — [GitHub](https://github.com/Utkarsh7106) · [LinkedIn](www.linkedin.com/in/utkarshmishra7106)
