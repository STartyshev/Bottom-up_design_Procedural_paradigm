from math import sqrt


def number_of_common_numbers(first_array, second_array):
    """
    Функция находит количество общих чисел в двух массивах.
    Также, число считается общим если оно входит в один массив, а в другом
    находится его перевернутая версия.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел.
    :return: Возвращает количество общих чисел двух массивов.
    """
    num_of_common_numbers = 0
    # Список в который будут добавляться общие числа
    list_of_common_numbers = []
    for elem in first_array:
        # Если число из первого массива или его обратная версия находятся во втором массиве
        # И это число еще не обрабатывалось прежде т. е. его нет в списке общих чисел
        # То оно добавляется в список и кол-во общих чисел увеличивается на 1
        if ((str(elem) in list(map(str, second_array)) or str(elem)[::-1] in list(map(str, second_array))) and
                elem not in list_of_common_numbers):
            num_of_common_numbers += 1
            list_of_common_numbers.append(elem)
    return num_of_common_numbers


def distance_between_points(first_array_of_dots, second_array_of_dots, distance):
    """
    Функция поиска точек расстояние между которыми больше заданного.
    :param first_array_of_dots: Первый массив точек;
    :param second_array_of_dots: второй массив точек;
    :param distance: заданное расстояние с которым будут сравниваться длины отрезков двух точек взятых
    из первого и второго массивов.
    :return: Возвращает словарь где ключи - длины отрезков которые больше заданного числа, а значения - пара точек,
    которые эти отрезки образуют.
    """
    return {
        segment_length(dot1, dot2): [dot1, dot2]
        for dot1, dot2 in zip(first_array_of_dots, second_array_of_dots)
        if segment_length(dot1, dot2) > distance
    }


def segment_length(dot1, dot2):
    """
    Функция вычисляющая длину отрезка образованного двумя точками.
    :param dot1: Первая точка;
    :param dot2: вторая точка.
    :return: Возвращает длину отрезка образованного двумя точками.
    """
    return sqrt(
        sum(
            (c1 - c2) ** 2 for c1, c2 in zip(dot1, dot2)
        )
    )


def arithmetic_conversion(first_array, second_array, third_array):
    """
    Функция реализующая решение следующей задачи:
    Требуется проверить можно ли получить число из 3-го массива, арифметическими преобразованиями
    с числами двух других массивов. Числа проверяются последовательно.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел;
    :param third_array: третий массив чисел, который будет проверяться.
    :return: Список со строками в которых будет содержаться описание результатов проверки
    (можно или нельзя преобразовать).
    """
    list_of_results = ['' for i in range(len(third_array))]
    triples_of_numbers = enumerate(zip(first_array, second_array, third_array))
    for index, triple in triples_of_numbers:
        try:
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 % elem2, '%'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 / elem2, '/'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 ** elem2, '**'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 * elem2, '*'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 - elem2, '-'
            )
            check_arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 + elem2, '+'
            )
        except ZeroDivisionError:
            pass

    for i in range(len(list_of_results)):
        if list_of_results[i] == '':
            list_of_results[i] = f"Нет способов получить {i + 1}-й элемент."

    return list_of_results


def check_arithmetic_operation(index, elem1, elem2, elem3, list_of_results, func, function_symbol):
    """
    Функция реализующая проверку: можно ли получить число из 3-го массива, заданным арифметическим преобразованием
    с числами 2-ух других массивов. В случае положительного результата добавляет полученый способ в список результатов.
    :param index: Индекс проверяемого элемента;
    :param elem1: элемент из первого массива;
    :param elem2: элемент из второго массива;
    :param elem3: элемент из третьего массива (проверяемый элемент);
    :param list_of_results: список полученных результатов;
    :param func: функция которая будет применяться к elem1 и elem2 (арифметическая операция);
    :param function_symbol: строковое отображение арифметической операции (значок).
    """
    if func(elem1, elem2) == elem3:
        if list_of_results[index] == '':
            list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                      f"{elem1} {function_symbol} {elem2} = {elem3};")
        else:
            list_of_results[index] += f"\n{elem1} {function_symbol} {elem2} = {elem3};"
    elif func(elem2, elem1) == elem3:
        if list_of_results[index] == '':
            list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                      f"{elem2} {function_symbol} {elem1} = {elem3};")
        else:
            list_of_results[index] += f"\n{elem2} {function_symbol} {elem1} = {elem3};"
