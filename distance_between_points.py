from console_ui import *


# Задача №2
def ui_distance_between_points():
    """
    Функция реализующая пользовательский интерфейс в командной строке для поиска точек расстояние между,
    которыми больше заданного числа.
    """
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Расстояние между точками.'
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
