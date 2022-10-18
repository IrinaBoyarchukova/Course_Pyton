# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
#    ключи — первые буквы имён, значения — списки, содержащие имена,
#    начинающиеся с соответствующей буквы.

#  ________________________________________________________ 1 вариант

def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

#  ________________________________________________________ 2 вариант
from itertools import groupby


def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))


#  ________________________________________________________ 3 вариант

def thesaurus(*args):
    if "" not in args:
        return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
    return "Error"


thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
          'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')

