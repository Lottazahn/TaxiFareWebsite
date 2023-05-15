import streamlit as st
import requests

st.title("Recipe Finder")

# What do we see?
meal = st.text_input("Which meal do you eat?", value="pizza margherita")

# Button
if st.button('Search'):
    url = "https://low-carb-recipes.p.rapidapi.com/search"
    
    # API
    # Enter here the address of your Flask API
    querystring = {"name":"cake","tags":"keto;dairy-free","includeIngredients":"egg;butter","excludeIngredients":"cinnamon","maxPrepareTime":"10","maxCookTime":"20","maxCalories":"500","maxNetCarbs":"5","maxSugar":"3","maxAddedSugar":"0","limit":"10"}
    

    headers = {
	"X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
	"X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
}
        
    response = requests.get(url, headers=headers, params=querystring)
    name = response.json()["result"][0]["name"]	

st.write(name)


    
