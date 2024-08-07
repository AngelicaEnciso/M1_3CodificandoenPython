# ******************
# CALCULO DE INTERES SIMPLE
# ******************

def run(principal: float, rate: float, time: float) -> float:
    # Calcula el interés simple
    interest = principal * rate * time
    return interest

if __name__ == '__main__':
    principal = 1000  # Ejemplo de monto principal
    rate = 0.05  # Ejemplo de tasa de interés (5%)
    time = 3  # Ejemplo de tiempo en años
    interest = run(principal, rate, time)
    print(f"El interés simple es: {interest}")