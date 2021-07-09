import random

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).


def rnd_list(start, end, amount):
    random_list = []
    for i in range(amount):
        random_list.append(random.randrange(start, end))
    return random_list


rnd1 = rnd_list(-100, 100, 15)
print(rnd1)


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
                flag = False
        if flag:
            break
    return array


print(bubble_sort(rnd1))

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

rnd2 = rnd_list(0, 50, 15)
print(rnd2)


def merge_sort(array):
    if len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array


print(merge_sort(rnd2))

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
# другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
# используйте метод сортировки, который не рассматривался на уроках

m = 5
rnd3 = rnd_list(-100, 100, 2 * m + 1)

print(rnd3)

while len(rnd3) != 1:
    max_element = 0
    min_element = 0
    for i in range(len(rnd3)):
        if rnd3[i] <= rnd3[min_element]:
            min_element = i
        elif rnd3[i] >= rnd3[max_element]:
            max_element = i
    min_element_val = rnd3[min_element]
    max_element_val = rnd3[max_element]
    rnd3.remove(min_element_val)
    rnd3.remove(max_element_val)

print(f'Медиана: {rnd3[0]}')
