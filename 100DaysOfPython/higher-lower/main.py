from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)
print(random_number)


@app.route("/")
def home():
    return "<h1>Guess the number between 0 and 9</h1>" \
           "<img src='https://media0.giphy.com/media/ne3xrYlWtQFtC/giphy.gif?cid=ecf05e47ktzkutg1clvfcn9omka1ze84ham2rbqr7df2i222&ep=v1_gifs_search&rid=giphy.gif&ct=g'>" \
           "<p></p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:guess>")
def guessed_pages(guess):
    if guess > random_number:
        return "<h1 style='color:red'>Too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess < random_number:
        return "<h1 style='color:blue'>Too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color:green'>Correct!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run()
