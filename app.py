import os
from datetime import datetime
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for,
    send_from_directory, make_response, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import pycountry
import pymongo
import requests
import json
import numpy as np
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(e):
    """Error handler for error 404 NOT FOUND"""

    flash('Page not found!')
    return redirect(url_for('get_reviews'))


@app.route('/images/<file>')
def images(file):
    return send_from_directory('images', file)


def map_reviews(reviews):
    """
    Replace username with user's display name and
    and country code with country name in the <reviews> parameter list
    """
    for i, review in enumerate(reviews):
        user = mongo.db.users.find_one({"username": review.get('user')})
        country = pycountry.countries.get(alpha_2=review.get('country'))
        if user:
            reviews[i]['name'] = user.get('name')
        if country:
            reviews[i]['country'] = country.name
    return reviews


@app.route('/', methods=["GET", "POST"])
@app.route('/get_reviews', methods=["GET", "POST"])
def get_reviews():
    # Check if search url argument exists
    if request.args.get('s'):
        query = request.args.get('s')
        # Search using the query
        search_reviews = map_reviews(
            list(mongo.db.reviews.find({"$text": {"$search": query}})))
        recent_reviews = []
        top_reviews = []
        # If no results, search for the country code
        if not search_reviews:
            country = pycountry.countries.get(name=query)
            if country:
                search_reviews = map_reviews(list(mongo.db.reviews.find(
                    {"$text": {"$search": country.alpha_2}})))
    else:
        # If no search, then get recent and top reviews
        search_reviews = []
        recent_reviews = map_reviews(list(mongo.db.reviews.find().sort(
            [("added_on", pymongo.DESCENDING)]).limit(5)))
        top_reviews = map_reviews(list(mongo.db.reviews.find().sort(
            [("rating", pymongo.DESCENDING), ("added_on", pymongo.DESCENDING)]).limit(5)))

    return render_template("reviews.html", search_reviews=search_reviews,
                           recent_reviews=recent_reviews,
                           top_reviews=top_reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "name": request.form.get("name")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("get_reviews", username=session.get("user")))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if not session.get('user'):
        if request.method == "POST":
            # check if username exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

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
    else:
        # user already logged in
        flash("You have already logged in!")
        return redirect(url_for("get_reviews"))


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session.get('user')})
    if user:
        if request.method == "POST":
            updated_user = {
                "name": request.form.get("name"),
            }
            mongo.db.users.update(
                {"_id": ObjectId(user.get("_id"))}, {
                    '$set': updated_user})
            flash("Display name successfully updated!")
            return redirect(url_for("profile"))

        reviews = list(mongo.db.reviews.find(
            {'user': user.get("username")}))

        for i, review in enumerate(reviews):
            country = pycountry.countries.get(alpha_2=review.get('country'))
            if country:
                reviews[i]['country'] = country.name

        return render_template("profile.html", reviews=reviews, user=user)
    else:
        flash("Please log in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if session.get('user'):
        if request.method == "POST":
            if not request.form.get("country") or not request.form.get("city") or \
                    len(request.form.get("comment")) not in range(5, 501) or \
                    float(request.form.get("rating")) not in np.arange(1, 5.5, 0.5):
                if not request.form.get("country"):
                    flash("Please select a country!")
                if not request.form.get("city"):
                    flash("Please select a city!")
                if len(request.form.get("comment")) not in range(5, 501):
                    flash("Your review should be 5-500 characters!")
                if float(request.form.get("rating")) not in np.arange(1, 5.5, 0.5):
                    flash("Rating invalid!")
            else:
                # check if user already reviewed this city
                existing_review = mongo.db.reviews.find_one(
                    {"user": session.get('user'),
                     "country": request.form.get("country"),
                     "city": request.form.get("city")})
                if not existing_review:
                    review = {
                        "country": request.form.get("country"),
                        "city": request.form.get("city"),
                        "rating": request.form.get("rating"),
                        "comment": request.form.get("comment"),
                        "user": session["user"],
                        "added_on": datetime.now().strftime('%B %d, %Y, %H:%M'),
                        "edited": datetime.now().strftime('%B %d, %Y, %H:%M')
                    }
                    mongo.db.reviews.insert_one(review)
                    flash("Review successfully added!")
                    return redirect(url_for("profile"))
                else:
                    flash("You have already reviewed this city!")

        countries = pycountry.countries
        return render_template(
            "add_review.html", countries=countries)
    else:
        flash("Please log in!")
        return redirect(url_for("login"))


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
            if not request.form.get("country") or not request.form.get("city") or \
                    len(request.form.get("comment")) not in range(5, 501) or \
                    float(request.form.get("rating")) not in np.arange(1, 5.5, 0.5):
                if not request.form.get("country"):
                    flash("Please select a country!")
                if not request.form.get("city"):
                    flash("Please select a city!")
                if len(request.form.get("comment")) not in range(5, 501):
                    flash("Your review should be 5-500 characters!")
                if float(request.form.get("rating")) not in np.arange(1, 5.5, 0.5):
                    flash("Rating invalid!")
            else:
                submit = {
                    "country": request.form.get("country"),
                    "city": request.form.get("city"),
                    "rating": request.form.get("rating"),
                    "comment": request.form.get("comment"),
                    "user": session["user"],
                    "edited": datetime.now().strftime('%B %d, %Y, %H:%M')
                }

                mongo.db.reviews.update({"_id": ObjectId(review_id)}, {
                    '$set': submit})
                flash("Review successfully updated!")
                return redirect(url_for("profile"))
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
        flash("Review deleted!")
    else:
        flash("Only authors can delete reviews!")
    return redirect(url_for("profile"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
