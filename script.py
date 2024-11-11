import eel

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

# Инициализация Eel
eel.init('web')

@eel.expose
def add_complex(real1, imag1, real2, imag2):
    z1 = Complex(real1, imag1)
    z2 = Complex(real2, imag2)
    result = z1 + z2
    return str(result)

@eel.expose
def subtract_complex(real1, imag1, real2, imag2):
    z1 = Complex(real1, imag1)
    z2 = Complex(real2, imag2)
    result = z1 - z2
    return str(result)

@eel.expose
def multiply_complex(real1, imag1, real2, imag2):
    z1 = Complex(real1, imag1)
    z2 = Complex(real2, imag2)
    result = z1 * z2
    return str(result)

@eel.expose
def divide_complex(real1, imag1, real2, imag2):
    z1 = Complex(real1, imag1)
    z2 = Complex(real2, imag2)
    try:
        result = z1 / z2
    except ZeroDivisionError:
        return "Division by zero is undefined"
    return str(result)

# Запуск интерфейса
eel.start('main.html', size=(600, 400))
