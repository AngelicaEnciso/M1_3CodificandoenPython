import turtle


def draw_pillar(t, width: int, height: int, color: str):
    """
    Dibuja un pilar (rectángulo vertical) con la tortuga.

    :param t: La tortuga que dibujará el pilar.
    :param width: Ancho del pilar.
    :param height: Altura del pilar.
    :param color: Color del pilar.
    """
    t.begin_fill()
    t.fillcolor(color)

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()


def draw_pillars(num_pillars: int, pillar_width: int, pillar_height: int, spacing: int, color: str):
    """
    Dibuja una serie de pilares en una fila.

    :param num_pillars: Número total de pilares a dibujar.
    :param pillar_width: Ancho de cada pilar.
    :param pillar_height: Altura de cada pilar.
    :param spacing: Espaciado entre los pilares.
    :param color: Color de los pilares.
    """
    window = turtle.Screen()
    window.title("Dibuja pilares")

    # Crea una tortuga
    drawer = turtle.Turtle()
    drawer.pensize(3)
    drawer.speed(2)

    for _ in range(num_pillars):
        draw_pillar(drawer, pillar_width, pillar_height, color)
        drawer.penup()
        drawer.forward(pillar_width + spacing)
        drawer.pendown()

    window.mainloop()


if __name__ == '__main__':
    num_pillars = 5  # Número de pilares
    pillar_width = 50  # Ancho de cada pilar
    pillar_height = 100  # Altura de cada pilar
    spacing = 20  # Espacio entre los pilares
    color = 'blue'  # Color de los pilares

    draw_pillars(num_pillars, pillar_width, pillar_height, spacing, color)
