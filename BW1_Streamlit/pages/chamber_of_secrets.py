""" This page is entirely to show the possibilites of Streamlit while making it fun """

import streamlit as st
import webbrowser
from PIL import Image


#left, center, right = st.beta_columns(3)

#left_one = left.button("About Python",key = "1")
#center_one = center.button("Learn Python", key = "2")
#right_one = right.button("Practice Python", key = "3")

#if left_one:
#    generate_syntax = st.button("Generate Syntax", key = "4")
#    if generate_syntax:
#        st.write("Hello All..")


def write():
    st.title("Chamber of Secerets :door:")
    st.write("\n")
    st.write("\n")
    st.markdown(
           """### Welcome to the chamber of secrets. To unlock the chamber,
           """
    )

    #creating a function for nested buttons, because streamlit reruns the loop for every nested
    #loop and the output inside the nested loop will only be displayed for a fraction of seconds

    def riddle():
        if st.button("Solve me"):
            st.write("Why did snape stand in the middle of the road?")

    def solution():
        if st.button("Ask dobby"):
            a = Image.open('snape_meme.jpg')
            st.image(a)
            #st.balloons()

    def team():
        if st.button("The Team:"):
            #Team QR code
            col1, col2, col3 = st.beta_columns([1,2,1])
            with col1:
                st.write("")
            with col2:
                st.image("team_qrcode.jpg")
            with col3:
                st.write("")


    if st.checkbox("Click here"):
        st.balloons()
        st.markdown("Congrats, You have successfully unlocked the chamber")
        st.write("\n")
        st.markdown("## Quest1:")

        #Call the functions
        riddle()
        solution()
        team()

