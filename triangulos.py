
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        equilatero = 'equilátero'
        isoceles = 'isóceles'
        escaleno = 'escaleno'
        if not(self.a+self.b) > self.c or not(self.a+self.c) > self.b or not(self.b+self.c) > self.a:
            return False
        elif self.a == self.b == self.c:
            return equilatero
        elif self.a != self.b != self.c != self.a:
            return escaleno
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return isoceles
