from array_manager import *


def main():
    manager = ArrayManager()

    while True:
        print("a. Создание массива")
        print("b. Ввод размера массива")
        print("c. Просмотр созданного массива")
        print("d. Выполнение функций")
        print("e. Выход\n")

        choice = input("Выберите пункт меню (1-4): ")

        if choice.lower() == "a":
            manager.create_array()
        elif choice.lower() == "b":
            manager.input_array_size()
        elif choice.lower() == "c":
            manager.view_array()
        elif choice.lower() == "d":
            manager.performing_functions()
        elif choice.lower() == "e":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 4.")


if __name__ == "__main__":
    main()
