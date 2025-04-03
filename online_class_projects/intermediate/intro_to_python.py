# mars_multiple = 0.378
# MERCURY_GRAVITY = 0.376 
# VENUS_GRAVITY = 0.889 
# MARS_GRAVITY = 0.378 
# JUPITER_GRAVITY = 2.36 
# SATURN_GRAVITY = 1.081 
# URANUS_GRAVITY = 0.815 
# NEPTUNE_GRAVITY = 1.14 
# EARTH_GRAVITY = 1.0
# def main():
#     earth_weight = float(input("Enter a weight on earth."))
#     mars_weight = earth_weight * mars_multiple
#     rounded_mars_weight = round(mars_weight,2)
#     print(f"The equivalent weight on Mars is {rounded_mars_weight}")
    
    
#     planet = input("Enter a planet name: ").lower()
    
#     if planet == "mercury":
#         gravity_constant = MERCURY_GRAVITY
#     elif planet == "venus":
#         gravity_constant = VENUS_GRAVITY
#     elif planet == "mars":
#         gravity_constant = MARS_GRAVITY
#     elif planet == "jupiter":
#         gravity_constant = JUPITER_GRAVITY
#     elif planet == "saturn":
#         gravity_constant = SATURN_GRAVITY
#     elif planet == "earth":
#         gravity_constant = EARTH_GRAVITY    
#     elif planet == "uranus":
#         gravity_constant = URANUS_GRAVITY
#     else:
#         gravity_constant = NEPTUNE_GRAVITY  
    
#     planetary_weight = earth_weight_str * gravity_constant 
#     rounded_planetary_weight = round(planetary_weight, 2)
    
#     print(f"The equivalent weight of planet {planet} is {rounded_planetary_weight}")                         
    
    
    
# if __name__ == "__main__":
#     main()   

# Gravity constants for different planets
MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def main():
    # Get weight input from user
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Mars weight calculation
    mars_weight = earth_weight * MARS_GRAVITY
    rounded_mars_weight = round(mars_weight, 2)
    print(f"The equivalent weight on Mars is {rounded_mars_weight} kg.")
    
    # Get planet input from user
    planet = input("Enter a planet name: ").lower()
    
    # Gravity dictionary for planets
    planet_gravity = {
        "mercury": MERCURY_GRAVITY,
        "venus": VENUS_GRAVITY,
        "mars": MARS_GRAVITY,
        "jupiter": JUPITER_GRAVITY,
        "saturn": SATURN_GRAVITY,
        "uranus": URANUS_GRAVITY,
        "neptune": NEPTUNE_GRAVITY,
        "earth": EARTH_GRAVITY
    }
    
    # Check if the entered planet exists
    if planet in planet_gravity:
        gravity_constant = planet_gravity[planet]
        planetary_weight = earth_weight * gravity_constant
        rounded_planetary_weight = round(planetary_weight, 2)
        print(f"The equivalent weight on {planet.capitalize()} is {rounded_planetary_weight} kg.")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
    