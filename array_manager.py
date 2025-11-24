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

    def create_array(self):
        if self.rows == 0 or self.cols == 0:
            print("Сначала введите размер массива!\n")
            return

        print("\n=== Создание массива ===")
        print("1. Ручной ввод")
        print("2. Автоматический ввод (целые числа 0-100)")
        print("3. Назад")

        choice = input("Выберите вариант: ")

        if choice == "1":
            self.manual_input()
        elif choice == "2":
            self.automatic_input()
        elif choice == "3":
            return
        else:
            print("Неверный выбор!")

    def manual_input(self):
        print("\n--- Ручной ввод ---")
        self.array = np.zeros((self.rows, self.cols), dtype=int)

        for i in range(self.rows):
            for j in range(self.cols):
                while True:
                    try:
                        print(f"Введите элемент [{i}][{j}]: ", end="")
                        value = int(input())
                        self.array[i, j] = value
                        break
                    except ValueError:
                        print("Ошибка: введите целое число!")

        print("Массив успешно заполнен!")

    def automatic_input(self):
        print("\n--- Автоматический ввод ---")
        self.array = np.random.randint(0, 101, size=(self.rows, self.cols))
        print("Массив успешно заполнен случайными числами 0-100!")
