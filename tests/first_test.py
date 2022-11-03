### Задание 19.2.3

import pytest
from app.calculator import Calculator

class TestCalc:
   """коллекция позитивных тестов арифметических функций калькулятора"""
   def setup (self):
       self.calc = Calculator

   def test_multiply (self):
       """тест функции умножения"""
       assert self.calc.multiply (self, 3, 20) == 60

   def test_division (self):
       """тест функции деления"""
       assert self.calc.division (self, 30, 2) == 15

   def test_subtraction (self):
       """тест функции вычитания"""
       assert self.calc.subtraction(self, 8, 2) == 6

   def test_adding (self):
       """тест функции сложения"""
       assert self.calc.adding (self, 3, 20) == 23