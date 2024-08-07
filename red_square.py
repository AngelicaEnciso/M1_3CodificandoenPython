import turtle

def draw_red_square(size: int):
    # Crea una ventana de dibujo
    window = turtle.Screen()
    window.title("Dibuja un cuadrado rojo")

    # Crea una tortuga
    red_turtle = turtle.Turtle()
    red_turtle.color("red")
    red_turtle.pensize(3)

    # Dibuja un cuadrado
    for _ in range(4):
        red_turtle.forward(size)
        red_turtle.right(90)

    # Termina el dibujo
    window.mainloop()

if __name__ == '__main__':
    size = 100  # Tamaño del cuadrado
    draw_red_square(size)
