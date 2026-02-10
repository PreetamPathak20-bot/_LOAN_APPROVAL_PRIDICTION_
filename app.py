import streamlit as st
import pandas as pd
import pickle as pk

# [2] Load the preserved model and scaler
model = pk.load(open('model.pickle', 'rb'))
scaler = pk.load(open('scaler.pickle', 'rb'))

# 2. UI Header aur Description [Conversational Request]
st.header('🤖 Loan Approval Prediction') 
st.markdown('**Developed by Group C under leading of Sunny Sir**')

# 3. Input Widgets with Unique Icons [4-7]
# Humne har label mein icon add kiya hai taaki user ko samajhne mein aasani ho
no_of_dep = st.slider('👨‍👩‍👧‍👦 Choose number of dependents', 0, 5)
grad = st.selectbox('🎓 Choose Education', ['Graduated', 'Not Graduated'])
self_emp = st.selectbox('🏢 Self Employed?', ['Yes', 'No'])
income = st.slider('💰 Annual Income', 0, 10000000)
loan_amt = st.slider('💸 Loan Amount', 0, 10000000)
duration = st.slider('⏳ Loan Duration (Years)', 1, 20)
cibil = st.slider('⭐ CIBIL Score', 100, 1000)
assets = st.slider('🏠 Total Assets (House/Car/Bank)', 0, 10000000)

# 4. Input values ko Numeric format mein convert karna [8-10]
# Training data ke mutabiq: Graduate = 1, Not Graduate = 0 | Yes = 1, No = 0
grad_status = 1 if grad == 'Graduated' else 0
emp_status = 1 if self_emp == 'Yes' else 0

# 5. Prediction ke liye DataFrame banana [7]
predict_data = pd.DataFrame([[no_of_dep, grad_status, emp_status, income, 
                              loan_amt, duration, cibil, assets]], 
                             columns=['no_of_dependents', 'education', 'self_employed', 
                                      'income_annum', 'loan_amount', 'loan_term', 
                                      'cibil_score', 'assets'])

# 6. Prediction Logic [11, 12]
if st.button('Predict'):
    # Pehle data ko scale karna [11]
    scaled_data = scaler.transform(predict_data)
    
    # Phir model se predict karwana [11]
    prediction = model.predict(scaled_data)
    
    # Result display karna [12]
    if prediction == 1:
        st.markdown('### ✅ **Loan is Approved**')
    else:
        st.markdown('### ❌ **Loan is Rejected**')