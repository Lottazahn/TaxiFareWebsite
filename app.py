import streamlit as st
import requests

st.title("Recipe Finder")

# What do we see?
name = st.text_input("Any keyword?", value="tasty")
tags = st.text_input("Any specific requirement?", value="gluten-free")
includeIngredients = st.text_input("Which ingredient should be included?", value="tomatoes")
maxCalories = st.number_input("How many calories should it max have?", value=100)
maxPrepareTime = st.number_input("How much time do you have (in minutes)?", value=50)

# Button
if st.button('Search'):
    url = "https://low-carb-recipes.p.rapidapi.com/search"

    querystring = querystring = {"name":"cake","tags":"keto;dairy-free","includeIngredients":"egg;butter","excludeIngredients":"cinnamon","maxPrepareTime":"10","maxCookTime":"20","maxCalories":"500","maxNetCarbs":"5","maxSugar":"3","maxAddedSugar":"0","limit":"10"}


    headers = {
        "X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
        "X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.ok:
        recipes = response.json().get("result", [])
        if recipes:
            for recipe in recipes:
                recipe_name = recipe["name"]
                recipe_tags = recipe["tags"]
                st.write("Recipe Name: ", recipe_name)
                st.write("Tags: ", recipe_tags)
                st.write("---")
        else:
            st.write("No recipes found.")
    else:
        st.write("Error occurred while fetching recipes.")
