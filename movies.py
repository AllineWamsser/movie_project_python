from colorama import init, Fore
import random
import movie_storage

init(autoreset=True)

def menu():
    """Zeigt das Hauptmenü für die Filmbibliothek an."""
    print(Fore.GREEN + "----- Movie Library -----")
    print("1 - Show Movies")
    print("2 - Add Movie")
    print("3 - Delete Movie")
    print("4 - Update Movie")
    print("5 - Show Statistics")
    print("6 - Search Movies")
    print("7 - Sort Movies by Rating")
    print("8 - Suggest a Random Movie")
    print("0 - Exit")


def show_movies():
    """Zeigt alle verfügbaren Filme mit Bewertung und Erscheinungsjahr."""
    movies = movie_storage.get_movies()
    print(Fore.CYAN + "----- Available Movies -----")
    for title, info in movies.items():
        print(f"{title}: {info['rating']} ({info['year']})")


def add_movies():
    """Ermöglicht dem Benutzer, einen Film mit Bewertung und Jahr hinzuzufügen."""

    movies = movie_storage.get_movies()
    title = input("Enter a movie title: ")
    if title in movies:
        print(Fore.CYAN + "This movie already exists.")
        return
    #Rating loop: loop bis richtige value.
    while True:
      try:
          rating = float(input("Enter a rating (0 - 10.0): ").strip())
          if 0 <= rating <= 10:
              break
          else:
            print(Fore.RED + "Rating must be between 0 and 10.")

      except ValueError:
          print(Fore.RED + "Invalid input. Please enter numbers only.")
        
    #year loop: loop bis richtige value.
    while True:
      try:
          year = int(input("Enter a year (Format: XXXX):").strip())
          if 1800 <= year <= 2100:
              break

          else:
            print(Fore.RED + "Enter a realistic year (eg. 1994, 2020.)") 

      except ValueError:
          print(Fore.RED + "Invalid input. Please enter a valid year")
          
    movie_storage.add_movie(title, year, rating)
    print(Fore.GREEN + f"{title} added successfully!")
       

def delete_movies():
    """Ermöglicht dem Benutzer, einen Film aus der Liste zu löschen."""

    movies = movie_storage.get_movies()
    #Rating loop: loop bis richtige value.
    while True:
        title = input("Enter the movie you want to remove (or type 'cancel'): ")
        if title.lower() == "cancel":
            print(Fore.CYAN + "Cancelled.")
            break
        elif title in movies:
            movie_storage.delete_movie(title)
            print(Fore.GREEN + f"{title} removed.")
            break
        else:
            print(Fore.RED + "Title not found.")


def update_movies():
    """Aktualisiert die Bewertung eines vorhandenen Films."""

    movies = movie_storage.get_movies()
    title = input("Enter the movie you want to update: ")
    if title in movies:
      while True:
        try:
            new_rating = float(input("Enter a new rating: "))
            if 0 <= new_rating <= 10:
                movie_storage.update_movie(title, new_rating)
                print(Fore.GREEN + f"{title} rating updated to {new_rating}")
                break
            else:
                print(Fore.RED + "Rating must be between 0 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid input.")
    else:
        print(Fore.RED + "Movie not found!")


def stats():
    """Zeigt Durchschnitt, besten und schlechtesten Film."""
    movies = movie_storage.get_movies()
    if movies:
        ratings = [info["rating"] for info in movies.values()]
        avg = sum(ratings) / len(ratings)
        best = max(movies, key=lambda x: movies[x]["rating"])
        worst = min(movies, key=lambda x: movies[x]["rating"])
        print(Fore.YELLOW + f"Average: {avg:.2f}")
        print(Fore.YELLOW + f"Best: {best} ({movies[best]['rating']}) ({movies[best]['year']})")
        print(Fore.YELLOW + f"Worst: {worst} ({movies[worst]['rating']}) ({movies[worst]['year']})")
    else:
        print(Fore.YELLOW + "No movies to show statistics.")


def search_movies():
    """Durchsucht die Liste nach einem Film basierend auf Benutzereingabe."""
    movies = movie_storage.get_movies()
    search = input("Enter a movie: ").lower()
    found = False
    for title, info in movies.items():
        if search in title.lower():
            print(Fore.CYAN + f"{title}: {info['rating']} ({info['year']})")
            found = True
    if not found:
        print(Fore.RED + "No movies found.")


def movie_sorted_by_rating():
    """Sortiert und zeigt die Filme nach Bewertung in absteigender Reihenfolge."""
    movies = movie_storage.get_movies()
    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True))
    print(Fore.CYAN + "------- Movies Sorted by Rating -------")
    for title, info in sorted_movies.items():
        print(Fore.BLUE + f"{title}: {info['rating']} ({info['year']})")


def random_movie():
    """Empfiehlt einen zufälligen Film aus der Liste."""
    movies = movie_storage.get_movies()
    if movies:
        title = random.choice(list(movies.keys()))
        print(Fore.MAGENTA + f"Suggested movie: {title} ({movies[title]['rating']}) ({movies[title]['year']})")
    else:
        print(Fore.RED + "No movies to choose from.")


def main():
    """Hauptfunktion: Verwaltet das Menü und die Programmlogik."""
    while True:
        menu()
        option = input("Choose an option: ")
        if option == "1":
            show_movies()
        elif option == "2":
            add_movies()
        elif option == "3":
            delete_movies()
        elif option == "4":
            update_movies()
        elif option == "5":
            stats()
        elif option == "6":
            search_movies()
        elif option == "7":
            movie_sorted_by_rating()
        elif option == "8":
            random_movie()
        elif option == "0":
            print(Fore.CYAN + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Try again.")


if __name__ == "__main__":
    main()