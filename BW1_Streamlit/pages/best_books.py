import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px
import time

def write():

    st.title("Best Books of the 20th century :books:")
    st.header("""**Description**: """)
    st.markdown(
            """ 
One day you are browsing through the internet and stumbled upon [Goodreads](https://www.goodreads.com/). Being a
curious _Data Scientist_, you want to know what are the best books of 20th century. Well, worry not as we did that
just for you. \n
We scrapped the website for the first 1000 *_Best Books of the 20th century_* and made a nice dataframe so that
you could also analyse it. Later down the line, we will add some visualizations to better understand the relation
between different features.

If you would like to scrape the data of other book genres by yourself, you can easily do so by
modifying the source code which you can find [here](https://github.com/Deniz-shelby/goodreads_webscrap).\n
So without wasting any time, \n
            """
        )
        
    #Gif for "Let's begin"
    st.write("![Your Awsome GIF](https://media.giphy.com/media/5zf2M4HgjjWszLd4a5/giphy.gif)")
    st.write("\n")
    st.write("\n")


    st.header("**DataFrame**:")

    #This feature is not viable during deployment as its prompts user to upload a csv file
    #and we cannot except the user to have similar DataFrame.

    #Prompt the user to upload a csv file
    #uploaded_file = st.file_uploader("Please choose a .CSV file", type=['csv'])
    #if uploaded_file is not None:
     #   # do stuff
      #  df = pd.read_csv(uploaded_file)
       # df1 = df.head()

    df = pd.read_csv('df_new_1100.csv')
    df1 = df.head()

    #Functions for rounding the avg_rating
    def round_float():
        st.dataframe(df.style.format({'avg_rating': '{:.2f}'}))
    def round_float_head():
        st.dataframe(df1.style.format({'avg_rating': '{:.2f}'}))

    st.markdown(""" You can select one of the following two options where you can choose between displaying
    the complete DataFrame or just the head (first five rows of the DataFrame).""")

    #Widgets for showing the DataFrame
    if st.button("Click here to see the full df"):
        with st.spinner('Loading the full DataFrame...'):
            time.sleep(4)
            round_float()
    elif st.button("Click here to see the head"):
        with st.spinner('Loading the head of the DataFrame...'):
            time.sleep(3)
        round_float_head()

    st.write("\n")
    st.write("\n")
    st.markdown("Now that you know how the data looks like. It's time for some analysis...")

    #penguin image for analysis
    col1, col2, col3 = st.beta_columns([2,1,1])
    with col1:
        st.image("450px-Kowalski.jpg")
    with col2:
        st.write("")
    with col3:
        st.write("")


    #User interactive analysis
    st.write("\n")
    st.write("\n")
    st.header("**A playground for Data Analysis** :football:")
    st.markdown("""Inorder to analyse the data we've implemented an interface where _you_ as a user 
    can interact with the dataset and play with it.\n""")

    #A tab where an user can select the columns that he wants to display
    interactive_col = st.multiselect("Please select the columns that you want to display from the above data.", df.columns)

    #A slider where an user can adjust the range of the values of given column
    slider3 = st.slider('Average_Ratings:',3.5, 5.0)
    slider1 = st.slider('Number of Pages:',23,1000)
    slider2 = st.slider('Publishing Year:',1900,2000) 

    #When the user selects the avg rating from slider, it wont do the round off
    filter3 = df[df.avg_rating >= slider3]
    #st.dataframe(df.style.format({'avg_rating': '{:.2f}'}))
    #Yet to implement the modification here
    st.dataframe(filter3[interactive_col].style.set_properties(**{'background-color': 'black', 'color': 'white', 'border-color': 'blue'})) 

    filter1 = df[df.num_pages >= slider1]
    st.dataframe(filter1[interactive_col].style.set_properties(**{'background-color': 'black', 'color': 'white', 'border-color': 'blue'}))
    
    filter2 = df[df.original_publish_year >= slider2]
    st.dataframe(filter2[interactive_col].style.set_properties(**{'background-color': 'black', 'color': 'white', 'border-color': 'blue'}))

    st.write("\n")
    st.write("\n")

    #Make the plots
    st.header("**Insights** :chart:")
    st.markdown("### How can we provide more insights and help in making better decisions?")


    #Bar plot  
    st.markdown("1. Which author has the most number of awards?")
    if st.button("This one"):
        col1, col2, col3 = st.beta_columns([1,4,1])
        with col1:
            st.write("")
        with col2:
            st.image("Barplot.PNG")
        with col3:
            st.write("")
    
    st.write("\n")
    st.write("\n")

    #Pie chart for diff genres  
    st.markdown("2. Percentage of diff Genres")
    if st.button("Here"):
        col1, col2, col3 = st.beta_columns([1,4,1])
        with col1:
            st.write("")
        with col2:
            st.image("Genres.png")
        with col3:
            st.write("")

    st.write("\n")
    st.write("\n")

    st.markdown("3. Avg_rating by different countries")
    if st.button("Countries"):
        col1, col2, col3 = st.beta_columns([1,4,1])
        with col1:
            st.write("")
        with col2:
            st.image("countries.PNG")
        with col3:
            st.write("")

    st.write("\n")
    st.write("\n")

    st.markdown("""4. Avg_rating before and after 
    [normalization](https://en.wikipedia.org/wiki/Normalization) technique""")

    if st.button("Norm."):
        #A plot which shows avg_rating before and after normalization
        hist_data = [df['avg_rating'],df['minmax_norm_ratings'],df['mean_norm_ratings']]
        group_labels = ['avg_rating', 'minmax_norm_rating','mean_norm_rating']
        # Create distplot with custom bin_size
        fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
        st.write(fig)


    #Desicions on probability
    st.header("**Make your decisions wisely**")
    st.write("\n")
    st.markdown("- The probability of a book that is part of a series has won an award is: 60.89 %")
    st.markdown("- The probability of a fictional book being in top 50 is:   90%")