
"Guess the Country" is a basic guessing game made using Python. The objective is to guess the country based on its silhouette. Players have a total of 5 guesses. After each incorrect guess, a hint is provided, indicating the direction and distance (calculated using the Pythagorean theorem) from the guessed country to the target country. Note: The game uses the Mercator projection, so distances are measured as if on a flat surface, not taking the Earth's curvature into account (as would be done with the Haversine formula).

data.py: Contains the countries' data.
main.py: The beta terminal version of the game.
game.py: The main game with a graphical user interface (GUI).
