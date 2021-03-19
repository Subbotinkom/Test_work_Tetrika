def del_double(a):
    """
    Функция удаляет дублирующиеся(накладывабщиеся друг на друга) интервалы.
    :param a: list
    :return: list
    """
    if len(a) == 2:
        return a

    intervals = []
    i = 2
    while i < len(a):
        if len(intervals) != 0:
            a_start, a_end = intervals[-2], intervals[-1]
            b_start, b_end = a[i], a[i + 1]
        else:
            a_start, a_end = a[0], a[1]
            b_start, b_end = a[2], a[3]

        i += 2
        # Проверяем, есть ли пересечения между a и b
        if a_end >= b_start and b_end >= a_start:
            sorted_list = sorted([a_start, a_end, b_start, b_end])
            # Проверяем, не совпадают ли искомый интервал с последним добавленным в intervals
            if sorted_list[0] != a_start and sorted_list[3] != a_end or len(intervals) == 0:
                intervals.extend([sorted_list[0], sorted_list[3]])
            # Проверяем случай, когда искомый интервал имеет верхнюю границу выше последнего добавленного в intervals
            elif sorted_list[0] <= a_start and sorted_list[3] != a_end:
                intervals.extend([a_end, sorted_list[3]])
        # Добавляем оба интервала в intervals т.к. нет пересечений/дублирования и это первая итерация
        elif len(intervals) == 0:
            intervals.extend([a_start, a_end, b_start, b_end])
        # Добавляем интервал, т.к. нет пересечений/дублирования
        else:
            intervals.extend([b_start, b_end])

    return intervals


def get_intersections(a, b):
    """
    Возвращает список пересечений между 2-мя списками интервалов
    :param a: list
    :param b: list
    :return: list
    """
    intersections = []
    i = j = 0
    while i < len(a) and j < len(b):
        a_start, a_end = a[i], a[i+1]
        b_start, b_end = b[j], b[j+1]

        if a_end < b_end:
            i += 2
        else:
            j += 2

        # Проверяем существует ли пересечение и добавляем его в intersections
        if a_end >= b_start and b_end >= a_start:
            sorted_list = sorted([a_start, a_end, b_start, b_end])
            intersections.extend(sorted_list[1:3])

    return intersections


def appearance(intervals):
    """
    Возвращает время общего присутствия ученика и учителя на уроке.
    :param intervals: list
    :return: int
    """
    # Получаем пересечение между списком lesson и pupil
    intersect_1 = get_intersections(del_double(intervals['lesson']), del_double(intervals['pupil']))
    # Потом это проверяем это пересечение с списком tutor
    result_intersect = get_intersections(intersect_1, del_double(intervals['tutor']))

    total = 0
    for i in range(0, len(result_intersect), 2):
        total += result_intersect[i + 1] - result_intersect[i]

    return total


tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
