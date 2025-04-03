# import requests
# from pprint import pprint

# API_KEY = '5dc131944ad39d41285744613c354a94'
# city = input("Enter city name: ")
# basee_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city + "&units=metric"
# weather_data = requests.get(basee_url).json()
# pprint(weather_data)




import requests
import streamlit as st

# Set Streamlit page config
st.set_page_config(page_title="Weather App", page_icon="🌤️")

# App title
st.title("🌍 Live Weather App")

# Input field for city name
city = st.text_input("🔍 Enter City Name", "Karachi")

# API Key & URL
API_KEY = '5dc131944ad39d41285744613c354a94'
base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}&units=metric"

# Fetch Weather Data
if st.button("Get Weather 🌡"):
    response = requests.get(base_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        # Extracting required info
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_desc = weather_data["weather"][0]["description"].title()
        wind_speed = weather_data["wind"]["speed"]
        country = weather_data["sys"]["country"]

        # Displaying Data in a Stylish Format
        st.success(f"📍 **Location:** {city}, {country}")
        st.metric(label="🌡 Temperature", value=f"{temp}°C")
        st.metric(label="💧 Humidity", value=f"{humidity}%")
        st.metric(label="🌬 Wind Speed", value=f"{wind_speed} m/s")
        st.info(f"🌤 **Weather Condition:** {weather_desc}")
    
    else:
        st.error("⚠️ Invalid City Name! Please enter a valid city.")

