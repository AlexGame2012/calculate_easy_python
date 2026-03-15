import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division2():
    assert calculate(8, 2, '/') == 4

def test_calculate_division3():
    assert calculate(3, 4, '*') == 12

def test_calculate_division4():
    assert calculate(1, 12, '-') == -11

def test_calculate_division5():
    assert calculate(4, 0, '/') == "Ошибка: Деление на ноль."

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
