import triangulos
# import pytest


class TestTriangulos:
    def testa_escaleno(self):
        t = triangulos.Triangulo(3, 4, 5)
        assert t.a == 3 and t.b == 4 and t.c == 5
        assert t.perimetro() == 12
        assert t.tipo_lado() == 'Escaleno'

    def testa_equilatero(self):
        t = triangulos.Triangulo(4, 4, 4)
        assert t.a == 4 and t.b == 4 and t.c == 4
        assert t.perimetro() == 12
        assert t.tipo_lado() == 'Equilátero'

    def testa_isoceles(self):
        t = triangulos.Triangulo(10, 10, 12)
        assert t.a == 10 and t.b == 10 and t.c == 12
        assert t.perimetro() == 32
        assert t.tipo_lado() == 'Isóceles'
