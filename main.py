from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def move_backward():
    turt.backward(10)


def turn_counter_clockwise():
    turt.left(10)


def turn_clockwise():
    turt.right(10)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.exitonclick()
