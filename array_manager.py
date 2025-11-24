import numpy as np
from collections import Counter


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
        print("a. Ручной ввод")
        print("b. Автоматический ввод (целые числа 0-100)")
        print("c. Назад")

        choice = input("Выберите вариант: ")

        if choice.lower() == "a":
            self.manual_input()
        elif choice.lower() == "b":
            self.automatic_input()
        elif choice.lower() == "c":
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

    def view_array(self):
        print("\n=== Просмотр массива ===")

        if self.array is None:
            print("Массив еще не создан!\n")
            return

        print("Содержимое массива:")
        print(self.array)

    def performing_functions(self):
        print("\n=== Выполнение функций ===")

        print("a. Вывести элементы массива, кратные 5, и их индексы")
        print("b. Вывести номера тех строк массива, в "
              "которых есть хотя бы один элемент, равный 10")
        print("c. Найти столбец с наибольшей суммой элементов")
        print("d. Найти все неповторяющиеся элементы "
              "двумерного массива целых чисел")
        print("e. Удалить из массива строку и столбец, на пересечении "
              "которых расположен минимальный элемент")

        choice = input("Выберите вариант: ")

        if choice.lower() == "a":
            self.output_elements_array()
        elif choice.lower() == "b":
            self.output_elements_ten()
        elif choice.lower() == "c":
            self.find_column_with_max_sum()
        elif choice.lower() == "d":
            self.find_unique_elements()
        elif choice.lower() == "e":
            self.delete_row_col_with_min()
        else:
            print("Неверный выбор!")

    def output_elements_array(self):
        if self.array is None:
            print("Массив еще не создан!\n")
            return

        print("Элементы, кратные 5, и их индексы:")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] % 5 == 0:
                    print(f"Элемент array[{i}][{j}] = {self.array[i][j]}")

    def output_elements_ten(self):
        if self.array is None:
            print("Массив еще не создан!\n")
            return

        print("Элементы, равные 10, и их номер строки:")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] == 10:
                    print(f"Элемент array[{i}] = {self.array[i][j]}")

    def find_column_with_max_sum(self):
        if self.array is None:
            print("Массив еще не создан!\n")
            return

        max_sum = sum(self.array[:, 0])
        result_column = 0

        for j in range(self.cols):
            current_sum = sum(self.array[:, j])
            if current_sum > max_sum:
                max_sum = current_sum
                result_column = j

        print(f"Столбец {self.array[:, result_column]} с наибольшей "
              f"суммой {max_sum}")

    def find_unique_elements(self):
        if self.array is None:
            print("Массив еще не создан!\n")
            return

        unique_elements = [int(x) for x, count in
                           Counter(self.array.flatten()).items()
                           if count == 1]
        print(f"Неповторяющиеся элементы: {unique_elements}")

    def delete_row_col_with_min(self):
        if self.array is None:
            print("Массив еще не создан!\n")
            return

        min_index = np.unravel_index(np.argmin(self.array), self.array.shape)
        min_row, min_col = min_index

        print(f"Минимальный элемент {self.array[min_row, min_col]} на "
              f"позиции ({min_row}, {min_col})")

        new_matrix = np.delete(self.array, min_row, axis=0)
        new_matrix = np.delete(new_matrix, min_col, axis=1)

        self.array = new_matrix

        print(f"Новый вид массива:\n{self.array}")
