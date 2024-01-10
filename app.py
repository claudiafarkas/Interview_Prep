# Creates a basic Flask web server that listens for requests. 
# When someone accesses the root URL ('/'), it will serve an HTML file named non_technical_questions.html.
from flask import Flask, render_template, request, send_file
import csv
from non_technical_questions_random import get_questions  # Importing from your script


app = Flask(__name__)


def save_to_csv(question, answer):
    with open('saved_questions_and_answers.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([question, answer])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'submit_answer':
            question = request.form['question']
            answer = request.form['answer']
            save_to_csv(question, answer)
            chosen_row = get_questions()
            return render_template('non_technical_questions.html', chosen_row=chosen_row)
        elif request.form['action'] == 'download_answers':
            return send_file('saved_questions_and_answers.csv', as_attachment=True)
    else:
        chosen_row=get_questions()
        return render_template('non_technical_questions.html', chosen_row=chosen_row)

if __name__ == '__main__':
    app.run(debug=True)
