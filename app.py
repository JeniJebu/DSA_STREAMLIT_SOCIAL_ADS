import streamlit as st
import pickle

st.header("Predition Buy,From Social_Ads")

st.write("Demo of Random Forest Classifier")

age=st.number_input(label="Enter Age",min_value=10.0,max_value=80.0,value=30.0,step=1.0)

salary=st.number_input(label="Enter Salary",min_value=1000.0,max_value=70000.0,value=5000.0,step=1000.0)

submitted=st.button('Predict')

if submitted:
    pickled_model = pickle.load(open('model.pkl','rb'))
    prediction= pickled_model.predict([(age,salary)])
    if prediction[0]==1:
        st.write("Prediction result is Purchased")
    else:
        st.write("Prediction result is Not Purchased")
