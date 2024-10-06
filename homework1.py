'''Практическое задание по уроку "Строки и индексация строк"
 
Задача:
Выполните следующие действия в PyCharm:
В переменную example запишите любую строку.
Выведите на экран(в консоль) первый символ этой строки.
Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
Выведите на экран(в консоль) это слово наоборот.
Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')

Вводные данные:
example = 'Топинамбур'
Вывод на экран(в консоль):
Т
р
амбур
рубманипоТ
оиабр'''

example = 'Топинамбур'
print(example[0:1])
print(example[::-10])
print(example[5:])
print(example[::-1])
print(example[1:10:2])
