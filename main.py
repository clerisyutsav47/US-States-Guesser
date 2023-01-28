import pandas
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("./50_states.csv")
state_list = data["state"].tolist()
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
answered = []
while len(answered) != 50:
    answer = screen.textinput(f"You've found {len(answered)}/50 states", "Enter the name of the state:").title()
    if answer in state_list and answer not in answered:
        answered.append(answer)
        data_state = data[data["state"] == answer]
        turtle.goto(float(data_state["x"]), float(data_state["y"]))
        turtle.write(answer)
    elif answer == "Exit":
        break
screen.exitonclick()
missed_state = [state for state in state_list if state not in answered]
missed_state = {"State": missed_state}
data_frame = pandas.DataFrame(missed_state)
data_frame.to_csv("./missed_states.csv")

