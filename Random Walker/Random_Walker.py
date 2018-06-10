import turtle
import random

def get_direction():
    # Maybe update to 8 directions! with upleft, upright, downleft, downright
    step = random.randint(0,3)
    return step
        
def take_step(speed = 1):
    step = get_direction()
    if step == 0:
        turtle.forward(speed)
    if step == 1:
        turtle.backward(speed)
    if step == 2:
        turtle.left(90)
        turtle.forward(speed)
    else:
        turtle.right(90)
        turtle.forward(speed)

def main():
    turtle.title("Random Walk")
    turtle.hideturtle()

    try:
        while True:
            take_step(speed = 1)
            #if turtle.onkeypress(fun, "space"):
            #    turtle.bye()
    except:
        print("Closing Error!")
        pass


if __name__ == "__main__":
    main()