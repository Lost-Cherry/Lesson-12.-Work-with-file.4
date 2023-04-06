"""
Write a program that will simulate user score in a game. Create a list with 5 player's names. After that simulate 100 games for each player. As a result of the game create a list with player's name and his score (0-1000 range). And save it to a CSV file. File should looks like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
...
"""
from contextlib import contextmanager
import random
import csv

names = ["Josh", "Luke", "Kate", "Mark", "Mary"]
header = ["Player name", "Score"]
scores = []

# simulate 100 games for each player
for i in range(500):
    # randomly select a player name for each game
    name = random.choice(names)
    # generate random score for each game
    score = random.randint(0, 1000)
    # add player's name and score to the scores list
    scores.append([name, score])

# save scores to a CSV file
with open("scores.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(scores)

