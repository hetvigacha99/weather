# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 10:33:40 2025

@author: ASUS
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("D:\internship\sav_files\weather_models.sav",'rb'))
def weather_prediction(input_data):
    input_data_array=np.asarray(input_data)
    input_data_reshape=input_data_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)
    if(prediction==1):
        return "Rainy"
    elif(prediction==0):
        return "Cloudy"
    elif(prediction==3):
        return "Sunny"
    else:
        return "Snowy"
def main():
    st.title("weather predition")
    Temperature = st.text_input('Temperature (°C)')
    Humidity = st.text_input('Humidity (%)')
    WindSpeed = st.text_input('Wind Speed (km/h)')
    Precipitation = st.text_input('Precipitation (%)')
    CloudCover = st.text_input('Cloud Cover (%)')
    AtmosphericPressure = st.text_input('Atmospheric Pressure (hPa)')
    UVIndex = st.text_input('UV Index')
    Season = st.text_input('Season(0,1,3,4)')
    Visibility = st.text_input('Visibility (km)')
    Location = st.text_input('Location')
    weather=''
    if st.button('Weather Test Result'):
        weather = weather_prediction([Temperature, Humidity, WindSpeed, Precipitation, CloudCover,AtmosphericPressure, UVIndex, Season,Visibility,Location])
    st.success(weather)
main()