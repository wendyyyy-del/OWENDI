from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # make sure your HTML is inside a folder called 'templates'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    
    # Save message to a text file
    with open('messages.txt', 'a') as f:
        f.write(f"{name}: {message}\n")
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
