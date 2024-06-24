import turtle
import pandas

correct_count = 0
correct_guesses = []
states_to_learn = []
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

data = pandas.read_csv("50_states.csv")

while correct_count < 50:
    answer_state = screen.textinput(title=f"Guess the State {correct_count}/50", prompt="What's another state's name?")
    guess = answer_state.title()
    if guess == "Exit":
        states_to_learn = [state for state in data.state.to_list() if state not in correct_guesses]
        learn = pandas.DataFrame(states_to_learn)
        learn.to_csv("States_to_learn")
        break
    if guess in data.state.to_list() and guess not in correct_guesses:
        correct_count += 1
        correct_guesses.append(guess)
        answer_row = data[data.state == guess]
        location = (int(answer_row["x"]), int(answer_row["y"]))
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(location)
        t.write(guess, align="center", font=("Courier", 10, "normal"))



