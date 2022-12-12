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
news_vectorizer = open("resources/vect_202.pkl","rb")
tweet_cv = joblib.load(news_vectorizer)


#img1 = Image.open("classi-predict\resources\imgs\homepage.jpg")
#st.image("https://media.istockphoto.com/id/1311598658/photo/businessman-trading-online-stock-market-on-teblet-screen-digital-investment-concept.jpg?s=612x612&w=0&k=20&c=HYlIJ1VFfmHPwGkM3DtVIFNLS5ejfMMzEQ81ko534ak=", width=700)
# Creating layout sidebars#
nav = st.sidebar.selectbox("Navigation",["Home","About Us","Projects", "Prediction", "Contribute to Data"])

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
    # but1,but2,but3,but4,but5 = st.columns([1,1.5,2,1.5,2])
    # if but1.button("Home", key=1):
    #     home()
    # elif but2.button("About Us", key=2):
    #     about_us()
    # elif but3.button("Show a Demo", key=3):
    #     nav = "Show a Demo"
    # elif but4.button("Prediction", key=4):
    #     pred()
    # elif but5.button("Contribute to data", key=5):
    #     contri()
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
    # bt1,bt2,bt3,bt4,bt5 = st.columns([1,1.5,2,1.5,2])
    # if bt1.button("Home"):
    #     home()
    # elif bt2.button("About Us"):
    #     about_us()
    # elif bt3.button("Show a Demo"):
    #     nav = "Show a Demo"
    # elif bt4.button("Prediction"):
    #     pred()
    # elif bt5.button("Contribute to data"):
    #     contri()
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
    d1.image("https://media.discordapp.net/attachments/1044546358721380352/1050330565108314122/IMG_5045.jpg?width=489&height=406")
    d1.write("#### Francis Egah, CEO")
    d2.image("https://media.discordapp.net/attachments/1044546358721380352/1049973783445913640/27_71_612_3800_20191117_101414.jpg?width=406&height=406")
    d2.write("#### Lesego Tiro,  Scrum Master")
    d3.image("https://media.discordapp.net/attachments/1044546358721380352/1050330068435607583/croped.jpeg?width=527&height=406")
    d3.write("#### Ruth Ossai,  Product Designer")
    e1.image("https://media.discordapp.net/attachments/1044546358721380352/1050331208480993301/IMG_7169.jpg?width=481&height=406")
    e1.write("#### Mueez Okunade,  Chief AI Engineer")
    e2.image("https://media.discordapp.net/attachments/1044546358721380352/1050135724692869120/IMG_20221101_085320_436.jpg?width=515&height=687")
    e2.write("#### Haruna Jibrin, Sales Manager")
    e3.image("https://media.discordapp.net/attachments/1044546358721380352/1049738518081060924/WhatsApp_Image_2022-12-06_at_6.14.34_PM.jpeg?width=368&height=369")
    e3.write("#### Micheal Benjamin, Business Analyst")
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
    # t1,t2,t3,t4,t5 = st.columns([1,1.5,2,1.5,2])
    # if t1.button("Home"):
    #     home()
    # elif t2.button("About Us"):
    #     about_us()
    # elif t3.button("Show a Demo"):
    #     nav = "Show a Demo"
    # elif t4.button("Prediction"):
    #     pred()
    # elif t5.button("Contribute to data"):
    #     contri()
    p1,p2,p3 = st.columns([2,1,1])
    p1.title("Tweet Classifer")
    p2.write("powered by")
    p2.image("https://media.discordapp.net/attachments/1044546358721380352/1050511721107820624/download_3_1.png")
    st.subheader("Climate Change Tweet classification")
    st.info("Prediction with ML Models")
		# Creating a text box for user input
    tweet_text = st.text_area("Enter Text","Type Here")
    option = st.selectbox(
        "Select Machine Learning Model",
        ("Logistic Regression", "Naive Bayes", "Random Forest Classifier")
    )
    if option == "Logistic Regression":
        if st.button("Classify"):
            # Transforming user input with vectorizer
            #tweet_cv.fit([tweet_text])
            vect_text = tweet_cv.transform([tweet_text]).toarray()
            # Load your .pkl file with the model of your choice + make predictions
            # Try loading in multiple models to give the user a choice
            predictor = joblib.load(open(os.path.join("resources/log_regg_model.pkl"),"rb"))
            prediction = predictor.predict(vect_text)

            # When model has successfully run, will print prediction
            # You can use a dictionary or similar structure to make this output
            # more human interpretable.
            if prediction == 1:
                st.success("Text Categorized as Neutral in Climate Change Sentiment")
            elif prediction == 0:
                st.success("Text Categorized as Pro in Climate Change Sentiment")
            elif prediction == -1:
                st.success("Text Categorized as News in Climate Change Sentiment")
            elif prediction == 2:
                st.success("Text Categorized as Anti Climate Change Sentiment")
    elif option == "Naive Bayes":
        if st.button("Classify"):
            # Transforming user input with vectorizer
            #tweet_cv.fit([tweet_text])
            vect_text = tweet_cv.transform([tweet_text]).toarray()
            # Load your .pkl file with the model of your choice + make predictions
            # Try loading in multiple models to give the user a choice
            predictor = joblib.load(open(os.path.join("resources/nv_model.pkl"),"rb"))
            prediction = predictor.predict(vect_text)

            # When model has successfully run, will print prediction
            # You can use a dictionary or similar structure to make this output
            # more human interpretable.
            if prediction == 1:
                st.success("Text Categorized as Neutral in Climate Change Sentiment")
            elif prediction == 0:
                st.success("Text Categorized as Pro in Climate Change Sentiment")
            elif prediction == -1:
                st.success("Text Categorized as News in Climate Change Sentiment")
            elif prediction == 2:
                st.success("Text Categorized as Anti Climate Change Sentiment")
    elif option == "Random Forest Classifier":
        if st.button("Classify"):
            # Transforming user input with vectorizer
            #tweet_cv.fit([tweet_text])
            vect_text = tweet_cv.transform([tweet_text]).toarray()
            # Load your .pkl file with the model of your choice + make predictions
            # Try loading in multiple models to give the user a choice
            predictor = joblib.load(open(os.path.join("resources/nv_model.pkl"),"rb"))
            prediction = predictor.predict(vect_text)

            # When model has successfully run, will print prediction
            # You can use a dictionary or similar structure to make this output
            # more human interpretable.
            if prediction == 1:
                st.success("Text Categorized as Neutral in Climate Change Sentiment")
            elif prediction == 0:
                st.success("Text Categorized as Pro in Climate Change Sentiment")
            elif prediction == -1:
                st.success("Text Categorized as News in Climate Change Sentiment")
            elif prediction == 2:
                st.success("Text Categorized as Anti Climate Change Sentiment")

def projects():
    st.title("Climate Change Project")
    st.subheader("Project Overview")
    st.video("https://youtu.be/mkjwxmcdb0E")
    st.subheader("Project Information")
    st.write("The aim is to design and create a Machine learning Model that is able to classify wether or not a person believes in climate change.Providing an accurate and robust solution to this task gives companies access to a broad base of consumer sentiment, spanning multiple demographic and geographic categories - thus increasing their insights and informing future marketing strategies")
    st.subheader("Exploratory Data Analysis")
    # Create a section for the dataframe header
    st.markdown('#### Header of Dataframe')
    st.write(raw.head())
    st.markdown('#### Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    s=raw['sentiment'].value_counts().to_dict()
    ax.bar(s.keys(),s.values())
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.set_xticklabels(['what', 'News','Pro', 'Neutral', 'Anti'], rotation=0)
    ax.set_ylabel('Count')
    ax.set_xlabel('Sentiment')
    st.pyplot(fig)

    # Visualising the percentage distribution of sentiments
    fig, ax = plt.subplots(1,1)
    ax.pie(raw.sentiment.value_counts().values, 
        labels = ["Neutral", "Anti", "Pro", "News"], 
        autopct = '%2.1f%%', textprops={'fontsize': 8})
    ax.set_title('Tweet Sentiment Percentage Distribution', fontsize=10)
    st.pyplot(fig)

    st.subheader("Models")
    st.write("**Logistic Regression:** Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lies between 0 and 1. Logistic Regression is much similar to Linear Regression except for how they are used. Linear Regression is used for solving Regression problems, whereas Logistic regression is used for solving the classification problems. In Logistic regression, instead of fitting a regression line, we fit an 'S' shaped logistic function, which predicts two maximum values (0 or 1). The curve from the logistic function indicates the likelihood of something such as whether the cells are cancerous or not, a mouse is obese or not based on its weight, etc.")
    st.image("https://static.javatpoint.com/tutorial/machine-learning/images/logistic-regression-in-machine-learning.png")
    st.write("**Naive-Bayes MultiNominal NB:** Naïve Bayes — a probabilistic approach for constructing the data classification models. It’s formulated as several methods, widely used as an alternative to the distance-based K-Means clustering and decision tree forests, and deals with probability as the “likelihood” that data belongs to a specific class. The Gaussian and Multinomial models of the naïve Bayes exist. The multinomial model provides an ability to classify data, that cannot be represented numerically. Its main advantage is the significantly reduced complexity. It provides an ability to perform the classification, using small training sets, not requiring to be continuously re-trained.(Arthur v. 2021)")
    st.write("**Random Forest Classifier:** Random forests is a supervised learning algorithm. It can be used both for classification and regression. It is also the most flexible and easy to use algorithm. A forest is comprised of trees. It is said that the more trees it has, the more robust a forest is. Random forests creates decision trees on randomly selected data samples, gets prediction from each tree and selects the best solution by means of voting. It also provides a pretty good indicator of the feature importance.")
    st.image("http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1526467744/voting_dnjweq.jpg")

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

elif nav == "Projects":
    projects()

elif nav == "Prediction":
    pred()

elif nav == "Contribute to Data":
    contri()
