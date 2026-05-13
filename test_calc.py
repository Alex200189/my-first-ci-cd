# test_calc.py
from calc import add, subtract

def test_add():
    # Проверяем, что 2 + 3 действительно равно 5
    assert add(2, 3) == 100

def test_subtract():
    # Проверяем вычитание
    assert subtract(10, 5) == 5

def test_add_negative():
    # Проверим отрицательные числа
    assert add(-1, -1) == -2
