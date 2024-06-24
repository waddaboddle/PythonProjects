from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"

    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://images.unsplash.com/photo-1606081165491-3384c9156db9?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8dHVya2V5JTIwYmlyZHxlbnwwfHwwfHx8MA%3D%3D'>"


@app.route("/bye")
@make_bold
@make_italic
@make_underline
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
