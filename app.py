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

querystring = {"name":"cake","tags":"keto;dairy-free","includeIngredients":"egg;butter","excludeIngredients":"cinnamon","maxPrepareTime":"10","maxCookTime":"20","maxCalories":"500","maxNetCarbs":"5","maxSugar":"3","maxAddedSugar":"0","limit":"10"}

headers = {
	"X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
	"X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
if response.ok:
        recipe_data = response.json().get("result")
        if recipe_data and len(recipe_data) > 0:
            recipe = recipe_data[0]
            name = recipe.get("name")
            tags = recipe.get("tags")
            description = recipe.get("description")
            prepareTime = recipe.get("prepareTime")
            cookTime = recipe.get("cookTime")
            ingredients = recipe.get("ingredients")
            steps = recipe.get("steps")
            servings = recipe.get("servings")
            nutrients = recipe.get("nutrients")

            st.write("Name:", name)
            st.write("Special requirements:", tags)
            st.write("Description:", description)
            st.write("Preparation Time:", prepareTime)
            st.write("Cooking Time:", cookTime)
            st.write("Ingredients:", ingredients)
            st.write("Steps:", steps)
            st.write("Servings:", servings)
            st.write("Nutrients:", nutrients)
        else:
            st.write("No recipes found.")
    else:
        st.write("Error occurred while fetching recipes.")
       
