import sys
import random
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей
# ОС.

# Windows 10 64-bit, Python 3.9

sides_length = input('Через пробел введите стороны трегольника: ').split()
sides_length_int = list(map(int, sides_length))
first_side = max(sides_length_int)
sides_length_int.remove(first_side)
if sum(sides_length_int) > first_side:
    print('Треугольник существует')
    if (sides_length_set := len(set(sides_length))) == 3:
        print('Треугольник разносторонний')
    elif sides_length_set == 2:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник равносторонний')
else:
    print('Треугольник не существует')

size_of_first_task = sys.getsizeof(sides_length) + sys.getsizeof(sides_length_int) + sys.getsizeof(first_side)
print(f'Программа задействует {size_of_first_task} байт памяти.')

# Результат:
# Через пробел введите стороны трегольника: 6 5 4
# Треугольник существует
# Треугольник разносторонний
# Программа задействует 300 байт памяти.

# Проверял эту же задачу на Windows 7 64-bit, Python 3.8. Там программа занимала 276 байт памяти.

list_of_numbers = input('Введите последователь чисел через пробел: ')
searching_for = input('Введите цифру, которую надо искать: ')
count = 0
for number in list_of_numbers.split(' '):
    for i in number:
        if searching_for == i:
            count += 1
print(f'Цифра {searching_for} встретилась {count} раз(а).')

size_of_second_task = sys.getsizeof(list_of_numbers) + sys.getsizeof(searching_for) + sys.getsizeof(count) + \
                      sys.getsizeof(number) + sys.getsizeof(i)
print(f'Программа задействует {size_of_second_task} байт памяти.')

# Результат:
# Введите последователь чисел через пробел: 15 32
# Введите цифру, которую надо искать: 0
# Цифра 0 встретилась 0 раз(а).
# Программа задействует 229 байт памяти.

# В этой программе в зависимости от исходных данных задействуется разное количество памяти.

print('Создаем матрицу')
matrix = []
for i in range(9):
    matrix_line = []
    for j in range(8):
        matrix_line.append(random.randint(0, 100))
    else:
        matrix_line.append(0)
    matrix.append(matrix_line)
    print(matrix_line)

print('\nНахожу сумму строк')
for i in range(len(matrix)):
    matrix_line_sum = 0
    for j in range(len(matrix[i]) - 1):
        matrix_line_sum += matrix[i][j]
    matrix[i][4] = matrix_line_sum
    print(matrix[i])

size_of_third_task = sys.getsizeof(matrix) + sys.getsizeof(i) + sys.getsizeof(matrix_line) + \
                     sys.getsizeof(matrix_line_sum)
print(f'Программа задействует {size_of_third_task} байт памяти.')

# Результат для матрицы 5 х 5:
# 1 Создаем матрицу
# [17, 6, 85, 80, 0]
# [98, 44, 89, 97, 0]
# [19, 4, 46, 60, 0]
# [11, 66, 27, 44, 0]
# [72, 39, 82, 59, 0]
#
# Нахожу сумму строк
# [17, 6, 85, 80, 188]
# [98, 44, 89, 97, 328]
# [19, 4, 46, 60, 129]
# [11, 66, 27, 44, 148]
# [72, 39, 82, 59, 252]
# Программа задействует 296 байт памяти.

# Для матрицы размером до 8 х 8 включительно программа задействует 296 байт, если матрица больше, то 424 байта.
