import time
import os


def clear_console():
    """
    Limpia la consola.
    """
    # Comando para limpiar la consola en Windows o Unix
    os.system('cls' if os.name == 'nt' else 'clear')


def clock_time():
    """
    Muestra la hora actual en formato HH:MM:SS en la consola en tiempo real.
    """
    try:
        while True:
            # Obtiene la hora actual
            current_time = time.strftime('%H:%M:%S')

            # Limpia la consola
            clear_console()

            # Imprime la hora actual
            print(f"Hora actual: {current_time}")

            # Espera 1 segundo antes de actualizar la hora
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReloj detenido.")


if __name__ == '__main__':
    clock_time()
