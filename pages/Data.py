import streamlit as st
import pandas as pd
from netflix.inputs import *
from netflix.pre_processing import *
from netflix.clean_data import clean_data
from netflix.analysis import *
import time



st.set_page_config(layout="wide")



page_bg_img =  """
    <style>

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


    [class="css-1wivap2 e16fv1kl3"] {
        background-color: #E6F3FB;
        border: 2px solid #c5d1f6;
        padding: 3%;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8;
        text-align: center;
    }

    </style>
"""

col1, col2 = st.columns([1,3])
col1.image("assets/images/netflixlogo.jpg")
col2.title("Ready?")


input_data = st.file_uploader("Upload 'Viewer Activity' CSV file", type=["csv"])

if input_data is not None:
    data = clean_data(input_data)
    users, years = user_names(data), years(data)
    user = st.selectbox("Which user would you like to see a summary for?", users)
    year = st.selectbox("Which year would you like to see a summary for", years)
    hours_watched = total_hours_watched(data, user, year)
    top_five_shows = top_five(data,user=user, year=year)
    favourite_show = top_five_shows.iloc[0][0]
    favourite_show_hours = int(round(top_five_shows.iloc[0][1],0))
    countries = countries_df(data, user, year)

if st.button("Ready!"):

    with st.spinner(f"Working on showing you {user}'s Netflix Wrapped for {year}"):
        time.sleep(3)
    st.balloons()
    time.sleep(3)


    st.metric(label="", value=f"{user}, you watched over...")
    time.sleep(2)
    st.header(f"{hours_watched} hours")
    time.sleep(1)
    st.text(f"of Netflix in {year}. That's a lot of TV!")




if st.button("Favourite Show"):
    st.subheader(f"{user}, let's have a look at some of your favourite shows...")
    time.sleep(1)
    st.subheader(f"You're most watched show was")
    time.sleep(2)
    st.header(favourite_show)
    time.sleep(1)
    st.text(f"You watched over {favourite_show_hours} hours!")



time.sleep(2)
if st.button("Top Five"):
    st.subheader("Let's have a look at your top five shows")
    time.sleep(2)
    fig = total_plot(top_five_shows)
    st.plotly_chart(figure_or_data=fig)

time.sleep(2)
if st.button("Countries"):
    st.header("You travelled the world and bought Netflix with you...")
    time.sleep(1)
    fig = country_plot(countries)
    st.plotly_chart(figure_or_data=fig)



#First step:
#variables
# hours_watched = total_hours_watched(data, user, year)
# top_five_shows = top_five(data,user=user, year=year)

# st.subheader(f"{user} you watched over")
# st.header(hours_watched)
# st.subheader("That's a lot of TV!")

# st.header(f"{user}, let's have a look at some of your favourite shows from {year}")
# st.plotly_chart(x=data["Title (clean)"], y=data["Duration (hours)"])

# if data is not None:
#     try:
#         st.write(top_five(data, user=user, year=year))
#     except:
#         st.text(f"Summarising {year} for {user}...")


#     data = pd.read_csv(data)
#     st.write(data.head())

# if data





# if uploaded_f is not None:
#     @st.cache_data()
#     def get_data():
#         uploaded_file = uploaded_f
#         return uploaded_file
