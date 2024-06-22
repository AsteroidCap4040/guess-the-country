#Importing Libraries
import tkinter as tk
from PIL import Image, ImageTk #Library for image set up
from data import countries
import random
import math

#Game Constannts
number_of_guesses = 5
latitude = 111  # Distance between two latitudes in km
longitude = 111  # Distance between two longitudes in km
is_game_running = True
BACKGROUND_COLOR = "black"
FONT_COLOR = "white"

#Randomly picking a country from data.py
country_name, country_info_1 = random.choice(list(countries.items()))

#Creating the image variable that contains file path of country's image
IMAGE = Image.open(country_info_1["image"])

#Checking if the country is correct or not
def check_country():
    global number_of_guesses, is_game_running 

    #Stopping the game if the boolean is false
    if not is_game_running:
        return

    #Lowering the cases of the inputed text
    country_text = country_guess.get().strip().lower()

    #Creating the list of countries from data.py
    country_list = list(countries.keys())

    #Game over sequence if yo ran out of guesses
    if number_of_guesses == 0:
        answer_label.config(text=f"Game over!!! You ran out of chances. The country was {country_name}.")
        is_game_running = False
    
    #Name error recognizer
    # <----------------  Note: Even if the country name is correct but it not present in data.py, the error will be raised ------------->
    elif country_text not in country_list:
        answer_label.config(text="Please enter a correct country name.")

    #Telling the user if thier guess is correct or not
    else:
        #Collecting the inputed countries info from the data.py
        country_info_2 = countries.get(country_text)

        #Getting Horizontal and Vertical distance from the two co-ordinates
        x_distance = country_info_1["longitude"] - country_info_2["longitude"]
        y_distance = country_info_1["latitude"] - country_info_2["latitude"]

        # <-------------- Note: The distance is based on mercator projection so the distance won't be accurate, as mercator is flat earth projection !!!! ---------------->
        #Multiplying with longitudes and latitudes contants
        x_kilometer = x_distance * longitude
        y_kilometer = y_distance * latitude

        #Getting the using Pythagoras theorem <----------  No Haversine formula (Used to calculate spherical distance) ---------------->
        distance = math.sqrt(x_kilometer**2 + y_kilometer**2)

        #Locating the direction of the questioned country from the guessed country
        if y_distance > 0 and x_distance > 0:
            direction = "north-east"
        elif y_distance > 0 and x_distance < 0:
            direction = "north-west"
        elif y_distance < 0 and x_distance > 0:
            direction = "south-east"
        elif y_distance < 0 and x_distance < 0:
            direction = "south-west"
        else:
            direction = "unknown"

        #Showing the user a well done message, if they guessed it correctly
        if country_text == country_name.lower():
            answer_label.config(text=f"Well done, {country_text} was the country!")
            is_game_running = False
        
        #Giving them a hint after their every guess
        else:
            number_of_guesses -= 1 #Decreasing the number of guesses after every guess
            answer_label.config(text=f"Look {direction} at a distance of {distance:.2f} km. {number_of_guesses} guesses remaining.")

            #Running out of guesses sequence
            if number_of_guesses == 0:
                answer_label.config(text=f"Game over!!! You ran out of chances. The country was {country_name}.")
                is_game_running = False

#Creating a Screen
window = tk.Tk()
window.minsize(700, 700)
window.maxsize(800, 800)
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
window.title("Guess the Country Through Silhouette")

#Displaying the random country's image
country_image = ImageTk.PhotoImage(IMAGE)
canvas = tk.Canvas(width=450, height=450, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(225, 225, image=country_image)
canvas.grid(column=1, row=0) #Placing them using grid system

#Title Label
question_label = tk.Label(text="Guess the country??")
question_label.config(font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
question_label.grid(column=1, row=1)

#User Input Field
country_guess = tk.Entry()
country_guess.config(width=100)
country_guess.grid(column=1, row=2, padx=10, pady=10)

#Button Field to check the input field
check_button = tk.Button(text="Check", command=check_country)
check_button.grid(column=1, row=3, padx=10, pady=10)

#Hint or Game Over Message
answer_label = tk.Label(text=f"Guesses Remaining: {number_of_guesses}")
answer_label.config(font=("Arial", 15, "bold"), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
answer_label.grid(column=1, row=4, padx=10, pady=10)

window.mainloop() #Main Screen Exit
