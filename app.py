# Creates a basic Flask web server that listens for requests. 
# When someone accesses the root URL ('/'), it will serve an HTML file named non_technical_questions.html.
from flask import Flask, render_template, request, send_file
from non_technical_questions_random import get_questions 
from datetime import datetime 
import csv
import os

app = Flask(__name__)

#Global Variables
headerlist=['Date/Time', 'Question', 'Answer']


# Responsible for creating the csv file - if it doesnt exist and writing the headers
def save_to_csv(formatted_date, question, answer):
    file_exists = os.path.isfile('saved_questions_and_answers.csv')
    with open('saved_questions_and_answers.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if not file_exists:
            csvwriter.writerow(['Date/Time', 'Question', 'Answer'])
        csvwriter.writerow([formatted_date, question, answer])  # Write the data


@app.route('/', methods=['GET', 'POST'])
# Responsible for storing the question and answers
def index():
    if request.method == 'POST':
        if request.form['action'] == 'submit_answer':
            question =  request.form['question']
            answer = request.form['answer']

            date = datetime.now()
            formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')

            save_to_csv(formatted_date, question, answer)
            chosen_row = get_questions()
            return render_template('non_technical_questions.html', chosen_row = chosen_row)
        elif request.form['action'] == 'download_answers':
            answers_file_name = 'saved_questions_and_answers.csv'
            return send_file(answers_file_name, as_attachment = True)
    else:
        chosen_row = get_questions()
        return render_template('non_technical_questions.html', chosen_row = chosen_row)

if __name__ == '__main__':
    app.run(debug=True)
