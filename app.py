import streamlit as st
import base64    #pip install pybase64
import streamlit.components.v1 as components
from PIL import Image
import os


st.set_page_config(layout="wide")

page_bg_img =  """
    <style>
    [data-testid="stMetricLabel"] {
        opacity:0;
        margin: -30px;
    }

    [data-testid="stSidebarNav"] {
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }

    [data-testid="stSidebar"] {
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        opacity: 0.85
    }

    [data-testid="stHeader"] {
        background-colour:rgba(0,0,0,0);
        colour: white;
        opacity: 0.1;
        margin = 1%
    }

    [data-testid="stToolbar"] {
        right: 2rem
    }

    [class="css-1wivap2 e16fv1kl3"] {
        background-color: #E6F3FB;
        border: 2px solid #c5d1f6;
        padding: 3%;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8;
        text-align: center;
    }

        [data-testid="stImage"] {
        width: 100%;
        text-align: center;
        margin: 1%
    }

    [data-testid="stText"] {
        width: auto;
        text-align: center;
        display: block;
        position: relative;
        left: 0%;
        border:5px;
        padding:10px;
        border-radius: 15px;
        background-color:#40414A;
        box-shadow: 3px 3px #28282D;
        border-radius: 4px;
        opacity: 0.9;
        margin: 3%
    }

    [class="css-10trblm e16nr0p30"] {
        padding: 3%;
        text-align: center;
    }

    </style>
"""


st.sidebar.success("Select a page above.")

col1, col2 = st.columns([1,3])
col1.image("assets/images/netflixlogo.jpg")
col2.title("Netflix Wrapped")

st.markdown(page_bg_img, unsafe_allow_html=True)



col1, col2 = st.columns(2)

st.header("How can I get my Netflix wrapped?")
st.text("Follow these simple instructions!")

st.subheader("Step One: Download your Netflix data")


st.text("""
        Log into your netflix account.
        Go to the dropdown menu in the upper right corner. Click on account and navigate to settings.
        Select the "Download your personal information" to request a copy of your personal information on Netflix.
        Scroll to the bottom of the page and click on "Submit Request" then click on "Confirm Request"
        Netflix will notify you when your download is ready - this can take up to 30 days!

        Once you have the zip file with your information, you have completed step one!
        """)

st.subheader("Step Two: Head to the input page")

st.text("""
        This website requires you to upload the "ViewerActivity" csv file.
        Continue the instructions on that page.
        """)
