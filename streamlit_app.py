import streamlit
streamlit.title('My parents healthy new diner')
streamlit.header('breakfast favorites')
streamlit.text('🍔 Omega 3 & blueberry oatmeal')
streamlit.text('🌯	Kale,Spinach & rocket Smoothie')
streamlit.text('🥗	Hard-Boiled Free -Range Egg')

streamlit.header('🍜build your own fruit smoothie🍝')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)['Avocado','Strawberries'])
