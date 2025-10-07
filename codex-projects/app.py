import streamlit as st
import time
import pickle as pkl


#importing models
iris=pkl.load(open('iris.pkl','rb'))

def load():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    #st.button("Rerun")


#header file
st.title("Codex Projects",width=500)
st.subheader("",divider='blue')
st.header("Welcome to the MLOps Codex Projects app",divider='grey')

st.info("This app allows you to explore different machine learning projects.")
#Sidebar features
string='''Choose any of the project below\n
          1.Iris Dataset \n
          OR\n
          2.House Price Prediction'''
st.sidebar.header("Project Selection")
#st.sidebar.subheader("Choose a project to explore")
st.sidebar.subheader(string)
set={"iris", "house price"}
op=st.sidebar.selectbox("Select a project",set )
bt=st.button("Refresh")
if bt:
    with st.spinner('Refreshing...'):
        time.sleep(2)
    st.success('Refreshed!')

st.markdown("You selected the project:")


if op=="iris":
    st.write(f"You selected: {op}")
    load()
    petal_length=st.number_input("Enter the petal length")
    petal_width=st.number_input("Enter the petal width")
    sepal_length=st.number_input("Enter the sepal length")
    sepal_width=st.number_input("Enter the sepal width")
    data_i=[sepal_length,sepal_width,petal_length,petal_width]
    
    easter_egg=[69.00,69.00,69.00,69.00]
    if data_i==easter_egg:
        st.error("There is no such flower mate")
        st.button("Try Again")
    else:
        if st.button("Predict"):
            if petal_length and petal_width and sepal_length and sepal_width:
                pred=iris.predict([data_i])
                if pred==0:
                    st.write(f"The predicted flower is Setosa")
                elif pred==1:
                    st.write(f"The predicted flower is Versicolor")
                else:
                    st.write(f"The predicted flower is Virginica")
            else:
                st.write("Please enter all the fields")
    #st.write("Pussy is power.")
    # Add more details or functionality for the iris-dataset project here
else:
    load()
    st.write(f"You selected: {op}")
    
    


