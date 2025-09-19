## Movie Library CLI Application

This is a command-line interface (CLI) application for managing a personal movie library. The program allows users to perform various operations such as adding, deleting, updating, and viewing movies, as well as generating statistics and searching the collection.
The application is built in Python and uses a local JSON file to persist the movie data.

# Features

Show Movies: Displays all movies in the library with their ratings and years.

* Add Movie: Prompts the user to add a new movie with a title, year, and rating, including input validation.
* Delete Movie: Removes a specific movie from the library.
* Update Movie: Modifies the rating of an existing movie.
* Show Statistics: Calculates and displays key metrics such as the average rating, and the best and worst-rated movies.
* Search Movies: Searches the library for movies by a keyword in the title.
* Sort Movies: Displays all movies sorted by their rating in descending order.
* Random Suggestion: Recommends a random movie from the library.

# Project Structure

* movies.py: The main script that contains the menu logic and all the core application functions.
* movie_storage.py: A separate module responsible for handling data persistence (reading from and writing to the data.json file).
* data.json: The file where all movie information is stored.
