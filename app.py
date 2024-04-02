from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template('index.html')


# @app.route("/home")
# def home():
#     return("This in home page")


from controller.user_controller import *




