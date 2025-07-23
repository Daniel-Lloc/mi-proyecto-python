"""Modulo que ofrece operaciones basicas de una calculadora."""


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a y b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la division de a entre b."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


if __name__ == "__main__":
    # Ejemplo de uso
    print("Suma:", sumar(5, 3))
    print("Resta:", restar(5, 3))
    print("Multiplicacion:", multiplicar(5, 3))
    print("Division:", dividir(5, 3))
