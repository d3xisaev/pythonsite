from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

Message = namedtuple('Message', 'text')
messages = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']

    messages.append(Message(text))

    return redirect(url_for('about'))


if __name__  == '__main__':
    app.run(debug=True)
