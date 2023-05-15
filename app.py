
import streamlit as st
import requests

'''
# Recipe Finder
'''

# What do we see?
ingredient = st.text_input("Which ingredient would you like to use?", value="vodka")

# Button
if st.button('Search'):
    url = "https://the-cocktail-db.p.rapidapi.com/search.php"

    # API
    # Enter here the address of your Flask API
    querystring = {"s": f"{ingredient}"}

    headers = {
        "X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
        "X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
