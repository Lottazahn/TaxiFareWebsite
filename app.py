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
    data = response.json()

    # Display cocktail details
    if 'drinks' in data:
        for drink in data['drinks']:
            drink_name = drink['strDrink']
            drink_image = drink['strDrinkThumb']

            # Display cocktail name
            st.write(f"Cocktail Name: {drink_name}")

            # Display cocktail image
            st.image(drink_image, caption=drink_name, use_column_width=True)
    else:
        st.write("No cocktails found for the given ingredient.")
