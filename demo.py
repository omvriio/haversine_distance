import streamlit as st
import math
from time import sleep

st.title("Distance Calculator")
st.write("Welcome to the Distance Calculator")
st.write("This app is using the Haversine formula to calculate the distance between two points on the map")

morrocan_cities=["Meknes","Oued Zem","Ouarzazate","Rabat","Casablanca","Fes","Tanger","Agadir","Marrakech","Essaouira","El Jadida","Tetouan","Nador","Al Hoceima","Laayoune","Dakhla","Taza","Khenifra","Beni Mellal","Safi","El Kelaa des Sraghna","Tiznit","Larache","Khouribga","Settat","Berrechid","Taourirt","Berkane","Sidi Kacem","Sidi Slimane","Errachidia","Guelmim","Tiflet","Lagouira","Sidi Ifni","Tiznit","Tata","Boujdour","Figuig","Guercif","Midelt","Ouezzane","Sefrou","Azrou","Youssoufia","Sidi Bennour","Skhirat","Oulad Teima","Tiflet","Larache","Khouribga","Settat","Berrechid","Taourirt","Berkane","Sidi Kacem","Sidi Slimane","Errachidia","Guelmim","Tiflet","Lagouira","Sidi Ifni","Tiznit","Tata","Boujdour","Figuig","Guercif","Midelt","Ouezzane","Sefrou","Azrou","Youssoufia","Sidi Bennour","Skhirat","Oulad Teima","Tiflet","Larache","Khouribga","Settat","Berrechid","Taourirt","Berkane","Sidi Kacem","Sidi Slimane","Errachidia","Guelmim","Tiflet","Lagouira","Sidi Ifni","Tiznit","Tata","Boujdour","Figuig","Guercif","Midelt","Ouezzane","Sefrou","Azrou","Youssoufia","Sidi Bennour","Skhirat","Oulad Teima","Tiflet","Larache","Khouribga","Settat","Berrechid","Taourirt","Berkane","Sidi Kacem","Sidi Slimane","Errachidia","Guelmim"]
#add - if no city is selected
morrocan_cities.insert(0, "-")
selected_city1 = st.selectbox("mdina 1", morrocan_cities)
selected_city2 = st.selectbox("mdina 2", morrocan_cities)



# Haversine formula
def haversine(lon1, lat1, lon2, lat2):
    R = 6371  # radius of the earth in km
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# Coordinates of the cities
cities = {
    "Meknes": [5.5313, 33.8869],
    "Oued Zem": [6.5592, 32.8629],
    "Ouarzazate": [6.9104, 30.4202],
    "Rabat": [-6.8498, 34.0209],
    "Casablanca": [-7.5898, 33.5731],
    "Fes": [-4.9786, 34.0181],
    "Tanger": [-5.9290, 35.7595],
    "Agadir": [-9.5981, 30.4220],
    "Marrakech": [-8.0083, 31.6295],
    "Essaouira": [-9.7658, 31.5085],
    "El Jadida": [-8.5068, 33.2336],
    "Tetouan": [-5.3698, 35.5706],
    "Nador": [-2.9287, 35.1740],
    "Al Hoceima": [-3.9306, 35.2451],
    "Laayoune": [-13.1950, 27.1547],
    "Dakhla": [-15.9390, 23.6848],
    "Taza": [-4.0119, 34.2190],
    "Khenifra": [-5.6667, 32.9359],
    "Beni Mellal": [-6.3553, 32.3342],
    "Safi": [-9.2265, 32.2994],
    "El Kelaa des Sraghna": [-7.5866, 32.0634],
    "Tiznit": [-9.7356, 29.6963],
    "Larache": [-5.8230, 35.1899],
    "Khouribga": [-6.9094, 32.8867],
    "Settat": [-7.6162, 33.0021],
    "Berrechid": [-7.6188, 33.2670],
    "Taourirt": [-2.8790, 34.4078],
    "Guelmim": [-10.0734, 28.9864],
    }

# Get the coordinates of the cities
if selected_city1 != "-" and selected_city2 != "-":
    st.write(f"Calculating distance between **{selected_city1}** and **{selected_city2}**")
    city1 = cities[selected_city1]
    city2 = cities[selected_city2]

    # Calculate the distance
    distance = haversine(city1[0], city1[1], city2[0], city2[1])

    #a box in streamlit to show distance with an animation
    with st.spinner('Wait for it...'):
        sleep(5)

    st.success(f"The distance between {selected_city1} and {selected_city2} is {distance:.2f} km")
    st.balloons()

