import numpy as np


class ArrayManager:
    def __init__(self):
        self.array = None
        self.rows = 0
        self.cols = 0

    def input_array_size(self):
        print("\n=== Ввод размера массива ===")
        try:
            self.rows = int(input("Введите количество строк: "))
            self.cols = int(input("Введите количество столбцов: "))

            if self.rows <= 0 or self.cols <= 0:
                print("Ошибка: размеры должны быть положительными числами!")
                return False

            print(f"Установленный размер массива: {self.rows} x {self.cols}\n")
            return True

        except ValueError:
            print("Ошибка: введите целые числа!")
            return False
