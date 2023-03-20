"""Restaurant rating lister."""


def process_scores():
    """Read from the scores.txt file and returns dictionary of {restaurant-name:score}"""

    scores_txt = open('scores.txt')
    scores = {}

    for line in scores_txt:
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores

def add_restaurant(scores):
    """Allows user to add a restaurant and rating"""

    print("Please add a rating for your favorite restaurant!")
    restaurant = input("Name of restaurant > ")
    rating = int(input("Rating > "))

    scores[restaurant] = rating

def print_sorted_scores(scores):
    """Prints restaurants and ratings, sorted"""

    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

# Reads existing scores in from scores.txt file
scores = process_scores()

# Allows user to add a restaurant/rating pair
add_restaurant(scores)

# Prints an alphabetical list of all rated restaurants and their ratings
print_sorted_scores(scores)
