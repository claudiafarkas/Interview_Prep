import csv
import random

def get_questions():
    with open('non_technical_questions.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    question = chosen_row[0] if chosen_row else "No question found"

    print(question)
    return question
