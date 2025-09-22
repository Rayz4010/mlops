import streamlit as st
import pickle

#load the model
model=pickle.load(open('/Users/rayquaza/Desktop/mlops/workshop/pizza_model.pkl','rb'))


st.title("Pizza Price Predictor")

age=st.number_input("Enter the age of the eater")
weight=st.number_input("Enter the weight of the eater")


if st.button("Predict"):
    #st.write('HEllo world')
    if age and weight:
        pred=model.predict([[age,weight]])
        if pred==1:
            st.write(f'with that {weight}you can eat 1 pizza')
        else:
            st.write(f'with that {weight} dont eat pizza; you fat pig  go to the gym')
    else:
        st.write("Please enter all the fields")