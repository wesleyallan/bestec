from flask import Flask, make_response
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

# Login e Registro
@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/registration/categories')
def registration_categories():
  return render_template("registration_categories.html")

@app.route('/reports')
def reports():
  return render_template("reports.html")

@app.route('/reports/sales')
def reports_sales():
  return render_template("reports_sales.html")

@app.route('/reports/ads')
def reports_ads():
  return render_template("reports_ads.html")

@app.route('/user')
def user():
  return render_template("user.html")

@app.route('/user/data')
def user_data():
  return render_template("user_data.html")

@app.route('/user/ads')
def user_ads():
  return render_template("user_ads.html")

@app.route('/user/ads/new')
def user_ads_new():
  return render_template("user_ads_new.html")

@app.route('/user/requests')
def user_requests():
  return render_template("user_requests.html")

@app.route('/user/favorites')
def user_favorites():
  return render_template("user_favorites.html")
