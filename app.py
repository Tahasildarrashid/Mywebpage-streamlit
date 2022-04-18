from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_0yfsb3a1.json")
#img_contact_form = Image.open("yt_contact_form.png")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("style/style.css")

with st.container():
    st.title("Hi! I Am Rashid T Tahasildar")
    st.subheader("A coding enthusiast and self taught programmer")
    st.subheader("I am pursuing my bachelors in PES University Bangalore")
    st.subheader("[click here > ](https://pes.edu/) to know more about pes university")

with st.container():
    st.write("---")
    left_column,  right_column = st.columns(2)
    with left_column:
        st.header("Read Me")
        st.write("##")
        st.write("Will be added later. Coming Soon!!!!!!") 
        st.write("##")
        st.write("This takes a little bit time")

with right_column:
    st_lottie(lottie_coding, height=300, key="Coding")


with st.container():
    st.write("---")
    st.subheader("My Projects:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    # with image_column:
    #     st.image(img_contact_form)
    with text_column:
        st.write("Due to technical issue image was not added")
        st.write("Images were supposed to be present here")
        st.markdown("[Watch video > ]Link to be added later")

with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
     <form action="https://formsubmit.co/tahasildarrashid233@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value = "false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder  = "Your Mail" required>
     <textarea name = "message" placeholder = "Your message here" reqiured></textarea>
     <button type="submit">Send</button>
     </form>
     """

    left_column, right_column = st.columns(2)
    with left_column:
       st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty() 