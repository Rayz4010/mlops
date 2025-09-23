import streamlit as st
import PIL.Image
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = 'AIzaSyCXsFF8QZrSYc5D95LEX3fm009LwsJNMDc'
genai.configure(api_key = os.environ["GOOGLE_API_KEY"])

st.title('Image to text generation using LLM') 
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def img_user_query(img,query):
    response = model.generate_content([query,img]).text
    return response

upload_image=st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
query=st.text_input("Enter waht you want from the image")

if st.button('Generate'):
    if upload_image:
                img = PIL.Image.open(upload_image)
                #result = img_user_query(img, query)

                st.write('Just win today')