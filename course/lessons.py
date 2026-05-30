# Структура курса: Псевдокод → Python
# Стиль: Brilliant.org — интерактивное, визуальное, пошаговое обучение

PART1_PSEUDOCODE = [
    {
        "id": "p1_intro",
        "title": "Что такое алгоритм?",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Алгоритм — это последовательность шагов для решения задачи.\n\nПредставь, что ты робот. Каждую команду нужно формулировать чётко и однозначно.\n\n🧠 Пример из жизни — рецепт бутерброда:\n  1. Взять хлеб\n  2. Намазать масло\n  3. Положить сыр\n  4. Накрыть вторым куском хлеба\n\nЭто и есть алгоритм! В программировании мы используем псевдокод — язык, похожий на человеческий, но с чёткими правилами."
            },
            {
                "type": "exercise",
                "question": "Что такое алгоритм?",
                "options": ["Случайный набор команд", "Последовательность шагов для решения задачи", "Язык программирования", "Компьютер"],
                "correct": 1,
                "explanation": "Алгоритм — это именно последовательность чётких шагов."
            },
            {
                "type": "example",
                "data": "Задача: дойти до двери, если есть стулья на пути.\n\nПсевдокод:\n  ПОКА есть препятствие:\n      обойти препятствие\n  ИДТИ к двери"
            }
        ]
    },
    {
        "id": "p1_vars",
        "title": "Переменные и данные",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Переменная — это коробка с именем, в которой хранится значение.\n\n🧮 В псевдокоде:\n  число x = 5\n  имя = 'Анна'\n  возраст = 25\n\nТипы данных в псевдокоде:\n  🔢 Числа (целые, дробные)\n  📝 Строки (текст)\n  ✅ Логические (Истина / Ложь)\n  📦 Списки (набор элементов)"
            },
            {
                "type": "exercise",
                "question": "Какое значение у переменной x после выполнения: x = 10, x = x + 5?",
                "options": ["5", "10", "15", "Ошибка"],
                "correct": 2,
                "explanation": "x = 10, потом x = 10 + 5 = 15"
            },
            {
                "type": "example",
                "data": "Псевдокод: работа с переменными\n\n  сумма = 100\n  скидка = 20\n  итог = сумма - скидка  # 80\n  ВЫВЕСТИ итог"
            }
        ]
    },
    {
        "id": "p1_conditions",
        "title": "Условные конструкции",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Условия позволяют принимать решения.\n\n🔀 В псевдокоде:\n  ЕСЛИ (условие):\n      действие 1\n  ИНАЧЕ:\n      действие 2\n\nОперации сравнения:\n  = равно\n  ≠ не равно\n  > больше\n  < меньше\n  ≥ больше или равно\n  ≤ меньше или равно"
            },
            {
                "type": "exercise",
                "question": "Что выведет этот код? x = 7; ЕСЛИ x > 10: ВЫВЕСТИ 'A' ИНАЧЕ: ВЫВЕСТИ 'B'",
                "options": ["A", "B", "Ничего", "Ошибка"],
                "correct": 1,
                "explanation": "7 > 10 — Ложь, поэтому выполняется блок ИНАЧЕ → 'B'"
            },
            {
                "type": "example",
                "data": "Проверка доступа:\n\n  возраст = 16\n  ЕСЛИ возраст ≥ 18:\n      ВЫВЕСТИ 'Доступ разрешён'\n  ИНАЧЕ:\n      ВЫВЕСТИ 'Доступ запрещён'"
            }
        ]
    },
    {
        "id": "p1_loops",
        "title": "Циклы",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Циклы повторяют действия несколько раз.\n\n🔄 ПОКА (while) — повторять, пока условие истинно:\n  ПОКА (есть шаги):\n      сделать шаг\n\n🔁 ДЛЯ (for) — повторять для каждого элемента:\n  ДЛЯ каждого числа в списке:\n      ВЫВЕСТИ число\n\nПример из жизни: пока есть нерешённые задачи — решать их."
            },
            {
                "type": "exercise",
                "question": "Сколько раз выполнится цикл? i = 1; ПОКА i ≤ 3: ВЫВЕСТИ i; i = i + 1",
                "options": ["2", "3", "4", "Бесконечно"],
                "correct": 1,
                "explanation": "i = 1,2,3 — три итерации. Когда i = 4, условие 4 ≤ 3 — Ложь."
            },
            {
                "type": "example",
                "data": "Подсчёт суммы от 1 до 5:\n\n  сумма = 0\n  i = 1\n  ПОКА (i ≤ 5):\n      сумма = сумма + i\n      i = i + 1\n  ВЫВЕСТИ сумма  # 15"
            },
            {
                "type": "example",
                "data": "Пример, который ты привёл:\n\n  ПОКА (balls exist):\n      move forward"
            }
        ]
    },
    {
        "id": "p1_lists",
        "title": "Списки и перебор",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Список (массив) — набор элементов под одним именем.\n\n📋 В псевдокоде:\n  студенты = ['Анна', 'Борис', 'Вика']\n  оценки = [85, 92, 78]\n\nДоступ к элементам:\n  студенты[0]  # первый элемент: 'Анна'\n  студенты[1]  # второй элемент: 'Борис'\n\nДЛЯ КАЖДОГО студента ИЗ студенты:\n    ВЫВЕСТИ студент"
            },
            {
                "type": "exercise",
                "question": "Чему равно числа[2], если числа = [10, 20, 30, 40]?",
                "options": ["10", "20", "30", "40"],
                "correct": 2,
                "explanation": "Индексация с 0: [0]=10, [1]=20, [2]=30"
            }
        ]
    },
    {
        "id": "p1_functions",
        "title": "Функции",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Функция — это именованный блок кода, который можно вызывать многократно.\n\n⚙️ В псевдокоде:\n  ФУНКЦИЯ имя(параметры):\n      действия\n      ВЕРНУТЬ результат\n\nЗачем?\n  ✅ Не повторять код\n  ✅ Разбивать задачу на части\n  ✅ Упрощать чтение"
            },
            {
                "type": "exercise",
                "question": "Что вернёт функция? ФУНКЦИЯ double(x): ВЕРНУТЬ x * 2. double(5)",
                "options": ["5", "10", "25", "2"],
                "correct": 1,
                "explanation": "double(5) = 5 * 2 = 10"
            },
            {
                "type": "example",
                "data": "Функция проверки чётности:\n\n  ФУНКЦИЯ is_even(n):\n      ЕСЛИ n % 2 = 0:\n          ВЕРНУТЬ Истина\n      ИНАЧЕ:\n          ВЕРНУТЬ Ложь"
            }
        ]
    },
    {
        "id": "p1_algo",
        "title": "Простые алгоритмы",
        "part": 1,
        "content": [
            {
                "type": "text",
                "data": "Применим всё вместе!\n\n🔍 Поиск максимального элемента:\n  числа = [3, 7, 2, 9, 1]\n  макс = числа[0]\n  ДЛЯ КАЖДОГО n ИЗ числа:\n      ЕСЛИ n > макс:\n          макс = n\n  ВЫВЕСТИ макс  # 9\n\n🔢 Подсчёт чётных:\n  count = 0\n  ДЛЯ КАЖДОГО n ИЗ числа:\n      ЕСЛИ n % 2 = 0:\n          count = count + 1\n  ВЫВЕСТИ count"
            },
            {
                "type": "exercise",
                "question": "Чему равен макс? числа = [5, 12, 8, 3]; макс = числа[0]; для каждого n: если n > макс: макс = n",
                "options": ["5", "8", "12", "3"],
                "correct": 2,
                "explanation": "12 — наибольший элемент массива"
            },
            {
                "type": "example",
                "data": "Алгоритм: есть ли число в списке?\n\n  ФУНКЦИЯ contains(список, цель):\n      ДЛЯ КАЖДОГО x ИЗ список:\n          ЕСЛИ x = цель:\n              ВЕРНУТЬ Истина\n      ВЕРНУТЬ Ложь"
            }
        ]
    },
]

PART2_PYTHON = [
    {
        "id": "p2_intro",
        "title": "От псевдокода к Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Теперь переведём псевдокод в настоящий код на Python!\n\n🔄 Псевдокод → Python:\n  ВЫВЕСТИ → print()\n  ВВЕСТИ → input()\n  ЕСЛИ → if\n  ИНАЧЕ → else\n  ПОКА → while\n  ДЛЯ КАЖДОГО → for x in ...\n  ФУНКЦИЯ → def\n  ВЕРНУТЬ → return\n  Истина/Ложь → True/False\n\nPython — читаемый и простой язык. Идеально подходит для начала!"
            },
            {
                "type": "example",
                "data": "Псевдокод:\n  ВЫВЕСТИ 'Привет, мир!'\n\nPython:\n  print('Привет, мир!')"
            },
            {
                "type": "exercise",
                "question": "Как в Python вывести текст?",
                "options": ["output('текст')", "print('текст')", "echo('текст')", "write('текст')"],
                "correct": 1,
                "explanation": "В Python используется функция print()"
            }
        ]
    },
    {
        "id": "p2_vars",
        "title": "Переменные в Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "В Python переменные объявлять не нужно — просто присваивай!\n\n📝 Псевдокод → Python:\n  имя = 'Анна'     →  name = 'Анна'\n  возраст = 25     →  age = 25\n  цена = 99.99     →  price = 99.99\n  активен = Истина →  active = True\n\nТипы данных в Python:\n  int — целые числа\n  float — дробные\n  str — строки\n  bool — True/False\n  list — списки"
            },
            {
                "type": "exercise",
                "question": "Какой тип у переменной x = 3.14?",
                "options": ["int", "float", "str", "bool"],
                "correct": 1,
                "explanation": "3.14 — дробное число, тип float"
            },
            {
                "type": "example",
                "data": "# Псевдокод:\n#   цена = 100\n#   скидка = 20%\n#   итог = цена - (цена * скидка / 100)\n\nprice = 100\ndiscount = 20\ntotal = price - (price * discount / 100)\nprint(total)  # 80.0"
            }
        ]
    },
    {
        "id": "p2_conditions",
        "title": "Условия в Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Псевдокод → Python:\n\n  ЕСЛИ (x > 0):         →  if x > 0:\n      ВЫВЕСТИ 'Пол.'    →      print('Пол.')\n  ИНАЧЕ:                →  else:\n      ВЫВЕСТИ 'Не пол.' →      print('Не пол.')\n  ИНАЧЕ ЕСЛИ (x = 0):   →  elif x == 0:\n      ВЫВЕСТИ 'Ноль'    →      print('Ноль')\n\n⚠️ В Python == это сравнение, = это присваивание!"
            },
            {
                "type": "exercise",
                "question": "Что выведет код? x = 10; if x > 5: print('A') else: print('B')",
                "options": ["A", "B", "AB", "Ошибка"],
                "correct": 0,
                "explanation": "10 > 5 — True, поэтому выполняется блок if → 'A'"
            },
            {
                "type": "example",
                "data": "# Псевдокод:\n#   ЕСЛИ возраст ≥ 18:\n#       ВЫВЕСТИ 'Вход разрешён'\n#   ИНАЧЕ:\n#       ВЫВЕСТИ 'Вход запрещён'\n\nage = 16\nif age >= 18:\n    print('Вход разрешён')\nelse:\n    print('Вход запрещён')"
            }
        ]
    },
    {
        "id": "p2_loops",
        "title": "Циклы в Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Циклы в Python:\n\nПОКА → while:\n# Псевдокод:\n#   ПОКА (i ≤ 5):\n#       ВЫВЕСТИ i\n#       i = i + 1\n\ni = 1\nwhile i <= 5:\n    print(i)\n    i += 1  # i = i + 1\n\nДЛЯ КАЖДОГО → for:\n# Псевдокод:\n#   ДЛЯ КАЖДОГО x ИЗ список:\n#       ВЫВЕСТИ x\n\nfor x in [1, 2, 3]:\n    print(x)\n\nrange(5) → 0, 1, 2, 3, 4\nrange(1, 6) → 1, 2, 3, 4, 5"
            },
            {
                "type": "exercise",
                "question": "Сколько раз выполнится цикл? for i in range(3): print(i)",
                "options": ["2", "3", "4", "5"],
                "correct": 1,
                "explanation": "range(3) даёт 0, 1, 2 — три итерации"
            },
            {
                "type": "example",
                "data": "# Псевдокод (твой пример):\n#   ПОКА (balls exist):\n#       move forward\n\nballs = 3\nwhile balls > 0:\n    print(f'Balls left: {balls}')\n    balls -= 1\n    print('move forward')\nprint('No balls left!')"
            },
            {
                "type": "example",
                "data": "# Псевдокод:\n#   сумма = 0\n#   ДЛЯ i ОТ 1 ДО 5:\n#       сумма = сумма + i\n\ntotal = 0\nfor i in range(1, 6):\n    total += i\nprint(total)  # 15"
            }
        ]
    },
    {
        "id": "p2_lists",
        "title": "Списки в Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Списки (list) — одна из самых мощных структур Python.\n\nСоздание и доступ:\n  students = ['Анна', 'Борис', 'Вика']\n  print(students[0])  # Анна\n  print(students[-1]) # Вика (последний)\n\nМетоды списков:\n  .append(x)  — добавить в конец\n  .remove(x)  — удалить элемент\n  .sort()     — отсортировать\n  len(список) — длина\n\nГенераторы списков:\n  squares = [n**2 for n in range(5)]  # [0, 1, 4, 9, 16]"
            },
            {
                "type": "exercise",
                "question": "Что выведет код? nums = [1, 2, 3]; nums.append(4); print(len(nums))",
                "options": ["3", "4", "5", "Ошибка"],
                "correct": 1,
                "explanation": "После append(4) список = [1,2,3,4], длина = 4"
            },
            {
                "type": "example",
                "data": "# Псевдокод:\n#   студенты = ['Анна', 'Борис', 'Вика']\n#   ДЛЯ КАЖДОГО s ИЗ студенты:\n#       ВЫВЕСТИ s\n\nstudents = ['Анна', 'Борис', 'Вика']\nfor s in students:\n    print(f'Привет, {s}!')"
            }
        ]
    },
    {
        "id": "p2_functions",
        "title": "Функции в Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Псевдокод → Python:\n\n  ФУНКЦИЯ имя(параметры):  →  def name(params):\n      действия               →      actions\n      ВЕРНУТЬ результат      →      return result\n\nПример:\n# Псевдокод:\n#   ФУНКЦИЯ double(x):\n#       ВЕРНУТЬ x * 2\n\ndef double(x):\n    return x * 2\n\nprint(double(5))  # 10"
            },
            {
                "type": "exercise",
                "question": "Что вернёт вызов? def add(a, b): return a + b; print(add(3, 7))",
                "options": ["3", "7", "10", "37"],
                "correct": 2,
                "explanation": "add(3, 7) = 3 + 7 = 10"
            },
            {
                "type": "example",
                "data": "# Псевдокод:\n#   ФУНКЦИЯ max_of_two(a, b):\n#       ЕСЛИ a > b:\n#           ВЕРНУТЬ a\n#       ИНАЧЕ:\n#           ВЕРНУТЬ b\n\ndef max_of_two(a, b):\n    if a > b:\n        return a\n    else:\n        return b\n\nprint(max_of_two(10, 7))  # 10"
            }
        ]
    },
    {
        "id": "p2_algo",
        "title": "Алгоритмы на Python",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Переводим алгоритмы с псевдокода на Python.\n\n🔍 Поиск максимума:\n\ndef find_max(numbers):\n    max_val = numbers[0]\n    for n in numbers:\n        if n > max_val:\n            max_val = n\n    return max_val\n\nprint(find_max([3, 7, 2, 9, 1]))  # 9\n\n✅ Подсчёт чётных:\n\ndef count_even(numbers):\n    count = 0\n    for n in numbers:\n        if n % 2 == 0:\n            count += 1\n    return count\n\nprint(count_even([1, 2, 3, 4, 5, 6]))  # 3"
            },
            {
                "type": "exercise",
                "question": "Что вернёт find_max([10, 5, 20, 8])?",
                "options": ["5", "10", "20", "8"],
                "correct": 2,
                "explanation": "20 — максимальный элемент списка"
            },
            {
                "type": "example",
                "data": "Линейный поиск:\n\ndef contains(lst, target):\n    for x in lst:\n        if x == target:\n            return True\n    return False\n\nprint(contains([1, 2, 3, 4, 5], 3))  # True\nprint(contains([1, 2, 3, 4, 5], 9))  # False"
            }
        ]
    },
    {
        "id": "p2_project",
        "title": "Финальный проект",
        "part": 2,
        "content": [
            {
                "type": "text",
                "data": "Финальный проект: игра «Угадай число»\n\nЗадача: компьютер загадывает число от 1 до 100, игрок угадывает.\n\nПсевдокод:\n  загадать случайное число от 1 до 100\n  ПОКА (игрок не угадал):\n      попросить ввести число\n      ЕСЛИ (число > загаданное):\n          сказать 'Меньше'\n      ИНАЧЕ ЕСЛИ (число < загаданное):\n          сказать 'Больше'\n      ИНАЧЕ:\n          сказать 'Угадал!'\n\nPython:\n  import random\n  secret = random.randint(1, 100)\n  guess = None\n  while guess != secret:\n      guess = int(input('Твой вариант: '))\n      if guess > secret:\n          print('Меньше!')\n      elif guess < secret:\n          print('Больше!')\n      else:\n          print('Угадал!')"
            },
            {
                "type": "exercise",
                "question": "Какая функция Python используется для случайного числа от 1 до 100?",
                "options": ["random.choice(1, 100)", "random.randint(1, 100)", "random.random(100)", "random.rand(1, 100)"],
                "correct": 1,
                "explanation": "random.randint(1, 100) — целое случайное число от 1 до 100"
            },
            {
                "type": "example",
                "data": "Полная программа «Угадай число»:\n\nimport random\n\nsecret = random.randint(1, 100)\nattempts = 0\n\nprint('Я загадал число от 1 до 100. Угадай!')\n\nwhile True:\n    guess = int(input('Твой вариант: '))\n    attempts += 1\n    if guess > secret:\n        print('Меньше!')\n    elif guess < secret:\n        print('Больше!')\n    else:\n        print(f'Угадал за {attempts} попыток!')\n        break"
            }
        ]
    },
]
