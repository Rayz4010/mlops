import streamlit as st
import time
import pickle as pkl



#globals
flag=False
#importing models
iris=pkl.load(open('iris.pkl','rb'))
housing=pkl.load(open('housing_model.pkl','rb'))


#the loading function just for asthetics though
def load():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    #st.button("Rerun")





#Sidebar features
def sidebar():
    global op
    string='''Choose any of the project below\n
            1.Iris Dataset \n
            OR\n
            2.House Price Prediction'''
    st.sidebar.header("Project Selection")
    #st.sidebar.subheader("Choose a project to explore")
    st.sidebar.subheader(string)
    set={"iris", "house price"}
    op=st.sidebar.selectbox("Select a project",set )
    if True:
        refresh()
    
def space():
    st.subheader("") 
    
def refresh():    
    bt=st.sidebar.button("Refresh")
    if bt:
        with st.spinner('Refreshing...'):
            time.sleep(2)
        st.success('Refreshed!')


#header file
st.title("Codex Projects",width=500)
st.subheader("",divider='blue')
st.header("Welcome to the MLOps Codex Projects app",divider='grey')
space()
st.info("This app allows you to explore different machine learning projects.")
space()


def house_input():
    global flag
    area=st.number_input("Enter area of the house: ")
    bedrooms=st.number_input("Enter number of bedrooms: ")
    bathrooms=st.number_input("Enter number of bathrooms: ")
    stories=st.number_input("Enter number of stories: ")
    mainroad=st.number_input("Is the house on main road (1 for yes, 0 for no): ")
    guestroom=st.number_input("Is there a guest room (1 for yes, 0 for no): ")
    basement=st.number_input("Is there a basement (1 for yes, 0 for no): ")
    hotwaterheating=st.number_input("Is there hot water heating (1 for yes, 0 for no: ")
    airconditioning=st.number_input("Is there air conditioning (1 for yes, 0 for no): ")
    parking=st.number_input("Enter number of parking spaces: ")
    prefarea=st.number_input("Is the house in preferred area (1 for yes, 0 for no): ")
    furnish=st.number_input("Enter furnishing status (2 for furnished, 1 for semi-furnished, 0 for unfurnished): ")
    data_house=[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnish]
    if area and bedrooms and bathrooms and stories and mainroad in [0,1] and guestroom in [0,1] and basement in [0,1] and hotwaterheating in [0,1] and airconditioning in [0,1] and parking and prefarea in [0,1] and furnish in [0,1,2]:
        flag=True
        return data_house

def iris_input():
        global flag
        petal_length=st.number_input("Enter the petal length")
        petal_width=st.number_input("Enter the petal width")
        sepal_length=st.number_input("Enter the sepal length")
        sepal_width=st.number_input("Enter the sepal width")
        data_i=[sepal_length,sepal_width,petal_length,petal_width]
        if petal_length and petal_width and sepal_length and sepal_width:
            flag=True
            return data_i

#main body
def main():
    sidebar()
    st.markdown("You selected the project:")


    if op=="iris":
        st.markdown(f"You selected: {op}")
        load()
        data_i=iris_input()
        
        easter_egg=[69.00,69.00,69.00,69.00]
        if data_i==easter_egg:
            st.error("There is no such flower mate")
            st.button("Try Again")
        else:
            if st.button("Predict"):
                st.write(flag)
                if flag==True:
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
        data=house_input()
        if st.button("Predict"):
            if flag==True:
                price=housing.predict([data])[0]
                st.write(f"The predicted price of the house is ${price:.2f}")
            else:
                st.write("Please enter all the fields")


if __name__ == '__main__':
    main()
    pass