import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from sklearn import datasets
from sklearn.svm import SVC

model = pickle.load(open('model.pkl', 'rb'))

st.header("IRIS CLASSIFICATION")
st.write("ANDHIKA NUR FIRDAUS -- 2019230061")

img = Image.open ('iris.png')
st.image(img, use_column_width=False)
st.write("ISI SEMUA NILAI DIBAWAH INI UNTUK MENDAPATKAN PREDIKSI:")

st.sidebar.header('PARAMETER iNPUTAN')

SepalLengthCm = st.sidebar.slider('SepalLengthCm:', 2.0, 6.0)
SepalWidthCm = st.sidebar.slider('SepalWidthCm:', 0.0, 5.0)
PetalLengthCm = st.sidebar.slider('PetalLengthCm',0.0, 3.0)
PetalWidthCm = st.sidebar.slider('PetalWidthCm:', 0.0, 2.0)
data = {'SepalLengthCm': SepalLengthCm,
        'SepalWidthCm': SepalWidthCm,
        'PetalLengthCm': PetalLengthCm,
        'PetalWidthCm': PetalWidthCm}

features = pd.DataFrame(data, index=[0])

st.subheader('PARAMETER INPUTAN')
st.write(features)
