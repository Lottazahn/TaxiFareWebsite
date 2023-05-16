import streamlit as st
import requests

st.title("What should I cook today?")

# What do we see?
name = st.text_input("Any idea?", value="cake")
tags = st.text_input("Any specific requirement?", value="keto")
includeIngredients = st.text_input("Which ingredient must be included?", value="egg")
maxCalories = st.number_input("How many calories should it max have?", value=500)
maxPrepareTime = st.number_input("How much time do I have (in minutes)?", value=20)

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
	
#	response = requests.get(url, headers=headers, params=querystring)
#	tags_special = response.json()[0]["tags"]
#	tags_special = response.json()[0]["tags"]
	
#	st.write("Special requirements: ",tags_special)

	response = requests.get(url, headers=headers, params=querystring)
	response_name = response.json()[0]["name"]
	image_url = response.json()[0]["image"]
	max_PrepareTime = response.json()[0]["prepareTime"]
	cookTime = response.json()[0]["cookTime"]
	servings = response.json()[0]["servings"]
	description = response.json()[0]["description"]
	maxCalories = response.json()[0]["nutrients"]
     
	
	st.write(response_name, " | ", servings, " servings")
	st.image(image_url,width = 400)
	st.write("Cooking Time: ",cookTime)
	st.write("Preparation Time: ",maxPrepareTime)
	st.write("Details: ",description)
	st.write("Steps:")
	for x in range(len(response.json()[0]["steps"])):
		steps_details = response.json()[0]["steps"][x]
		st.write("-", steps_details)
	
	st.write("Ingredients:")
	for x in range(len(response.json()[0]["ingredients"])):
		ingredient_name = response.json()[0]["ingredients"][x]["name"]
		st.write("-",ingredient_name)
	
	line = ", ".join("nutrients")
	st.write(line)
	
		
		
			
	
	


       
