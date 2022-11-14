"""Restaurant rating lister."""

def ratings(filename):
    dt = {}
    file = open(filename)

    rest = input("What's the restaurant name? ")
    score = input("What's the restaurant rating? ")
    dt[rest] = score

    for line in file:
        name, rating = line.split(":")
        dt[name] = rating.rstrip()

    for k, v in sorted(dt.items()): 
        print(f"{k} is rated at {v}")


if __name__ == '__main__':

    ratings('scores.txt')
