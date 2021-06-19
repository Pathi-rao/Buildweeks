import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image


def write():

    st.title("Rescuing Baby Yoda :baby:")
    st.header("""Description: """)
    st.markdown(
            """ 
Our goal of this project is to find the co-ordinates of "Baby-Yoda" and get to him before anyone else.
We used clustering algorithm to separate the galaxies to 3 different clusters to start our search.
\n
Then we identified the highest coordinate of the uppermost galaxy where Yoda is located.
Afterwards, we found the gravitational centre with the help of PCA method.
            """
        )


    st.header(""" Data of the galaxies: """)
    df = pd.read_csv('galaxies.csv')
    df1 = df.head()
    #X= dataset.iloc[:, [0,1]].values


    #Functions for rounding the co-ord.
    def round_float():
        st.dataframe(df.style.format({'X': '{:.2f}', 'Y': '{:.2f}'}))
    def round_float_head():
        st.dataframe(df1.style.format({'X': '{:.2f}', 'Y': '{:.2f}'}))

    st.markdown(""" Once we have the co-ordinates of all galaxies, we used K-Means clustering with number
    of clusters = 3 and intialized with K-means++ """)

    #Widgets for showing the DataFrame
    if st.button("Click here to see the corodinates of all galaxies"):
        with st.spinner('Loading the full corordinates...'):
            time.sleep(4)
            round_float()
    #elif st.button("Click here to see the head"):
    #    with st.spinner('Loading the head of the DataFrame...'):
    #        time.sleep(3)
    #    round_float_head()

   
    if st.button("Cluster of Galaxies"):
        img = Image.open("galaxies.png")
        st.image(img, caption="Cluster of Galaxies")
        #st.markdown(""" The three different colors are the  """)

    st.header(""" The nearest point to the gravitational centre will be Yoda's coordinate.""")
    st.write("\n")
    st.write("\n")
    if st.button("Location of Yoda"):
        img = Image.open("yoda.png")
        st.image(img, caption="Location of Baby-Yoda")

    if st.button("Co-ordinates of Baby-Yoda"):
        st.write(" X = 9.16,  Y = 8.8")
        st.balloons()