"""Restaurant rating lister."""
dt = {}
import random

def ratings(filename):
    file = open(filename)
    st = ""
    for line in file:
        name, rating = line.split(":")
        dt[name] = rating.rstrip()

    for k, v in sorted(dt.items(), key= lambda x: x[0].upper()): 
        st += f"{k} is rated at {v}\n"
    
    return st


def add_new():
    while True:
        rest = input("What's the restaurant name?")
        score = input("What's the restaurant rating? ")
        try:
            score = int(score)
            if 1 <= score <= 5:
                dt[rest] = str(score)
                break
            else:
                print("Please enter an integer between 1 and 5")
        except:
            print("Please enter a valid integer")
            continue
    
    return dt

def update_random(filename):
    ratings(filename)
    ls = []
    for k in dt.keys():
        ls.append(k)
    random_rest = random.choice(ls)
    print(f"{random_rest} is rated at {dt[random_rest]}")
    new_rating = input("What the new rating should be?")
    dt[random_rest] = new_rating


if __name__ == '__main__':
    request = input(
        "\nWhat would you like to do?\na. Seeing all the ratings \nb. Adding a new restaurant \nc. Updating a random restaurant's rating \nq. Quitting \nEnter your response: \n"
        )

    while request != 'q':
        if request == 'a':
            print(ratings('scores.txt'))
            request = input(
        "\nWhat would you like to do?\na. Seeing all the ratings \nb. Adding a new restaurant \nc. Updating a random restaurant's rating \nq. Quitting \nEnter your response: \n"
        )
        elif request == 'b':
            add_new()
            request = input(
        "\nWhat would you like to do?\na. Seeing all the ratings \nb. Adding a new restaurant \nc. Updating a random restaurant's rating \nq. Quitting \nEnter your response: \n"
        )
        elif request == 'c':
            update_random('scores.txt')
            request = input(
        "\nWhat would you like to do?\na. Seeing all the ratings \nb. Adding a new restaurant \nc. Updating a random restaurant's rating \nq. Quitting \nEnter your response: \n"
        )
        else:
            print("Please enter an valid response")
