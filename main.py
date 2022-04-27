import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=930, height=723)
screen.bgpic("bulgaria_map.gif")

data = pandas.read_csv("regions_info.csv")
regions_list = data.region.tolist()
right_guess = 0
made_guesses = []
missed_regions = []

while right_guess < 28:

    guess = screen.textinput(f"{right_guess} / 28", "Име на регион.").title()

    if guess == "Изход":
        missed_regions = [n for n in regions_list if n not in made_guesses]
        data = pandas.DataFrame(missed_regions)
        data.to_csv("regions_to_learn.csv")
        break
    if guess in made_guesses:
        pass
    elif guess in regions_list:
        made_guesses.append(guess)
        guessed_region = data[data.region == guess]
        x_cor = int(guessed_region.x)
        y_cor = int(guessed_region.y)
        region = Turtle()
        region.hideturtle()
        region.penup()
        region.color("black")
        region.goto(x=x_cor, y=y_cor)
        region.write(guess, font=("Arial", 12, "normal"))
        right_guess += 1

screen.exitonclick()
