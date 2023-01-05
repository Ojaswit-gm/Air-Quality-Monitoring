#HP_SL_T13

import streamlit as st
import json
import pandas as pd 
import numpy as np
import urllib3
import matplotlib.pyplot as plt


def predict_Air_Index(Inference_DF):
    corpus = Inference_DF.drop(['created_at', 'entry_id',  'field6'],axis=1)
    
    field1= corpus["field1"].dropna().astype(float).mean()
    field2= corpus["field2"].dropna().astype(float).mean()
    field3= corpus["field3"].dropna().astype(float).mean()
    field4= corpus["field4"].dropna().astype(float).mean()
    field5= corpus["field5"].dropna().astype(float).mean()


    weight1=0.2
    weight2=0.2
    weight3=0.2
    weight4=0.2
    weight5=0.2

    # Formula must be changed to that what is required
    heuristic_Air_index=weight1*field1+weight2*field2+weight3*field3+weight4*field4+weight5*field5 


    return heuristic_Air_index 






baseURL = "https://api.thingspeak.com/channels/1925607/feeds.json?api_key=VACSRC103T19AQH9&results="

st.write("""

# Interactive Air Quality Monitoring

This Web App uses IoT based device to sense the Air Quality at a particluar location and predicts the air quality using an objective formula.

Currently this project demonstrates an End-to-End IoT based working model with a hand-crafted heuristic for air quality and random thresholds as a Proof of Concept.

 Below are the readings and predictions of our model!!!

 ## Readings
""")

option=st.slider("## Window :  Denotes Last N readins to be fetched", min_value=25, max_value=100)
baseURL = baseURL + str(option)

http = urllib3.PoolManager()
response = http.request('GET', baseURL)
data = json.loads(response.data)
Inference_DF = pd.DataFrame(data['feeds'])
air_index=predict_Air_Index(Inference_DF)

Inference_DF = Inference_DF.fillna(value=0)
print(Inference_DF.drop(['created_at', 'entry_id',  'field6'],axis=1))
st.line_chart(Inference_DF.drop(['created_at', 'entry_id',  'field6'],axis=1).astype(float))


st.write("""
## Predicted Air Quality : 
""")
st.write(air_index)



    

