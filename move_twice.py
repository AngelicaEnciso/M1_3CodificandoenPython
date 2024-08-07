import turtle


def move_twice(t, direction: str, distance: int):
    """
    Mueve la tortuga dos veces en una dirección especificada.

    :param t: La tortuga que se moverá.
    :param direction: La dirección en la que se moverá ('forward', 'backward', 'left', 'right').
    :param distance: La distancia que la tortuga se moverá en cada movimiento.
    """
    if direction == 'forward':
        t.forward(distance)
        t.forward(distance)
    elif direction == 'backward':
        t.backward(distance)
        t.backward(distance)
    elif direction == 'left':
        t.left(90)
        t.forward(distance)
        t.forward(distance)
        t.right(90)
    elif direction == 'right':
        t.right(90)
        t.forward(distance)
        t.forward(distance)
        t.left(90)
    else:
        print("Dirección no válida. Use 'forward', 'backward', 'left' o 'right'.")


if __name__ == '__main__':
    # Configura la ventana de dibujo
    window = turtle.Screen()
    window.title("Mueve la tortuga dos veces")

    # Crea una tortuga
    my_turtle = turtle.Turtle()
    my_turtle.pensize(3)

    # Mueve la tortuga dos veces hacia adelante
    move_twice(my_turtle, 'forward', 100)

    # Termina el dibujo
    window.mainloop()
