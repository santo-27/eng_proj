# from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
# from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
Bootstrap5(app)
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chennai,India"

WEA_API_KEY = "BYQFA92QMMNN5WQSWHUQEVLMB" #weather api key


# body={
#     "location": "Chennai,India",
# }

params = {
    "key": WEA_API_KEY,
}
weather = requests.get(base_url,params=params)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))



with app.app_context():
    db.create_all()

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        new_interval = request.form['new_interval']
        print(new_interval)
        return render_template("index.html")
        
    
    print(weather.json())
    return render_template("index.html", weather = weather.json())



if __name__ == "__main__":
    app.run(port=5002, debug = True)