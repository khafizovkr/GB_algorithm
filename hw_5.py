# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

amount_of_companies = int(input('Количество предприятий: '))
companies = {}
full_income = 0

for i in range(1, amount_of_companies + 1):
    company_income = 0
    company = input(f'Название {i} предприятия: ')
    for quoter in range(1, 5):
        income_per_quoter = input(f'Прибыль "{company}" за {quoter} квартал: ')
        company_income += int(income_per_quoter)
    companies[company] = company_income
    full_income += company_income

average_income = full_income / amount_of_companies
below_avg_companies = []
above_avg_companies = []
avg_companies = []

for company in companies:
    if companies[company] > average_income:
        above_avg_companies.append(company)
    elif companies[company] < average_income:
        below_avg_companies.append(company)
    else:
        avg_companies.append(company)

print(f'Предприятия с прибылью выше среднего: {", ".join(above_avg_companies)}')
print(f'Предприятия со среденей прибылью: {", ".join(avg_companies)}') if len(avg_companies) > 0 else True
print(f'Предприятия с прибылью ниже среднего: {", ".join(below_avg_companies)}')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# first_number = [str(i) for i in input('Введите первое шестнадцатиричное число: ')]
# second_number = [str(i) for i in input('Введите второе шестнадцатиричное число: ')]
first_number = ['C']
second_number = ['A', '2', '5']

hex_numbers = [str(i) for i in range(0, 10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def sum_hex(first, second):
    if len(second) > len(first):
        first, second = second, first
    rev_first, rev_second = list(reversed(first)), list(reversed(second))
    while (ln := len(rev_second)) != len(rev_first):
        rev_second.append('0')

    res = []
    whole = 0
    for i in range(ln):
        frac = (hex_numbers.index(rev_first[i]) + hex_numbers.index(rev_second[i])) % 16 + whole
        whole = (hex_numbers.index(rev_first[i]) + hex_numbers.index(rev_second[i])) // 16
        res.append(hex_numbers[frac])
    else:
        if whole > 0:
            res.append(hex_numbers[whole])
    return res[::-1]


def multiply_hex(first, second):
    if second > first:
        first, second = second, first
    rev_first, rev_second = list(reversed(first)), list(reversed(second))
    res = []

    for i in range(len(rev_second)):
        whole = 0
        for_sum = []
        for j in range(len(rev_first)):
            frac = (hex_numbers.index(rev_first[j]) * hex_numbers.index(rev_second[i])) % 16 + whole
            whole = (hex_numbers.index(rev_first[j]) * hex_numbers.index(rev_second[i])) // 16
            if frac > 15:
                frac %= 16
                # Почему то без добавления единицы работает неправильно
                whole += frac // 16 + 1
            for_sum.append(hex_numbers[frac])
        else:
            if whole > 0:
                for_sum.append(hex_numbers[whole])
            for_sum = list(reversed(for_sum))
        if i > 0:
            for m in range(i):
                for_sum.append('0')
        res.append(for_sum)

    # Сложение после умножения стобиком
    while len(res) != 1:
        num1 = res.pop()
        num2 = res.pop()
        res.append(sum_hex(num1, num2))
    else:
        res = res[0]
    return res


print(sum_hex(first_number, second_number))
print(multiply_hex(first_number, second_number))
