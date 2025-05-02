
import numpy as np
import streamlit as st
import pytesseract 
import cv2 
from PIL import Image


st.title('ID Scanner Application ')

uploaded_img = st.file_uploader('Please Upload An Image.....', type = ['jpg','png','jpeg','webp'])
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def Extract_text_fun(img):
    text = pytesseract.image_to_string(img)
    return text

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    img_array = np.array(img)
    st.image(img_array, caption ='Uploaded Image')
    
    
    with st.spinner('Extracting text from your ID...'):
        ext_text = Extract_text_fun(img_array)
        # st.write(ext_text)
        st.subheader("Extracted Text:")
        text_list = ext_text.splitlines()
        # st.write(text_list)
        st.write('Organiztion Name :',text_list[0]+ ' ' + text_list[1])
        st.write('Employee Name :',text_list[8])
        st.write(text_list[3])
        st.write(text_list[4])
        st.write(text_list[5])
        st.write(text_list[6])
