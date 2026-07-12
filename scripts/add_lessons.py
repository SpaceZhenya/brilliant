import json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
data_path = os.path.join(os.path.dirname(__file__), '..', 'course', 'data.json')

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_lessons = [
    {
        "id": "p2_strings",
        "title": "Строки в Python",
        "icon": "\U0001f4dd",
        "subtitle": "Урок 2.9",
        "desc": "Погрузись в мир строк в Python \u2014 мощный инструмент для работы с текстом.",
        "skills": [
            "Работать с методами строк: upper, split, join",
            "Использовать f-строки и форматирование",
            "Применять срезы и индексацию к строкам"
        ],
        "content": [
            {
                "type": "text",
                "data": "Строки в Python \u2014 это не просто текст. Это мощный инструмент с множеством встроенных методов.\n\nОсновные методы строк:\n  text.upper()      \u2014 все заглавные\n  text.lower()      \u2014 все строчные\n  text.split()      \u2014 разбить по пробелам в список\n  ' '.join(list)    \u2014 склеить список в строку\n  text.strip()      \u2014 удалить пробелы по краям\n  text.replace(a,b) \u2014 заменить a на b\n  len(text)         \u2014 длина строки"
            },
            {
                "type": "example",
                "data": "# Работа со строками\nname = 'python'\nprint(name.upper())  # PYTHON\nprint(name[0])       # p\nprint(name[-1])      # n\nprint(name[1:4])     # yth\n\n# Split и join\ntext = 'яблоко, банан, виноград'\nwords = text.split(', ')\nprint(words)  # ['яблоко', 'банан', 'виноград']\nprint(' | '.join(words))  # яблоко | банан | виноград"
            },
            {
                "type": "exercise",
                "question": "Что вернёт 'Hello World'.upper()?",
                "options": ["hello world", "HELLO WORLD", "Hello World", "HELLO world"],
                "correct": 1,
                "explanation": "upper() преобразует все символы в заглавные."
            },
            {
                "type": "code",
                "task": "Напиши код, который разбивает строку 'a b c d' по пробелам и выводит третий элемент.",
                "hint": "Используй .split() и индекс [2]",
                "defaultCode": "text = 'a b c d'\nwords = text.split()\nprint(words[2])",
                "expectedOutput": "c"
            }
        ]
    },
    {
        "id": "p2_dicts",
        "title": "Словари в Python",
        "icon": "\U0001f4ca",
        "subtitle": "Урок 2.10",
        "desc": "Словари \u2014 это хранение данных по принципу ключ-значение. Мощная и гибкая структура данных.",
        "skills": [
            "Создавать словари и обращаться по ключу",
            "Использовать методы .keys(), .values(), .items()",
            "Перебирать словарь в цикле"
        ],
        "content": [
            {
                "type": "text",
                "data": "Словарь (dict) хранит пары ключ-значение.\n\nВместо числового индекса мы используем ключ \u2014 это может быть число, строка или другой неизменяемый тип.\n\nПример:\n  student = {\n      'name': 'Анна',\n      'age': 20,\n      'grade': 4.8\n  }\n  print(student['name'])  # Анна\n  print(student['age'])   # 20"
            },
            {
                "type": "example",
                "data": "# Работа со словарём\nuser = {'name': 'Иван', 'age': 25, 'city': 'Москва'}\n\nprint(user.keys())    # dict_keys(['name', 'age', 'city'])\nprint(user.values())  # dict_values(['Иван', 25, 'Москва'])\n\n# Добавить новый ключ\nuser['email'] = 'ivan@mail.ru'\n\n# Перебор\nfor key, value in user.items():\n    print(f'{key}: {value}')"
            },
            {
                "type": "exercise",
                "question": "Что выведет код? d = {'a': 1, 'b': 2}; print(d['a'])",
                "options": ["'a'", "1", "2", "Ошибку"],
                "correct": 1,
                "explanation": "d['a'] возвращает значение по ключу 'a' \u2014 это 1."
            },
            {
                "type": "code",
                "task": "Создай словарь с ключами 'name', 'age' и выведи значение name.",
                "hint": "my_dict = {'name': '...', 'age': ...}",
                "defaultCode": "person = {'name': 'Мария', 'age': 22}\nprint(person['name'])",
                "expectedOutput": "Мария"
            }
        ]
    }
]

data['part2'].extend(new_lessons)

with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added 2 new lessons. Part 2 now has {len(data['part2'])} lessons")
print("Done!")
