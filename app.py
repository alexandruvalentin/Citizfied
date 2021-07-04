import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for,
    send_from_directory, make_response, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import pycountry
import requests
import json
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    reviews = list(mongo.db.reviews.find().limit(5))
    for i, review in enumerate(reviews):
        user = mongo.db.users.find_one({"username": review.get('user')})
        if user:
            reviews[i]['name'] = user.get('name')

    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("register", username=session.get("user")))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "get_reviews", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session.get('user')})
    if user:
        if request.method == "POST":
            pass

        reviews = list(mongo.db.reviews.find(
            {'user': user.get("username")}))
        return render_template("profile.html", reviews=reviews)
    else:
        flash("Please log in")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "country": request.form.get("country"),
            "city": request.form.get("city"),
            "rating": request.form.get("rating"),
            "comment": request.form.get("comment"),
            "user": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_reviews"))

    countries = pycountry.countries
    return render_template(
        "add_review.html", countries=countries)


@app.route('/countries')
def countries():
    # CREDITS to cities.json: https://github.com/lutangar/cities.json
    return send_from_directory('', 'cities.json')


@app.route('/cities/<country_code>')
def cities(country_code):
    r = requests.get(
        url_for('countries', _external=True))
    all_cities = json.loads(r.content)

    cities = [c for c in all_cities if c['country'] == country_code]
    citylist = []
    for city in cities:
        citylist.append(city['name'])

    return make_response(jsonify(sorted(citylist)))


@app.route('/edit_review/<review_id>', methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if session.get('user') == review.get('user'):
        if request.method == "POST":
            submit = {
                "country": request.form.get("country"),
                "city": request.form.get("city"),
                "rating": request.form.get("rating"),
                "comment": request.form.get("comment"),
                "user": session["user"]
            }

            mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
            flash("Review Successfully Updated")
        countries = pycountry.countries
        return render_template(
            "edit_review.html", countries=countries, review=review)
    else:
        flash("Only authors can manage reviews!")
        return redirect(url_for("get_reviews"))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if session.get('user') == review.get('user'):
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("Review Deleted")
    else:
        flash("Only authors can delete reviews!")
    return redirect(url_for("get_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
