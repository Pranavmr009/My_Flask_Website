from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/about")
def home_page():
    return render_template('home.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/portfolio")
def portfolio_page():
    return render_template('portfolio.html')