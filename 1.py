# print(0.1 + 0.1 * 5 - 0.3 * 4)
#
# print((3.14 + 0.3) / 2 + 0.15)
#
# a = -13
# b = 7
# a = a - b
# b = a + b
# a = b - a
# print(a)
# print(b)
#
# print(3 > 10)
# print('the' in 'python')
#
# s1 = "foo"
# s2 = "bar"
# s = s1 + s2
# print(s)
#
# print(round(0.3 + 0.3 + 0.3, 2))
#
# print(-5 / 2)
# print(-5 // 2)
# print(-5 % 2)
#
# print((31 % 2) + (-31 % 2))
#
# print(13 % -3 * 3 - 3 ** 2)
#
# # f = 653457
# # g = 123493
# # print(f**g)
#
# print(round(11 * 2.5 / 3, 2))
# print(3.14159 ** 2 / 2)
# print(round(3.14159 ** 2 / 2))

# s = "Hello!"
# print(s[2:])
# print(s[:4])
# print(len(s))

# colors = 'red blue green'
# print(colors.split())

# numbers = input("Введите числа через пробел:")
# numbers_split = numbers.split()
# numbers_lines = "\n".join(numbers_split)
# print(numbers_lines)

# pi = 31.4159265
# print ("%.4e" % (pi))

# day = 14
# month = 2
# year = 2012
# print("%d.%02d.%d" % (day, month, year))
# print("%d-%02d-%d" % (year, month, day))
# print("%d/%d/%d" % (year, day, month))

# hours = 'HH'
# minutes = 'MM'
# seconds = 'SS'
# print("%s:%s:%s" % (hours, minutes, seconds))
# hours1 = 15
# minutes1 = 23
# seconds1 = 8
# print("%02d:%02d:%02d" % (hours1, minutes1, seconds1))

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[:3:-1])

# L = ['3.3', '4.4', '5.5', '6.6']
# print (list (map (float, L)))

# string = input("Введите числа через пробел:")
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

# string = input("Введите числа через пробел:")
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(float, list_of_strings)) # список чисел
# list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]
# list_of_numbers.append(sum(list_of_numbers))
# print(list_of_numbers)

# L = list(map(float, input("Введите числа через пробел:").split()))
# L[0], L[-1] = L[-1], L[0]
# L.append(sum(L))
# print(L)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))

# Напишите программу, которая получает на вход
# название книги, фамилию автора и год выпуска.
# Полученные данные должны быть преобразованы в словарь
# и в таком представлении выведены в консоль.
# title = input('введите название книги')
# author = input('введите фио автора')
# year = input('введите год издания')
# book = {'title': (title), 'author':(author), 'year':(year)}
# publishing = input('введите название издательства')
# book.append(publishing)
# print(book)

# text = input('ведите текст')
# b=list(set(text))
# print(b, 'количество уникальных символов', len(b))

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = a_set.intersection(b_set)
# print(a_and_b)

# a = input("Введите последовательность чисел: ")
# b = input("Введите последовательность чисел: ")
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b1 = a_set.difference(b_set)
# a_and_b2 = a_set.symmetric_difference(b_set)
# print(a_and_b1)
# print(a_and_b2)

# #программа вывода чисел в порядке возрастания лажа получилась
# a = input("Введите последовательность чисел: ")
# b = input("Введите последовательность чисел: ")
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = a_set.union(b_set)
# с = a_and_b.sort()
# print(c)

# L = ['a', 'b', 'c']
# print(id(L))
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# print(id(a))
# print(id(b))
# d=id(a)-id(b)
# print(d)

# list_1 = ['a', 'b', 'c']
# list_2 = list_1
# list_3 = list(list_1)
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_1 == list_2)
# print(list_1 == list_3)
# print(list_1 is list_2)
# print(list_1 is list_3)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_before==list_id_after)