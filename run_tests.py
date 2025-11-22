import os
import subprocess
import questionary


def run_pytest(args: list):
    """Функция для запуска pytest с заданными аргументами"""
    command = ["pytest"] + args
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError: print("Во время прохождения теста проишла ошибка")
    except FileNotFoundError: print("Команда pytest не найдена."
                                    "Убедитесь, что pytest установлен и доступен в PATH")

def main_menu():
    """Главное меню CLI"""
    while True:
        choice = questionary.select("Добро пожаловать в CLI для запуска тестов.",
                                    choices=[
                                        "Запустить все тесты",
                                        "Запустить smoke тесты",
                                        "Запустить regression тесты",
                                        "Выход"
                                    ]).ask()

        if choice == "Запустить все тесты":
            run_pytest(["-v"])
        elif choice == "Запустить smoke тесты":
            run_pytest(["-v", "-m", "smoke",])
        elif choice == "Запустить regression тесты":
            run_pytest(["-v", "-m", "regression"])
        elif choice == "Выход":
            break

if __name__ == "__main__":
    main_menu()