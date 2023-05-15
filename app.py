
import streamlit as st

import datetime

import requests

'''
# Recipe Finder


-- what do we see?
ingredient = st.text_input ("Which ingredient would you like to use?",value="vodka")

-- button
if st.button('Search'):

-- API
# enter here the address of your flask api

querystring = {"s":"vodka"}

headers = {
	"X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


