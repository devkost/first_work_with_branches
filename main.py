from array_manager import *


def main():
    manager = ArrayManager()

    while True:
        print("1. Создание массива")
        print("2. Ввод размера массива")
        print("3. Просмотр созданного массива")
        print("4. Выход\n")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            manager.create_array()
        elif choice == "2":
            manager.input_array_size()
        elif choice == "3":
            manager.view_array()
        elif choice == "4":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 4.")


if __name__ == "__main__":
    main()
