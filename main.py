from data import countries
import random
import math

number_of_guesses = 5
latitude = 111 #Distance between two latitudes in km
longitutde = 111 #Distance between two longitudes in km
is_game_running = True

country_1, location_1 = random.choice(list(countries.items()))


while True and number_of_guesses > 0:
    country_2 = input("Enter the country- ").lower()
    location_2 = countries.get(country_2)

    x_distance = location_1["longitude"] - location_2["longitude"]
    y_distance = location_1["latitude"] - location_2["latitude"]

    x_kilometer = x_distance * longitutde
    y_distance = y_distance * latitude

    distance = math.sqrt(x_kilometer**2 + y_distance**2)


    if y_distance > 0 and x_distance > 0:
        print(f"Look north-east at distance of {distance}")
        number_of_guesses -= 1
    elif y_distance > 0 and x_distance < 0:
        print(f"Look north-west at distance of {distance}")
        number_of_guesses -= 1
    elif y_distance < 0 and x_distance > 0:
        print(f"Look south-east at distance of {distance}")
        number_of_guesses -= 1
    elif y_distance < 0 and x_distance < 0:
        print(f"Look south-west at distance of {distance}")
        number_of_guesses -= 1
    else:
        print(f"Well done, {country_1} was the country")
        is_game_running = False

print("GAME OVER !!!")