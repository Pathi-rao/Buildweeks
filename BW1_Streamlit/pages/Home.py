#Home page for the web app
import streamlit as st
import base64
from PIL import Image
import webbrowser

def write():
    st.title("Our Journey :car:")
    st.markdown(
           """## About us

We are a team of developers who are divided by nation but united by passion to learn. We are currently
developing our AI skills at [_Strive School_](https://strive.school/) with not only theortical knowledge but also
applying it practically. One such example is this web application that you are in. 

As you explore this web app, you will find our first Build week(a week where we apply our theortical knowledge
to a real-world scenario) project where we scrape [_The Best Books of the 20th Century_](https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century)


            """
    )

    st.markdown(
        """## Team Snape

That's right, we are officially called "Snape" as in [this one](https://en.wikipedia.org/wiki/Severus_Snape).
Although most of us hated him in our childhood and came to know his truself later on, we believe he is the
real protagonist in the series and so are we in real-life. 
        """
    )
    st.write("![Your Awsome GIF](https://media.giphy.com/media/vLOVgH5FABgt2/giphy.gif)")


#Give the details of the team
    def dummy_fun():
        st.markdown("## Members:")
        if st.button('Lakshmipathi rao Devalla'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/devalla-lakshmipathirao/')
        elif st.button('Deniz Elci'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/deniz-elci-2500b2205/')
        elif st.button('Thanh Nguyen'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/nguyenphuocxuanthanh/')
        elif st.button('Stephen George'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/stephen-george-b79941116/')
        elif st.button('Bilal Hussain'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/bilal-hussain-546a1a20b/')

    dummy_fun()
