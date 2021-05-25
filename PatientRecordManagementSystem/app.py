from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page. Place Home Page contents here.'

@app.route('/services')
def products():
    return 'Services Page. Place Services Page contents here.'

@app.route('/booking')
def branches():
    return 'Booking Page. Place Booking Page contents here.'

@app.route('/doctors')
def aboutus():
    return 'Doctors Page. Place Doctors Page contents here.'
