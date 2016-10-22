from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    john = {'name': 'John Smith', 'number':'(314)123-4567'}
    jacob = {'name': 'Jacob Heep', 'number':'(314)321-4567'}
    ann = {'name': 'Ann Kurtis', 'number':'(314)123-4999'}
    erica = {'name': 'Erica Jackson', 'number':'(314)100-4567'}

    persons=[john, jacob, ann, erica]

    return render_template('index.html', persons=persons)
