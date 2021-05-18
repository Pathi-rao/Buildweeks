#Do the imports
import streamlit as st
import pages.Home
import pages.best_books
import pages.chamber_of_secrets
import base64
from PIL import Image
import resources.ast as ast

#Navigation bar
PAGES = {
    "Home": pages.Home,
    "Build week-1": pages.best_books,
    "Chamber of Secrets": pages.chamber_of_secrets
}

def main():
    st.sidebar.title("Navigation bar")
    selection = st.sidebar.radio("Go To", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Us")
    st.sidebar.info(
        """
If you are looking to hire an AI Engineer/Data Scientist or even better a team of engineers,
you _really_ don't want to miss [*these*](https://qr-creator.com/urls/fY_LDoIwFEQ_yJQCAQzu8BFdGDe6bnKBht5Qbgkton69UDeuWM5JJjNHKOd6u-N8mqZAI7WyRgoq03EkXkvCD5O6QhanYVjGcZhysd54gtbANLRWddiDUziAWS9RM74l9Wo01WsEcgpIrTdK1KCZGq0FJJYmGUQQh-V6yTrZK0mskWZoJCu3eZ5EUZRxcVw8N8WhYKfZdY5ewoPrn4gHs414LA99uvnrYr_88eDiPw3i_hvz7LwMii8) awesome candidates.
        """
    )

    st.sidebar.title("Our Mentors")
    st.sidebar.info(
        """
This work wouldn't have been possible without the help of these _Awesome_ mentors. 
- [Jan Carbonell](https://www.linkedin.com/in/jancarbonell/)
- [Antonio Marsella](https://www.linkedin.com/in/antonio-marsella/)
- [Jon perez](https://www.linkedin.com/in/jon-perez-etxebarria-7901271b2/)

        """        
    )

unsafe_allow_html = True

if __name__ == "__main__":
    main()