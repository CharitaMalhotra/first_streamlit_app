import streamlit
# streamlit.title("I got selected in my dream company-GOOGLE 🫶🥰")
streamlit.header("I got selected in my dream company-GOOGLE 🫶🥰")
streamlit.header("🇪🇺 PARIS IS BEAUTIFUL 🗼")
#########################################################################################################

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# we'll pre-populate the list to set an example for the customer. 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado","Lemon"])

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)

#########################################################################################################
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#########################################################################################################
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json()) # just writes the data to the screen

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

