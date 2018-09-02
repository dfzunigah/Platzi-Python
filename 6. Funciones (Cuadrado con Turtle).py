import turtle

def suma(num1, num2):
    return num1 + num2

def make_line_and_turn(turtle, length):
    turtle.forward(length)
    turtle.left(90)

def make_square(turtle):
    length = int(input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(turtle, length)

def main():
    window = turtle.Screen()
    donatello = turtle.Turtle()

    make_square(donatello)

if __name__ == '__main__':
    main()
