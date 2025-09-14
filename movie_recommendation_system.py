import requests
import json
from collections import Counter

API_KEY = "your_api_key_here"  # Replace with your OMDb API key
HISTORY_FILE = "movies.json"

class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) | Genre: {self.genre} | Rating: {self.rating}"

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def search_movie(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url).json()
    if response.get("Response") == "True":
        movie = Movie(
            response["Title"],
            response["Year"],
            response["Genre"],
            response["imdbRating"]
        )
        return movie
    else:
        print("Movie not found!")
        return None

def show_top_searches(history, n=5):
    counter = Counter(history)
    top = counter.most_common(n)
    print("\nTop Searches:")
    for movie, count in top:
        print(f"{movie} ({count} times)")

def main():
    history = load_history()

    while True:
        print("\n1. Search Movie\n2. Show Top 5 Searches\n3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Enter movie title: ")
            movie = search_movie(title)
            if movie:
                print(movie)
                history.append(movie.title)
                save_history(history)

        elif choice == "2":
            show_top_searches(history)

        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()