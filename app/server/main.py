from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=f'{os.getcwd()}/app/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    # do something
    return 'predictions'


if __name__ == "__main__":
    app.run(debug=True)
