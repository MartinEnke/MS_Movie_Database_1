"""
This program manages a dictionary of movies and their ratings.
It serves as a "Movie Database," offering features such as
listing, adding, deleting, updating, viewing statistics,
random selection, searching, and sorting by rating.
It also provides the option to create a histogram of all ratings.
To enhance the visual experience, various colors have been applied.
"""

import random
import matplotlib.pyplot as plt

def color_text(text, color_code):
    # Applies an ANSI color code to the given text.
    return f"\033[{color_code}m{text}\033[0m"

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def display_menu():
    menu_text = """ 
Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create Rating Histogram
"""
    print(color_text(menu_text, BLUE))


def user_choice(movies):
    choice = input(color_text("Enter choice (1-9): ", BLUE))
    if choice == "1":
        print(color_text(f"{len(movies)} movies in total", GREEN))
        list_movies(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "2":
        add_movie(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "3":
        del_movie(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "4":
        update_movie(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "5":
        stats(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "6":
        random_movie(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "7":
        search_movie(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "8":
        movies_sorted_by_rating(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "9":
        rating_histogram(movies)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    else:
        print(color_text("Invalid choice! Please enter a number between 1 and 8", RED))
        input(color_text("Press Enter to continue", YELLOW))


def get_movie_name():
    movie = input(color_text("Enter movie name: ", BLUE)).title()
    return movie


def get_movie_rating():
    while True:
        rating = input(color_text("Enter movie rating (0-10): ", BLUE)).replace(",", ".")
        if rating.replace(".", "").isdigit():
            rating = float(rating)
            if 0.0 <= rating <= 10.0:
                return rating
            else:
                print(color_text("Rating must be between 0 and 10", RED))
        else:
            print(color_text("Invalid input. Please enter numeric value", RED))


def list_movies(movies):
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie(movies):
    movie = get_movie_name()
    if movie in movies:
        print(color_text(f"Movie '{movie}' already exists", RED))
        return
    rating = get_movie_rating()
    movies[movie] = rating
    print(color_text(f"Movie '{movie}' successfully added", GREEN))


def del_movie(movies):
    movie = get_movie_name()
    if movie in movies:
        del movies[movie]
        print(color_text(f"Movie '{movie}' successfully deleted", GREEN))
    else:
        print(color_text(f"Movie '{movie}' doesn't exist", RED))
        return


def update_movie(movies):
    movie = get_movie_name()
    if movie in movies:
        rating = get_movie_rating()
        movies[movie] = rating
        print(color_text(f"Movie '{movie}' successfully updated with rating {rating}", GREEN))

    else:
        print(color_text(f"Movie '{movie}' doesn't exist", RED))
        return


def stats(movies):
    """Average & median rating, best & worst movie(s) by rating"""
    ratings = sorted(movies.values())
    count = len(ratings)

    average_rating = sum(ratings) / count
    print(f"Average rating: {average_rating:.2f}")

    if count % 2 == 1:
        median_rating = ratings[count // 2]
    else:
        mid1 = ratings[count // 2 - 1]
        mid2 = ratings[count // 2]
        median_rating = (mid1 + mid2) / 2
    print(f"Median rating: {median_rating:.2f}")

    max_rating = max(movies.values())
    best_movies = []
    for movie, rating in movies.items():
        if rating == max_rating:
            best_movies.append(movie)
    print(f"Best movie(s) with rating: {max_rating}:")
    for movie in best_movies:
        print(color_text(f"- {movie}", GREEN))

    min_rating = min(movies.values())
    worst_movies = []
    for movie, rating in movies.items():
        if rating == min_rating:
            worst_movies.append(movie)
    print(f"Worst movie(s) with rating: {min_rating}:")
    for movie in worst_movies:
        print(color_text(f"- {movie}", GREEN))


import random

def random_movie(movies):
    movie = random.choice(list(movies.keys()))
    rating = movies[movie]
    print(color_text(f"Your movie for tonight: '{movie}', Rating: {rating}", GREEN))


def search_movie(movies):
    movie = get_movie_name().casefold()
    found = False
    for movies, ratings in movies.items():
        if movie in movies.casefold():
            # str-length: 3 char minimum
            if len(movie) > 2:
                print(color_text(f"- {movies}: {ratings}", GREEN))
                found = True
    if not found:
        print(color_text("No entry under this name", RED))


def movies_sorted_by_rating(movies):
    # dict conversion into two lists for movies & their ratings
    movie_names = list(movies.keys())
    movie_ratings = list(movies.values())

    for i in range(len(movie_ratings)):
        for j in range(i + 1, len(movie_ratings)):
            # Compare ratings
            if movie_ratings[i] < movie_ratings[j]:
                # Swap ratings - if lower rating first
                movie_ratings[i], movie_ratings[j] = movie_ratings[j], movie_ratings[i]
                # Swap corresponding movie names
                movie_names[i], movie_names[j] = movie_names[j], movie_names[i]

    for i in range(len(movie_names)):
        print(color_text(f"- {movie_names[i]}: {movie_ratings[i]}", GREEN))




def rating_histogram(movies):
    ratings = list(movies.values())  # extract ratings from dictionary

    # Create histogram
    plt.hist(ratings, bins=range(0, 11), edgecolor="yellow")  # Range 0-10 for ratings

    # labels and title
    plt.title('Movie Ratings Histogram')
    plt.ylabel('Frequency')
    plt.xlabel('Ratings')

    file_name = input(color_text("Enter filename to save histogram: ", BLUE))

    # Save plot to the file
    plt.savefig(file_name)
    print(color_text(f"Histogram successfully saved to '{file_name}'", GREEN))

    plt.show()


def main():
    print(color_text("\n********** MOVIE DATABASE **********", BLUE))

    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    while True:

        display_menu()
        user_choice(movies)
        print("")


if __name__ == "__main__":
    main()

