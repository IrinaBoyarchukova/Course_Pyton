# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
def find_list(n: int):
    people = [input('Введите имя: ') for _ in range(n)]
    return people


def find_list2(list_p: list):
    result = {}
    for name in list_p:
        key = name[0]
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


n = int(input('Cколько у вас сотрудников? '))
name = find_list(n)
print(name)
print(find_list2(name))