import csv

lst = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]

with open("movies.csv", "w") as movie:
    c = csv.writer(movie, delimiter=",")
    for l in lst:
        c.writerow(l)
