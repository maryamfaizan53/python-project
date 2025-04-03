import requests
import streamlit as st

# Function to fetch country data
def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:  # Ensuring the response is a valid list
            country_data = data[0]

            # Extracting required details safely
            name = country_data["name"]["common"]
            capital = country_data.get("capital", ["N/A"])[0]  # Ensures no KeyError
            population = country_data.get("population", "N/A")
            area = country_data.get("area", "N/A")
            region = country_data.get("region", "N/A")
            
            # Formatting currency display
            currencies = country_data.get("currencies", {})
            currency_info = ", ".join(
                [f"{currencies[c]['name']} ({currencies[c].get('symbol', 'N/A')})" for c in currencies]
            ) if currencies else "N/A"

            return name, capital, population, area, currency_info, region
    return None

# Streamlit app
def main():
    # Page title with emoji
    st.markdown("<h1 style='text-align: center; color: #FF5733;'>🌍 Country Information App 🏛️</h1>", unsafe_allow_html=True)
    st.write("🔎 **Enter a country name to discover fun facts about it!**")

    # User input
    country_name = st.text_input("🌎 Type a country name:", "").strip()

    # Add a fun button
    if st.button("🔍 Find Info"):
        if country_name:
            country_info = fetch_country_data(country_name)
            
            if country_info:
                name, capital, population, area, currency, region = country_info

                # Displaying results with enhanced UI
                st.markdown(f"<h2 style='color: #4CAF50;'>📌 {name}</h2>", unsafe_allow_html=True)
                st.write(f"🏛️ **Capital:** `{capital}`")
                st.write(f"👥 **Population:** `{population:,}`")
                st.write(f"🌍 **Region:** `{region}`")
                st.write(f"📏 **Area:** `{area:,} km²`")
                st.write(f"💰 **Currency:** `{currency}`")

                # Cool Success Message
                st.success(f"🎉 Yay! You discovered facts about {name}! 🎉")
            else:
                st.error("❌ Country not found. Please try again! 🌎")
        else:
            st.warning("⚠️ Please enter a country name first.")

if __name__ == "__main__":
    main()
