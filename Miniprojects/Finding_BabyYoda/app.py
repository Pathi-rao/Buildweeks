#Do the imports
import streamlit as st
#import pages.Home
#import pages.imdb_scrapping
import pages.baby_yoda

import resources.ast as ast

#Navigation bar
PAGES = {
    #"Home": pages.Home,
    "Team project": pages.baby_yoda,
    #"Mini Projects": pages.imdb_scrapping
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("To", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("The Team")
    st.sidebar.info(
        """
Meet the Awesome team behind this project: 
- [Gavaskar Kanagaraj](https://www.linkedin.com/in/Gavaskar-kanagaraj-67878b111/)
- [Madina Zhenisbek](https://www.linkedin.com/in/madina-zhenisbek/)
- [Lakshmipathi rao Devalla](https://www.linkedin.com/in/devalla-lakshmipathirao/)
        """
    )

    st.sidebar.title("Additional Info")
    st.sidebar.info(
        """

This is an interactive streamlit app completely created with Python's library [**Streamlit**](https://streamlit.io/).
Check out their awesome source code [**here**](https://github.com/MarcSkovMadsen/awesome-streamlit).
        """
    )

if __name__ == "__main__":
    main()
