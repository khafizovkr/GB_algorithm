import random
# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные
# для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова
# запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве
# делителя.

while True:
    first_number = input('Введите первое число: ')
    second_number = input('Введите второе число: ')
    if (first_number.isdigit() and second_number.isdigit() or first_number[0] == '-' and first_number[1:].isdigit() and
            second_number[0] == '-' and second_number[1:].isdigit()):
        while (operation := input('Введите знак операции (+, -, *, /, если хотите завершить программу нажмите 0): ')) \
                not in '+-/*0':
            print('Вы ввели неверный знак!')
        else:
            if operation == '+':
                print(f'Сумма чисел равна {int(first_number) + int(second_number)}')
            elif operation == '-':
                print(f'Разница чисел раван {int(first_number) - int(second_number)}')
            elif operation == '*':
                print(f'Произведение чисел равно {int(first_number) * int(second_number)}')
            elif operation == '/':
                if int(second_number) == 0:
                    print('Деление на ноль!')
                else:
                    print(f'Результат деления равен {int(first_number) / int(second_number)}')
            elif operation == '0':
                break

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

user_number = input('Введите число ')
even_number_count = 0
for number in user_number:
    if int(number) % 2 == 0:
        even_number_count += 1
print(f'В числе {user_number} {even_number_count} четные цифры и {len(user_number) - even_number_count} нечетных цифр.')

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

user_number2 = input('Введите число ')
result = ''
for index in range(len(user_number2)):
    result += user_number2[len(user_number2) - index - 1]
print(result)

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры

elements_amount = int(input('Введите количество элементов '))
res = 0
for n in range(elements_amount):
    res += (-2)**(-n)
print(res)

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for i in range(32, 128):
    print('\n' if (i - 31) % 10 == 0 else f'{i} - "{chr(i)}" ', end='')

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что
# загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

rnd = random.randint(0, 100)
try_count = 0
while (user_answer := int(input('Угадайте число от 0 до 100: '))) != rnd:
    try_count += 1
    if user_answer > rnd:
        print(f'Вы ввели число больше загадонного. Осталось {10 - try_count} попыток.')
    elif user_answer < rnd:
        print(f'Вы ввели число меньше загаданного. Осталось {10 - try_count} попыток.')
    if try_count == 10:
        print(f'Вы не угадали загаданное число. Было загадано {rnd}')
        break
else:
    print('Поздравляю, вы угадали')

# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

user_number = int(input('Введите число n для проверки утверждения: 1+2+...+n = n(n+1)/2, '
                        'где n - любое натуральное число: '))
# будет лучше использовать моржовый оператор или позже заново расчитать по формуле user_number * (user_number + 1) / 2?
if (sum_of_numbers := sum(range(user_number + 1))) == user_number * (user_number + 1) / 2:
    print('Утверждение верно!')
else:
    print('Утверждение неверно!')
print(f'Сумма 1+2+...+n = {sum_of_numbers}')

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

list_of_numbers = input('Введите последователь чисел через пробел: ')
searching_for = input('Введите цифру, которую надо искать: ')
count = 0
for number in list_of_numbers.split(' '):
    for i in number:
        if searching_for == i:
            count += 1
print(f'Цифра {searching_for} встретилась {count} раз(а).')

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

users_numbers = input('Введите натуральные числа через пробел: ').split(' ')
sum_of_users_numbers = []
for number in users_numbers:
    res = 0
    for i in number:
        res += int(i)
    sum_of_users_numbers.append(res)
print(sum_of_users_numbers)
print(f'Число с наибольшей суммой цифр {users_numbers[sum_of_users_numbers.index(max(sum_of_users_numbers))]}. '
      f'Сумма цифр равна {max(sum_of_users_numbers)}')
