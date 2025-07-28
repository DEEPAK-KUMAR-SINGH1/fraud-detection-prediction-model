# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained fraud detection model from a .pkl file
model = joblib.load("Fraud_dectection_pipeline.pkl")

# Set the title of the Streamlit web app
st.title('Fraud Detection Prediction App')

# Show a brief description/instruction for the user
st.markdown('Please enter the transaction detailes and use the predict button')

# Adds a horizontal line divider in the UI
st.divider()

# Create a dropdown menu for selecting the transaction type
transaction_type = st.selectbox('Transaction Type',['PAYMENT','TRANSFER','CASH_OUT','DEPOSIT']) 
amount = st.number_input('Amount',min_value = 0.0, value= 1000.0) # Sender's balance before transaction
oldbalanceOrg = st.number_input('Old Balance (Sender)',min_value = 0.0, value =10000.0) # Numeric input for sender's account balance before the transaction
newbalanceOrig = st.number_input('New Balance (Sender)',min_value =0.0, value= 9000.0) # Numeric input for sender's account balance after the transaction
oldbalanceDest =st.number_input('Old Balance (Receiver)',min_value = 0.0,value = 0.0) # Numeric input for receiver's account balance before the transaction
newbalanceDest = st.number_input('New Balance (Receiver)',min_value = 0.0, value = 0.0) # Numeric input for receiver's account balance after the transaction

if st.button('Predict'): # When the 'Predict' button is clicked
    # Create a DataFrame with the entered input values, as the model expects input in this format
    input_data = pd.DataFrame([{
        'type' : transaction_type,
        'amount' : amount,
        'oldbalanceOrg' : oldbalanceOrg,
        'newbalanceOrig' : newbalanceOrig,
        'oldbalanceDest' : oldbalanceDest,
        'newbalanceDest' : newbalanceDest
    }])
    
    # Use the pre-trained model to predict if the transaction is fraudulent
    prediction = model.predict(input_data)[0]
    
    # Display the raw prediction (0 or 1) as a subheader
    st.subheader(f"Predicton : '{int(prediction)}'")
    
    # Based on the prediction, display appropriate success or error message
    if prediction == 1:
        st.error('This transaction can be Fraud')  # Red alert for potential fraud
    else:
        st.success('This transaction look like it is not a fraud')  # Green alert for safe transaction