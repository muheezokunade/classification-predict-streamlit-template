"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""


# Streamlit dependencies
import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
import numpy as np 
import joblib,os
from PIL import Image
import pickle

# Load your raw data
raw = pd.read_csv("resources/trainn.csv")

# Vectorizer
news_vectorizer = open("resources/vect_20.pkl","rb")
tweet_cv = joblib.load(news_vectorizer)


#img1 = Image.open("classi-predict\resources\imgs\homepage.jpg")
#st.image("https://media.istockphoto.com/id/1311598658/photo/businessman-trading-online-stock-market-on-teblet-screen-digital-investment-concept.jpg?s=612x612&w=0&k=20&c=HYlIJ1VFfmHPwGkM3DtVIFNLS5ejfMMzEQ81ko534ak=", width=700)
# Creating layout sidebars#
nav = st.sidebar.selectbox("Navigation",["Home","About Us","Show a Demo", "Prediction", "Contribute to Data"])

def home():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0099ff;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #b7cbeb;
        color:#ff0000;
        }
    </style>""", unsafe_allow_html=True)
    but1,but2,but3,but4,but5 = st.columns([1,1.5,2,1.5,2])
    if but1.button("Home", key=1):
        home()
    elif but2.button("About Us", key=2):
        about_us()
    elif but3.button("Show a Demo", key=3):
        nav = "Show a Demo"
    elif but4.button("Prediction", key=4):
        pred()
    elif but5.button("Contribute to data", key=5):
        contri()
    st.title("DataPoint Inc.")
    st.image("https://tinyurl.com/3my8mkfh", width=700)
    st.write("--")
    col1,col2 = st.columns([1,2.5])
    col2.markdown("## WHY CHOOSE US")
    aa1,aa2,aa3 = st.columns([1,1,1])
    aa1.markdown("#### INSIGHTS")
    aa1.write("Discover and analyse important information and trends in your data")
    aa2.markdown("#### MODELS")
    aa2.write("Helping businesses be the model and pace setter across different industries")
    aa3.markdown("#### VALUE")
    aa3.write("Project your business value by providing on point data intelligence")
    st.write("--")
    v1,v2 = st.columns([23,1])
    v1.markdown("<h1 style='text-align: center; color: black;'> Our Clients</h1>", unsafe_allow_html=True)
    x1,x2,x3,x4 = st.columns([1,1,1,1])
    x1.image("https://tinyurl.com/3yyrjuad")
    x2.image("https://tinyurl.com/2p8pzf7x")
    x3.image("https://tinyurl.com/yfr9nwaz")
    x4.image("https://tinyurl.com/2ppestpb")
    st.write("--")
    col3,col4 = st.columns([1,2])
    col4.markdown("## Contact Us")
    col5 = st.text_input("Email", "Enter your email")
    col6 = st.text_area("Message", "Your Message")
    but11,but12,but13 = st.columns([1,4,1])
    if but11.button("Submit"):
        st.write("We are glad to hear from you")
  
def about_us():
    n = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0099ff;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #b7cbeb;
        color:#ff0000;
        }
    </style>""", unsafe_allow_html=True)
    bt1,bt2,bt3,bt4,bt5 = st.columns([1,1.5,2,1.5,2])
    if bt1.button("Home"):
        home()
    elif bt2.button("About Us"):
        about_us()
    elif bt3.button("Show a Demo"):
        nav = "Show a Demo"
    elif bt4.button("Prediction"):
        pred()
    elif bt5.button("Contribute to data"):
        contri()
    # z1,z2,z3 = st.columns([1,1,1])
    # z2.markdown("## About Us")

    st.write("<h1 style='text-align: center; color: brown;'>At DataPoint, we are the bridge between your past experiences and future possibilities. We help businesses make informed decisions by getting insights on data, and make plans for the future</h1>", unsafe_allow_html=True)
    st.write("--")
    a1,a2,a3 = st.columns([1,1,1])
    b1,b2,b3 = st.columns([1,1,1])
    c1,c2,c3 = st.columns([3,6,1])
    a1.markdown("### Why Choose Us")
    a1.write("Discover and analyse hidden information and trends in your data.")
    b3.markdown("### Vision")
    b3.write("Become a leading business intelligence provider beyond the African shores")
    c2.markdown("## Meet Our Team")
    c1.write("")
    d1,d2,d3= st.columns([1,1,1])
    e1,e2,e3= st.columns([1,1,1])
    d1.image("https://tinyurl.com/ycyrmta5")
    d1.write("#### Ruth Ossai, CEO")
    d2.image("https://tinyurl.com/ycyrmta5")
    d2.write("#### Ruth Ossai, CEO")
    d3.image("https://tinyurl.com/ycyrmta5")
    d3.write("#### Ruth Ossai, CEO")
    e1.image("https://tinyurl.com/ycyrmta5")
    e1.write("#### Ruth Ossai, CEO")
    e2.image("https://tinyurl.com/ycyrmta5")
    e2.write("#### Ruth Ossai, CEO")
    e3.image("https://tinyurl.com/ycyrmta5")
    e3.write("#### Ruth Ossai, CEO")
    st.write("--")
    st.write("<h1 style='text-align: center; color: purple;'>DataPoint Inc</h1>", unsafe_allow_html=True)

def pred():
    n = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0099ff;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #b7cbeb;
        color:#ff0000;
        }
    </style>""", unsafe_allow_html=True)
    t1,t2,t3,t4,t5 = st.columns([1,1.5,2,1.5,2])
    if t1.button("Home"):
        home()
    elif t2.button("About Us"):
        about_us()
    elif t3.button("Show a Demo"):
        nav = "Show a Demo"
    elif t4.button("Prediction"):
        pred()
    elif t5.button("Contribute to data"):
        contri()
    st.title("Tweet Classifer")
    st.subheader("Climate Change Tweet classification")
    st.info("Prediction with ML Models")
		# Creating a text box for user input
    tweet_text = st.text_area("Enter Text","Type Here")

    if st.button("Classify"):
		# Transforming user input with vectorizer
        #tweet_cv.fit([tweet_text])
        vect_text = tweet_cv.transform([tweet_text]).toarray()
		# Load your .pkl file with the model of your choice + make predictions
		# Try loading in multiple models to give the user a choice
        predictor = joblib.load(open(os.path.join("resources/log_reg_model.pkl"),"rb"))
        prediction = predictor.predict(vect_text)

		# When model has successfully run, will print prediction
		# You can use a dictionary or similar structure to make this output
		# more human interpretable.
        st.success("Text Categorized as: {}".format(prediction))

def show_a_demo():
    st.title("Climate Change Project")
    st.subheader("Project Overview")
    st.video("https://youtu.be/mkjwxmcdb0E")
    st.subheader("Project Information")
    st.subheader("Exploratory Data Analysis")
    st.subheader("Models")


def contri():
    st.header("Contribute to our dataset")
    pst = st.text_area("Enter your post")
    senti = st.number_input("Enter the sentiment no.",-1,3)
    twi_id = st.number_input("Enter Tweet ID")
    if st.button("Submit"):
        to_add = {"sentiment":[senti], "message":[pst], "tweetid":[twi_id]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("resources/data/train.csv", mode="a", header=False, index=False)
        st.success("Thanks for your contribution")


if nav == "Home":
    home()
    

elif nav == "About Us":
    about_us()

elif nav == "Show a Demo":
    show_a_demo()

elif nav == "Prediction":
    pred()

elif nav == "Contribute to Data":
    contri()
