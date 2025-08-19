import turtle
import random

catch_board = turtle.Screen()
catch_board.bgcolor("light blue")
catch_board.title("Catch The Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.shape("turtle")
turtle_instance.shapesize(stretch_wid=2, stretch_len=2)

score = 0
time = 20


score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-100, catch_board.window_height()//2 - 40)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))



time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(100, catch_board.window_height()//2 - 40)
time_display.write(f"Time: {time}", align="center", font=("Arial", 16, "bold"))


def score_board(x, y):
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))
    turtle_instance.hideturtle()


turtle_instance.onclick(score_board)


def time_board():
    global time
    if time > 0:
        time = time - 1
        time_display.clear()
        time_display.write(f"Time: {time}", align="center", font=("Arial", 16, "bold"))
        catch_board.ontimer(time_board, 1000)

    else:
        turtle_instance.hideturtle()
        time_display.clear()
        time_display.write(f"Oyun Bitti! Skorunuz: {score}", align="center", font=("Arial", 18, "bold"))


def teleport():
    global time
    if time > 0:
        turtle_instance.hideturtle()
        turtle_instance.up()
        width = catch_board.window_width() // 2
        height = catch_board.window_height() // 2

        x = random.randint(-width, width)
        y = random.randint(-height, height)

        turtle_instance.goto(x, y)
        turtle_instance.showturtle()



        catch_board.ontimer(teleport, 800)
    else:
        turtle_instance.hideturtle()




time_board()
teleport()
turtle.done()