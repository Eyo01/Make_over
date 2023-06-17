import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Mac jonny's make_over", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_9osuehx9.json")

with st.container():
    st.subheader("Hi, I am Joan :wave:")
    st.title("A Makeup Artist From Nigeria")
    st.write("My passion for make-up drives me to create versatile looks that take your natural beauty to the next level. The creation of beauty is an art and we're those performing artists. Good makeup means a good day! It takes a lot of patience and practice to get the right look.")
    st.write("[Learn more >](https://wa.me.-8147823220)")


with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
      st.header("What I do")
      st.write("##")
      st.write(
        """
        As a makeup Artist,some of my decorums are:
        - Bridal Makeup Artist: Specialize in creating beautiful, natural-looking makeup for brides, bridesmaid, mothers of the bride and groom, and other family members.
        - Editorial Makeup artist: Works in the publishing industry, creating makeup looks for fashion magazines, catalogs, and other publications.     
        - Fashion Makeup Artist: Works in the fashion industry, creating bold and avant-garde looks for runway shows, editorial photo shoots, and advertising campaign.
        - Celebrity Makeup artist: I also work with celebrities, creating looks for red carpet events, movie premieres, and other high-profile appearances.
      
        If this sounds interesting to you, consider checking out my instagram page to see some of my works.
      
                           """)   
      st.write("[Instagram Page >](https://instagram.com/macjonnys_makeover?igshid=Y2IzZGU1MTFhOQ%3D%3D)") 

  with right_column:
      st_lottie(lottie_coding, height=450, key="Makeup")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """ 
    <form action="https://formsubmit.co/joanieee101@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>""" 

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty() 
      