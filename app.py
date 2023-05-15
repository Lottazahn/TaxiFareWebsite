import streamlit as st
import requests

st.title("Recipe Finder")

# What do we see?
meal = st.text_input("Which meal do you eat?", value="pizza margherita")

# Button
if st.button('Search'):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients"
    
    # API
    # Enter here the address of your Flask API
    querystring = {"limitLicense":"false","minProtein":"0","minVitaminC":"0","minSelenium":"0","maxFluoride":"50","maxVitaminB5":"50","maxVitaminB3":"50","maxIodine":"50","minCarbs":"0","maxCalories":"250","minAlcohol":"0","maxCopper":"50","maxCholine":"50","maxVitaminB6":"50","minIron":"0","maxManganese":"50","minSodium":"0","minSugar":"0","maxFat":"20","minCholine":"0","maxVitaminC":"50","maxVitaminB2":"50","minVitaminB12":"0","maxFolicAcid":"50","minZinc":"0","offset":"0","maxProtein":"100","minCalories":"0","minCaffeine":"0","minVitaminD":"0","maxVitaminE":"50","minVitaminB2":"0","minFiber":"0","minFolate":"0","minManganese":"0","maxPotassium":"50","maxSugar":"50","maxCaffeine":"50","maxCholesterol":"50","maxSaturatedFat":"50","minVitaminB3":"0","maxFiber":"50","maxPhosphorus":"50","minPotassium":"0","maxSelenium":"50","maxCarbs":"100","minCalcium":"0","minCholesterol":"0","minFluoride":"0","maxVitaminD":"50","maxVitaminB12":"50","minIodine":"0","maxZinc":"50","minSaturatedFat":"0","minVitaminB1":"0","maxFolate":"50","minFolicAcid":"0","maxMagnesium":"50","minVitaminK":"0","maxSodium":"50","maxAlcohol":"50","maxCalcium":"50","maxVitaminA":"50","maxVitaminK":"50","minVitaminB5":"0","maxIron":"50","minCopper":"0","maxVitaminB1":"50","number":"10","minVitaminA":"0","minPhosphorus":"0","minVitaminB6":"0","minFat":"5","minVitaminE":"0"}

    headers = {"X-RapidAPI-Key": "a1cbd55fa4msh4fe6d0f423ccb9ep1066a8jsna6b685db9cc1",
               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"}
        
    response = requests.get(url, headers=headers, params=querystring)
    title = response.json()["result"][0]["title"]
    calories = response.json()["result][0]["calories"]
    protein = response.json()["result"][0]["protein"]
    fat = response.json()["result"][0]["fat"]
    gram = response.json()["result"][0]["gram"]                           
                               
    st.image(posterURLs,width = 400)
    st.write(title, "|" ,gram)
    st.write("calories:",calories)
    st.write("protein:",protein)
    st.write("fat:",fat)                           
    

    
