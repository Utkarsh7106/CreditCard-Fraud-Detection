import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st 

import pandas as pd

# loading the dataset to a Pandas DataFrame
credit_card_data = pd.read_csv('creditcard.csv')

# separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

#undersample legitimate transactions to balance the class
legit_sample = legit.sample(n=492)
new_dataset = pd.concat([legit_sample, fraud], axis=0)

#split data into training and testing sets
X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

#train logistic regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

#evaluate model performance
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# webpage
st.title(" Credit Card Fraud Detection ")
input_df = st.text_input(' Enter all required features values ')
input_df_splited = input_df.split(' , ')
sunmit = st.button(" Submit ")

if submit:
    features = np.asarray(input_df_splited,dtype = np.float64)
    prediction = model.predict(features.reshape(1,-1))
    
    if prediction[0] == 0:
        st.write(" Legitimate Transaction ")
    else:
        st.write(" Fraudulant Transaction ")
