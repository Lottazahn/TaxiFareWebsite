import streamlit as st
import requests

st.title("What do I want to eat?")

# What do we see?
name = st.text_input("Any idea?", value="tasty")
tags = st.text_input("Any specific requirement?", value="gluten-free")
includeIngredients = st.text_input("Which ingredient must be included?", value="tomatoes")
maxCalories = st.number_input("How many calories should it max have?", value=100)
maxPrepareTime = st.number_input("How much time do I have (in minutes)?", value=50)

# Button
if st.button('Search'):
	url = "https://low-carb-recipes.p.rapidapi.com/search"

	querystring = {"name":f"{name}",
		       "tags":f"{tags}",
		       "includeIngredients":f"{includeIngredients}",
		       "maxPrepareTime":f"{maxPrepareTime}",
		       "maxCalories":f"{maxCalories}"}

	headers = {
		"X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
		"X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
	}
	
#	response = requests.get(url, headers=headers, params=querystring)
#	st.write(response.json())
	
	response = requests.get(url, headers=headers, params=querystring)
	tags_special = response.json()[0]
	
	st.write(response_name)
	st.write("Special requirements: ",tags_special)

       
