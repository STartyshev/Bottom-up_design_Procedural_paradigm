from console_ui import *


# Задача №1
def ui_number_of_common_numbers():
    """
    Функция реализующая пользовательский интерфейс в командной строке для поиска кол-ва общих чисел в двух массивах.
    """
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Проверка двух массивов на количество общих чисел.'
        )

        match main_menu_item:
            # Условие задачи
            case 1:
                pass

            # Ввод исходных данных
            case 2:
                pass

            # Выполнение алгоритма
            case 3:
                pass

            # Вывод результатов работы алгоритма
            case 4:
                pass

            # Выход в главное меню
            case 5:
                break

            case _:
                print_error_message('В меню всего 5 пунктов. Попробуйте еще раз.')
