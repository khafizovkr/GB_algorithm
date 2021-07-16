import itertools
import collections

# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

string = 'hello hi'
string = string.replace(' ', '')

sub_list = set()
for i in range(1, len(string)):
    for j in itertools.combinations(string, i):
        sub_str = hash(''.join(j))
        if ''.join(j) in string:
            sub_list.add(sub_str)
print(f'Количество подстрок: {len(sub_list)}')

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.


class MyNode:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


def search(node, path='',):
    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        spam = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam
    if node.left is not None and node.left.value != 0:
        spam = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam


my_str = input('Введите строку для кодирования: ')

s_dict = {}
for i in my_str:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1

node_list = collections.deque([MyNode(s_dict[i], i) for i in s_dict])

for i in range(len(s_dict)-1):

    node_list = collections.deque(sorted(node_list, key=lambda node: node.value))

    first_el = node_list.popleft()
    second_el = node_list.popleft()

    new_node = MyNode(first_el.value + second_el.value, left=first_el, right=second_el)

    node_list.appendleft(new_node)

tree = node_list[0]

table = {}
for i in range(len(s_dict)):
    k = search(tree)
    table[k[0]] = k[1]
del tree

print(f'Оригинальная строка: {my_str}')
print('Кодированная строка:', end=' ')
for char in my_str:
    print(table[char], end=' ')
