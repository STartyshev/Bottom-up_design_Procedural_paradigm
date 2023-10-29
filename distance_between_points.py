from console_ui import *
from correct_initialization import input_correct_num, ui_array_of_dots_init, ui_random_array_of_dots_init
from math_functions import distance_between_points


# Задача №2
def ui_distance_between_points():
    """
    Функция реализующая пользовательский интерфейс в командной строке для поиска точек расстояние между,
    которыми больше заданного числа.
    """
    # Массивы с точками
    first_array_of_dots = []
    second_array_of_dots = []
    # Словарь в котором ключи - длины отрезков значения, которых больше заданного числа,
    # а значения - пары точек, которые эти отрезки образуют
    dict_of_segments_and_points = dict()
    # Заданное число с которым нужно сравнивать длину отрезков
    max_length = None
    # Флаг состояния
    algorithm_completed = False
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Расстояние между точками.'
        )
        match main_menu_item:
            # Условие задачи
            case 1:
                system('CLS')
                print(
                    'Входные данные: два массива с точками и число. '
                    'Требуется вывести точки из первого и второго массивов, '
                    'расстояния между которыми больше заданного числа. '
                    'Расстояния считаются только для соответствующих чисел.'
                )
                system('PAUSE')

            # Ввод исходных данных
            case 2:
                # При вводе новых данных все предыдущие обнуляются
                first_array_of_dots = []
                second_array_of_dots = []
                dict_of_segments_and_points = dict()
                algorithm_completed = False
                system('CLS')
                max_length = input_correct_num(
                    left_value=1,
                    right_value=float('inf'),
                    input_message='Введите значение с которым нужно сравнивать длины отрезков: ',
                    error_message='Значение должно быть положительное. Попробуйте еще раз.',
                    type_of_number=float
                )
                while True:
                    system('CLS')
                    initialization_item = ui_menu(
                        'Способ инициализации массивов точек.\n'
                        '1. Вручную.\n'
                        '2. Автоматически.'
                    )
                    match initialization_item:
                        # Инициализация массивов точек вручную
                        case 1:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            ui_array_of_dots_init(first_array_of_dots)
                            print('Инициализация второго массива: ')
                            ui_array_of_dots_init(second_array_of_dots)
                            break

                        # Инициализация массивов точек случайным образом
                        case 2:
                            system('CLS')
                            print('В каком пространстве будут находиться точки?\n'
                                  '1. На прямой.\n'
                                  '2. На плоскости.\n'
                                  '3. В трехмерном пространстве.')

                            space_selection = input_correct_num(
                                left_value=-float('inf'),
                                right_value=float('inf'),
                                input_message='Выберите пункт меню: ',
                                error_message='В меню всего 3 пункта. Попробуйте еще раз.',
                                type_of_number=int
                            )
                            print('Инициализация первого массива: ')
                            ui_random_array_of_dots_init(first_array_of_dots, space_selection)
                            print('Инициализация второго массива: ')
                            ui_random_array_of_dots_init(second_array_of_dots, space_selection)
                            break

                        case _:
                            print_error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                print('Инициализация массивов прошла успешно.')
                system('PAUSE')

            # Выполнение алгоритма
            case 3:
                system('CLS')
                if len(first_array_of_dots) < 1 or len(second_array_of_dots) < 1:
                    print_error_message(
                        'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    dict_of_segments_and_points = distance_between_points(
                        first_array_of_dots,
                        second_array_of_dots,
                        max_length
                    )
                    algorithm_completed = True
                    print('Алгоритм успешно выполнен!')
                    system('PAUSE')

            # Вывод результатов работы алгоритма
            case 4:
                system('CLS')
                if algorithm_completed:
                    if len(dict_of_segments_and_points.keys()) < 1:
                        print(f"Алгоритм не нашел ни одной пары точек, которые образовали бы отрезок "
                              f"длиной больше {max_length}.")
                    else:
                        print(
                            f"Результат работы алгоритма.\n"
                            f"Первый массив точек: {' '.join(map(str, first_array_of_dots))}\n"
                            f"Второй массив точек: {' '.join(map(str, second_array_of_dots))}\n"
                            f"Список точек расстояние между которыми больше {max_length}: "
                        )
                        for key in dict_of_segments_and_points.keys():
                            print(f"Пара точек: {dict_of_segments_and_points[key]}; длина отрезка, "
                                  f"который они образуют: {round(key, 1)}.\n")
                    system('PAUSE')
                else:
                    print_error_message(
                        'Невозможно вывести результат работы алгоритма, так как алгоритм не был выполнен. '
                        'Запустите работу алгоритма и попробуйте еще раз.'
                    )

            # Выход в главное меню
            case 5:
                break

            case _:
                print_error_message('В меню всего 5 пунктов. Попробуйте еще раз.')
