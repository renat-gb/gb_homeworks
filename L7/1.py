# Реализовать класс Matrix (матрица).

# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.

# Решение требует установки доп модуля numpy


import numpy as np


class Matrix:
    def __init__(self):
        self.matrix_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def __str__(self):
        return str(self.matrix_one)

    def __add__(self, other):
        return other + self.matrix_one


matrix_res = Matrix()

matrix_res_one = matrix_res.matrix_one
print(matrix_res_one)

matrix_two = np.array([[6, 7, 8], [1, 2, 3], [1, 2, 3]])
matrix_res_two = matrix_res_one + matrix_two

print(matrix_res_two)
