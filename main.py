from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def move_backward():
    turt.backward(10)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.exitonclick()
