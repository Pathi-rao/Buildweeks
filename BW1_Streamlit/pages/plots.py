import plotly.figure_factory as ff
import plotly.express as px
import streamlit as st
import pandas as pd

#A plot which shows avg_rating before and after normalization
def avg_rating_plot():
    hist_data = [df['avg_rating'],df['minmax_norm_ratings'],df['mean_norm_ratings']]
    group_labels = ['avg_rating', 'minmax_norm_rating','mean_norm_rating']
    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
    st.write(fig)


#Bar plot 
def awards_plot():
    st.markdown("Is there a way to know which author has most awards")
    if st.button("Author vs Awards"):
        col1, col2, col3 = st.beta_columns([1,4,1])
        with col1:
            st.write("")
        with col2:
            st.image("Barplot.PNG")
        with col3:
            st.write("")