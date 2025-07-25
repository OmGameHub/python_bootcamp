"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os
import json

FILE_NAME = "movies.json"

def load_movies():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_movies(movies):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=2)

def add_movie(movies):
    title = input("Enter movie title: ").strip()

    if any(movie["title"].lower() == title.lower() for movie in movies):
        print("Movie already exists!")
        return
    
    genre = input("Enter movie genre: ").strip().lower()
    
    try:
        rating = float(input("Enter movie rating (0-10): "))
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10.")
    except ValueError as e:
        print(f"Invalid rating: {e}")
        return
    
    movies.append({ "title": title, "genre": genre, "rating": rating })
    save_movies(movies)
    
def search_movies(movies):
    query = input("Enter title or genre to search: ").strip().lower()

    results = [movie for movie in movies if query in movie["title"].lower() or query in movie["genre"].lower()]

    if not results:
        print("No movies found.")
        return
    
    print("\nFound Movies:")
    print("-" * 60)
    for movie in results:
        print(f"Title: {movie["title"]} -- Genre: {movie["genre"]} -- Rating: {movie["rating"]}")
    print("-" * 60)

def view_all_movies(movies):
    if not movies:
        print("No movies in the database.")
        return
    
    print("\nAll Movies:")
    print("-" * 60)
    print(f"{"Title"} {"Genre"} {"Rating"}")
    print("-" * 60)
    
    for movie in movies:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")

def main():
    movies = load_movies()

    while True:
        print("\nPersonal Movie Tracker")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movies")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case "1": add_movie(movies)
            case "2": view_all_movies(movies)
            case "3": search_movies(movies)
            case "4": print("Exiting..."); break
            case _: print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
