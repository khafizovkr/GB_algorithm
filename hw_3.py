import random
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for divisor in range(2, 10):
    count = 0
    for dividend in range(2, 100):
        if dividend % divisor == 0:
            count += 1
    print(f'В диапозоне от 2 до 99, {count} чисел кратны {divisor}')

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
# 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с
# нуля), т.к. именно в этих позициях первого массива стоят четные числа.

elements_in_list = random.randint(5, 10)
first_list = []
for i in range(elements_in_list):
    first_list.append(random.randint(0, 100))

second_list = []
for i in range(len(first_list)):
    if first_list[i] % 2 == 0:
        second_list.append(i)

print(f'Первый список: {first_list}')
print(f'Список с индексами четных чисел: {second_list}')

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

elements_in_list2 = random.randint(5, 10)
min_max_list = []
for i in range(elements_in_list2):
    min_max_list.append(random.randint(0, 100))

min_element_index = 0
max_element_index = 0
print(min_max_list)
for i in range(1, len(min_max_list)):
    if min_max_list[i] < min_max_list[min_element_index]:
        min_element_index = i
    elif min_max_list[i] > min_max_list[max_element_index]:
        max_element_index = i
min_max_list[min_element_index], min_max_list[max_element_index] = min_max_list[max_element_index], min_max_list[min_element_index]
print(min_max_list)

# 4. Определить, какое число в массиве встречается чаще всего.

elements_in_list5 = random.randint(0, 20)
element_count_list = []
for i in range(elements_in_list5):
    element_count_list.append(random.randint(0, 10))

count_max = 0
for element in element_count_list:
    count1 = 0
    for element2 in element_count_list:
        if element == element2:
            count1 += 1
    if count_max < count1:
        count_max = count1
        count_max_element = element
print(element_count_list)
print(f'Число {count_max_element} встречается {count_max} раз(а)')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

elements_in_list1 = random.randint(5, 10)
some_list = []
for i in range(elements_in_list1):
    some_list.append(random.randint(-100, 100))

min_element = 0
for i in range(1, len(some_list)):
    if some_list[i] < some_list[min_element]:
        min_element = i
print(some_list)
print('Нет отрицательных элементов' if some_list[min_element] >= 0
      else f'Максимальный отрицательный элемент {some_list[min_element]} находится на {min_element} позиции '
           f'(начиная с 0)')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

elements_in_list3 = random.randint(5, 10)
first_list2 = []
for i in range(elements_in_list3):
    first_list2.append(random.randint(0, 100))

max_element = 0
min_element1 = 0
for i in range(1, len(first_list2)):
    if first_list2[i] <= first_list2[min_element1]:
        min_element1 = i
    elif first_list2[i] >= first_list2[max_element]:
        max_element = i

sum_of_elements = 0
if max_element > min_element1:
    for i in range(min_element1 + 1, max_element):
        sum_of_elements += first_list2[i]
else:
    for i in range(max_element + 1, min_element1):
        sum_of_elements += first_list2[i]
print(f'Сумма между минимальным и максимальным элементами в массиве {first_list2} равна {sum_of_elements}.')

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.

elements_in_list4 = random.randint(5, 10)
first_list2 = []
for i in range(elements_in_list4):
    first_list2.append(random.randint(0, 100))

min1, min2 = 0, 1
if first_list2[min2] < first_list2[min1]:
    min2, min1 = min1, min2

for i in range(2, len(first_list2)):
    if first_list2[i] < first_list2[min1]:
        min2, min1 = min1, i
    elif first_list2[i] < first_list2[min2]:
        min2 = i
# чтобы проще было проверять, сделал сортировку
print(sorted(first_list2))
print(f'Два наименьших элемента: {first_list2[min1]}, {first_list2[min2]}')

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

print('Создаем матрицу')
matrix = []
for i in range(5):
    matrix_line = []
    for j in range(4):
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

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

print('Создаем матрицу:')
M = random.randint(5, 10)
N = random.randint(5, 10)
matrix2 = []
for i in range(N):
    matrix_line1 = []
    for j in range(M):
        matrix_line1.append(random.randint(0, 100))
    matrix2.append(matrix_line1)
    print(matrix_line1)

print('Нахожу минимальные элементы столбцов матрицы:')
min_el_in_matrix = []
for i in range(M):
    min_element2 = 0
    for j in range(N):
        if matrix2[j][i] <= matrix2[min_element2][i]:
            min_element2 = j
    min_el_in_matrix.append(matrix2[min_element2][i])
print(min_el_in_matrix)

print('Нахожу максимальный элемент среди минимальных элементов:')
max_element1 = 0
for i in range(1, len(min_el_in_matrix)):
    if min_el_in_matrix[i] > min_el_in_matrix[max_element1]:
        max_element1 = i
print(min_el_in_matrix[max_element1])
