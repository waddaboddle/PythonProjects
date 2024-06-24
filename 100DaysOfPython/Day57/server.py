from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<guess>")
def guessed(guess):
    response_age = requests.get(url=f"https://api.agify.io?name={guess}")
    response_gender = requests.get(url=f"https://api.genderize.io?name={guess}")
    guessed_gender = response_gender.json()["gender"]
    guessed_age = response_age.json()["age"]
    return render_template("guess.html", name=guess, gender=guessed_gender, age=guessed_age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
