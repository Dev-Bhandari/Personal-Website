from flask import Flask, redirect, render_template, request, flash, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def home():
    return render_template('index.html')


app.run(debug=True, host='0.0.0.0')
