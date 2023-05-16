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

querystring = {"name":f"{cake}","tags":f"{keto;dairy-free}","includeIngredients":f"{egg;butter}","excludeIngredients":f"{cinnamon}","maxPrepareTime":"10","maxCookTime":"20","maxCalories":"500","maxNetCarbs":"5","maxSugar":"3","maxAddedSugar":"0","limit":"10"}

headers = {
	"X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
	"X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
name = response.json()["result"][0]["name"]
tags = response.json()["result"][0]["tags"]
description = response.json()["result"][0]["description"]
maxPrepareTime = response.json()["result"][0]["maxPrepareTime"]
cookTime = response.json()["result"][0]["cookTime"]
includeIngredients = response.json()["result"][0]["includeIngredients"]
steps = response.json()["result"][0]["steps"]
servings = response.json()["result"][0]["servings"]
maxCalories = response.json()["result"][0]["maxCalories"]

st.write(name)
st.write("Special requirements: ",tags)
st.write("Details: ",description)
st.write("Preparation Time: ",maxPrepareTime)
st.write("Cooking Time: ",cookTime)
st.write("Steps: ",steps)
st.write("Servings: ",servings)
st.write("Calories: ",maxCalories)

       
