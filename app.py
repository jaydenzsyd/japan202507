from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

color = "#ffffff"
colorhead = "#888888"

@app.route('/home')
def home():
    return render_template('home.html', color = color)

@app.route('/parks')
def parks():
    return render_template('parks.html')

@app.route('/contact')
def contact():
    return render_template('feedback.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedbackstore():
    message = ""
    if request.method == 'POST':
        feedback = request.form.get('fname')  # get the input from the form
        name = request.form.get('name')        # name input
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # current time/date
        messagevar = name + " " + feedback + " " + timestamp
    print("Received feedback:", feedback)

    with open('feedback_storage.txt', 'a', encoding='utf-8') as f:
        f.write(messagevar + '\n---\n')
        message = f"Thank you for your feedback, {messagevar} !"

    return render_template('feedback.html', message=message)
@app.route('/myexp')
def myexp():
    return render_template('myexp.html')

if __name__ == '__main__':
    app.run(host='192.168.86.250',debug=True)
