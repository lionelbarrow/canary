from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/forecast")
def forecast():
    return render_template('forecast.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
