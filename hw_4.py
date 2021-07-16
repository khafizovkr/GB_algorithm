import cProfile
import math
# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
# уроков.


def sum_n(n):
    res = 0
    for i in range(n):
        res += (-2)**(-i)
    return res


def sum_n2(n):
    e = 1
    s = 0
    for i in range(n):
        s += e
        e /= -2
    return s


cProfile.run('sum_n(100000)')
cProfile.run('sum_n2(100000)')
# Первый алгоритм (мой) дольше выполняется, чем второй (нашел в интернете, не смог написать рекурсию) потому что в нем
# сложнее операция - возведение в степень. По моему оба алгоритма линейные O(n).

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;


def prime_number(n):
    start = 3
    prime_numbers = [2]
    while True:
        if len(prime_numbers) == n:
            break
        for number in prime_numbers:
            if start % number == 0:
                break
        else:
            prime_numbers.append(start)
        start += 2
    return prime_numbers[-1]


# i-ое по счету число
pn_i = 500
print(f'{pn_i} простое число = {prime_number(pn_i)}')

# Используя алгоритм «Решето Эратосфена»


def sieve_eratosthenes(i):
    number_of_primes = 0
    start = 3
    while number_of_primes <= i:
        number_of_primes = start / math.log(start)
        start += 1

    lst_prime = [n for n in range(2, start)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


# print(f'{pn_i} простое число = {sieve_eratosthenes(pn_i)}')

cProfile.run('prime_number(500)')
cProfile.run('sieve_eratosthenes(500)')

# Решето Эратосфена дольше выполняется чем обычный, который перебирает числа
