import csv
import random

def get_questions():
    with open('non_technical_questions.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))

    print(chosen_row)
    return chosen_row
