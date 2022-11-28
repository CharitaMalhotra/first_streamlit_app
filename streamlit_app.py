import streamlit
# streamlit.title("I got selected in my dream company-GOOGLE 🫶🥰")
streamlit.header("I got selected in my dream company-GOOGLE 🫶🥰")
streamlit.header("🇪🇺 PARIS IS BEAUTIFUL 🗼")

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
