import time
import sys
import os
import math

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def create_profile():
    print_slow("Введите имя пользователя: ")
    username = input()
    print_slow("Введите пароль: ")
    password = input()

    if not os.path.exists("profiles"):
        os.makedirs("profiles")

    with open(f"profiles/{username}.txt", "w") as f:
        f.write(f"{username}:{password}")

    return username

def login():
    profiles = [f for f in os.listdir("profiles") if f.endswith(".txt")]

    if not profiles:
        return None

    print_slow("Доступные профили:")
    for i, profile in enumerate(profiles, 1):
        print_slow(f"{i}. {profile[:-4]}")

    print_slow("Выберите номер профиля: ")
    try:
        choice = int(input())
        selected_profile = profiles[choice-1]

        with open(f"profiles/{selected_profile}", "r") as f:
            data = f.read().split(":")
            username = data[0]

        print_slow("Введите пароль: ")
        password = input()

        with open(f"profiles/{selected_profile}", "r") as f:
            if f.read() == f"{username}:{password}":
                return username
            else:
                print_slow("Неверный пароль!")
                return None
    except:
        print_slow("Неверный выбор!")
        return None

def change_password(username):
    print_slow("Введите текущий пароль: ")
    current_password = input()

    # Проверяем текущий пароль
    with open(f"profiles/{username}.txt", "r") as f:
        if f.read() != f"{username}:{current_password}":
            print_slow("Неверный текущий пароль!")
            return False

    print_slow("Введите новый пароль: ")
    new_password = input()
    print_slow("Повторите новый пароль: ")
    confirm_password = input()

    if new_password != confirm_password:
        print_slow("Пароли не совпадают!")
        return False

    # Сохраняем новый пароль
    with open(f"profiles/{username}.txt", "w") as f:
        f.write(f"{username}:{new_password}")

    print_slow("Пароль успешно изменен!")
    return True

def shutdown_system():
    print_slow("Останавливаем работу OSbird...")
    time.sleep(3)
    print_slow("Заканчиваем работу Energy Star...")
    time.sleep(4)
    print_slow("Закрываем профиля...")
    time.sleep(2)
    print_slow("Отключение прав...")
    time.sleep(3)
    print_slow("Завершение работы...")
    time.sleep(5)
    sys.exit()

def load_menu():
    for i in range(51):
        sys.stdout.write(f"\rЗагрузка файлов меню ({i}/50)")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

    print_slow("Меню:")
    print_slow("1. Файлы")
    print_slow("2. Калькулятор")
    print_slow("3. Настройки")
    print_slow("4. Завершение работы")

    return show_apps()

def show_apps():
    print_slow("Введите номер приложения для запуска: ")
    choice = input()

    if choice == "1":
        return files_app()
    elif choice == "2":
        return calculator_app()
    elif choice == "3":
        return settings_app()
    elif choice == "4":
        shutdown_system()
    else:
        print_slow("Неверный выбор!")
        return load_menu()

def files_app():
    print_slow("Файловый менеджер")
    print_slow("1. Создать файл")
    print_slow("2. Просмотреть файлы")
    print_slow("3. Удалить файл")
    print_slow("4. Назад в меню")

    choice = input()
    if choice == "1":
        print_slow("Введите имя файла: ")
        filename = input()
        with open(filename, "w") as f:
            print_slow("Введите содержимое файла: ")
            content = input()
            f.write(content)
        print_slow(f"Файл {filename} создан!")
        return files_app()
    elif choice == "2":
        files = [f for f in os.listdir(".") if os.path.isfile(f)]
        print_slow("Файлы в текущей директории:")
        for file in files:
            print_slow(file)
        return files_app()
    elif choice == "3":
        print_slow("Введите имя файла для удаления: ")
        filename = input()

        if filename == "main.py":
            print_slow("Нельзя удалить основной файл системы!")
        elif os.path.exists(filename):
            os.remove(filename)
            print_slow(f"Файл {filename} удален!")
        else:
            print_slow("Файл не найден!")
        return files_app()
    elif choice == "4":
        return load_menu()
    else:
        print_slow("Неверный выбор!")
        return files_app()

def calculator_app():
    print_slow("Калькулятор")
    print_slow("1. Сложение")
    print_slow("2. Вычитание")
    print_slow("3. Умножение")
    print_slow("4. Деление")
    print_slow("5. Назад в меню")

    choice = input()
    if choice in ["1", "2", "3", "4"]:
        print_slow("Введите первое число: ")
        num1 = float(input())
        print_slow("Введите второе число: ")
        num2 = float(input())

        if choice == "1":
            result = num1 + num2
            print_slow(f"Результат: {result}")
        elif choice == "2":
            result = num1 - num2
            print_slow(f"Результат: {result}")
        elif choice == "3":
            result = num1 * num2
            print_slow(f"Результат: {result}")
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print_slow(f"Результат: {result}")
            else:
                print_slow("Ошибка: деление на ноль!")

        return calculator_app()
    elif choice == "5":
        return load_menu()
    else:
        print_slow("Неверный выбор!")
        return calculator_app()

def settings_app():
    print_slow("Настройки системы")
    print_slow("1. Сменить пароль")
    print_slow("2. Информация о системе")
    print_slow("3. Кредиты")
    print_slow("4. Назад в меню")

    choice = input()
    if choice == "1":
        # Получаем имя текущего пользователя из глобальной переменной
        if 'current_user' in globals():
            change_password(current_user)
        else:
            print_slow("Ошибка: пользователь не определен!")
        return settings_app()
    elif choice == "2":
        print_slow("OSbird 1.2.0")
        return settings_app()
    elif choice == "3":
        print_slow("Кредиты:")
        print_slow("OSbird 1.2.0")
        print_slow("Владелец системы: Владимир Золотарь")
        print_slow("Создатель системы: Владимир Золотарь")
        print_slow("Тестер: Владимир Золотарь")
        print_slow("Редактор: Владимир Золотарь")
        print_slow("Помощник: Идет его поиск")
        print_slow("Помощник с идеями: Владимир Золотарь")
        print_slow("Редактор кода для создания и тестирования: Replit")
        print_slow("В помощь с написанием кода помогал: DeepSeek")
        print_slow("")
        print_slow("Чтоб попасть в список напишите в телеграм пользователю: @VladimirZolotar")
        return settings_app()
    elif choice == "4":
        return load_menu()
    else:
        print_slow("Неверный выбор!")
        return settings_app()

print_slow("Запуск OSbird...")
time.sleep(3)

print_slow("Проверка первой плашки ОЗУ...")
time.sleep(1)
print_slow("Проверка второй плашки ОЗУ...")
time.sleep(1)
print_slow("Проверка третей плашки ОЗУ...")
time.sleep(1)

print_slow("Начинается проверка жесткого диска...")
time.sleep(5)

print_slow("Начинаем запуск Energy Star...")
time.sleep(3)
print_slow("Проверка всех прав...")
time.sleep(4)

print_slow("OSbird Запущена!")
print_slow("Проверка пользователя...")
time.sleep(5)

if not os.path.exists("profiles") or not os.listdir("profiles"):
    print_slow("Профили не обнаружены. Создать новый профиль? (y/n)")
    choice = input().lower()
    if choice == 'y':
        current_user = create_profile()
        print_slow(f"Профиль {current_user} успешно создан!")
        print_slow("Загрузить файлы меню? (y/n)")

        command = input().lower()
        if command == "y":
            load_menu()
        else:
            shutdown_system()
    else:
        shutdown_system()
else:
    print_slow("Обнаружены существующие профили. Войти в систему? (y/n)")
    choice = input().lower()
    if choice == 'y':
        current_user = login()
        if current_user:
            print_slow(f"Добро пожаловать, {current_user}!")
            print_slow("Загрузить файлы меню? (y/n)")

            command = input().lower()
            if command == "y":
                load_menu()
            else:
                shutdown_system()
        else:
            print_slow("Не удалось войти в систему.")
            shutdown_system()
    else:
        shutdown_system()