import csv

# read scores from scores.csv
with open('scores.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    # this line of code creates a dictionary with keys representing the names of players
    scores = {name: 0 for name in ["Josh", "Luke", "Kate", "Mark", "Mary"]}
    for row in reader:
        #loop extracts the player's name
        name = row[0]
        #convert the score from a string to an integer
        score = int(row[1])
        #the highest score
        if score > scores[name]:
            scores[name] = score

# sort scores by descending order of highest score
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# write high scores to high_scores.csv
with open('high_scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest score'])
    for name, score in sorted_scores:
        writer.writerow([name, score])
