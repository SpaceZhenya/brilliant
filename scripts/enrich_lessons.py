import json, os, copy

data_path = os.path.join(os.path.dirname(__file__), '..', 'course', 'data.json')
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# New exercises to add per lesson (id -> list of new blocks)
new_content = {
    "p1_intro": [
        {"type": "order", "question": "Расположи шаги алгоритма «Перейти дорогу»:", "items": ["Посмотреть налево", "Посмотреть направо", "Если машин нет — перейти", "Если машины есть — подождать"], "correct": [0, 1, 2, 3]},
        {"type": "code", "task": "Напиши программу, которая выводит твоё любимое число.", "hint": "print(твоё_число)", "defaultCode": "# Выведи любимое число\nprint(42)", "expectedOutput": "42"},
        {"type": "exercise", "question": "Как называется свойство алгоритма «разбит на отдельные шаги»?", "options": ["Понятность", "Дискретность", "Результативность", "Массовость"], "correct": 1, "explanation": "Дискретность — алгоритм состоит из отдельных, неделимых шагов."}
    ],
    "p1_vars": [
        {"type": "exercise", "question": "Что будет в переменной y? y = 10; y = y * 2;", "options": ["10", "12", "20", "102"], "correct": 2, "explanation": "y = 10 * 2 = 20. Старое значение 10 перезаписывается."},
        {"type": "code", "task": "Создай две переменные a=5 и b=3, выведи их сумму.", "hint": "print(a + b)", "defaultCode": "a = 5\nb = 3\nprint(a + b)", "expectedOutput": "8"}
    ],
    "p1_conditions": [
        {"type": "exercise", "question": "Сколько веток в конструкции ЕСЛИ-ИНАЧЕ ЕСЛИ-ИНАЧЕ с двумя ИНАЧЕ ЕСЛИ?", "options": ["2", "3", "4", "5"], "correct": 2, "explanation": "ЕСЛИ + 2×ИНАЧЕ ЕСЛИ + ИНАЧЕ = 4 ветки."},
        {"type": "code", "task": "Напиши псевдокод: если число > 0, выведи ' Positive', иначе 'Negative'.", "hint": "Используй ЕСЛИ и ИНАЧЕ", "defaultCode": "x = 5\nif x > 0:\n    print('Positive')\nelse:\n    print('Negative')", "expectedOutput": "Positive"}
    ],
    "p1_loops": [
        {"type": "exercise", "question": "Что выведет код? for i in range(3): print('Hi')", "options": ["Hi (1 раз)", "Hi Hi Hi (3 раза)", "0 1 2", "Ошибка"], "correct": 1, "explanation": "Цикл выполняется 3 раза, каждый раз выводит 'Hi'."},
        {"type": "code", "task": "Напиши цикл, который выводит 'Hello' 3 раза.", "hint": "for i in range(3): print('Hello')", "defaultCode": "for i in range(3):\n    print('Hello')", "expectedOutput": "Hello\nHello\nHello"}
    ],
    "p1_lists": [
        {"type": "exercise", "question": "Дан список fruits = ['apple', 'banana']. Чему равен fruits[0]?", "options": ["'apple'", "'banana'", "0", "Ошибка"], "correct": 0, "explanation": "Индексация с 0: fruits[0] = 'apple'."},
        {"type": "code", "task": "Создай список цветов ['red', 'green', 'blue'] и выведи второй элемент.", "hint": "colours[1]", "defaultCode": "colours = ['red', 'green', 'blue']\nprint(colours[1])", "expectedOutput": "green"}
    ],
    "p1_functions": [
        {"type": "exercise", "question": "Что вернёт max_of_two(3, 8) если она возвращает бОльшее число?", "options": ["3", "5", "8", "11"], "correct": 2, "explanation": "8 больше 3, поэтому возвращается 8."},
        {"type": "code", "task": "Напиши функцию greet(name), которая выводит 'Hello, ' + name.", "hint": "def greet(name): ...", "defaultCode": "def greet(name):\n    print('Hello, ' + name)\n\ngreet('Alice')", "expectedOutput": "Hello, Alice"}
    ],
    "p1_algo": [
        {"type": "exercise", "question": "Сколько сравнений сделает find_max на списке из 5 элементов?", "options": ["4", "5", "6", "10"], "correct": 1, "explanation": "Первый элемент берём как максимум, затем сравниваем с каждым из оставшихся 4 — всего 4 сравнения. Но в коде мы сравниваем все 5."},
        {"type": "code", "task": "Напиши функцию sum_list(numbers), которая возвращает сумму всех чисел списка.", "hint": "def sum_list(nums): total = 0; for n in nums: total += n; return total", "defaultCode": "def sum_list(numbers):\n    total = 0\n    for n in numbers:\n        total += n\n    return total\n\nprint(sum_list([1, 2, 3, 4, 5]))", "expectedOutput": "15"}
    ],
    "p2_intro": [
        {"type": "exercise", "question": "Какое ключевое слово Python для определения функции?", "options": ["func", "def", "function", "define"], "correct": 1, "explanation": "В Python функции определяются через def."},
        {"type": "code", "task": "Выведи на экран 'Python is fun!' три раза, каждый на новой строке.", "hint": "print() три раза", "defaultCode": "for i in range(3):\n    print('Python is fun!')", "expectedOutput": "Python is fun!\nPython is fun!\nPython is fun!"}
    ],
    "p2_vars": [
        {"type": "exercise", "question": "Какая функция преобразует строку '123' в число?", "options": ["str()", "int()", "float()", "bool()"], "correct": 1, "explanation": "int('123') = 123. str() делает наоборот."},
        {"type": "code", "task": "Создай переменную pi = 3.14159 и выведи её с точностью 2 знака.", "hint": "print(f'{pi:.2f}')", "defaultCode": "pi = 3.14159\nprint(f'{pi:.2f}')", "expectedOutput": "3.14"}
    ],
    "p2_conditions": [
        {"type": "exercise", "question": "Что выведет код? x = 0; if x: print('Yes') else: print('No')", "options": ["Yes", "No", "0", "Ошибка"], "correct": 1, "explanation": "0 — это False (ложь) в логическом контексте. Выполняется else → 'No'."},
        {"type": "code", "task": "Напиши код, который проверяет, является ли число чётным.", "hint": "n % 2 == 0", "defaultCode": "n = 8\nif n % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')", "expectedOutput": "Even"}
    ],
    "p2_loops": [
        {"type": "exercise", "question": "Что вернёт range(5, 10)?", "options": ["[5,6,7,8,9,10]", "[5,6,7,8,9]", "[0,1,2,3,4]", "Ошибка"], "correct": 1, "explanation": "range(5, 10) от 5 до 9 включительно."},
        {"type": "code", "task": "Выведи все чётные числа от 0 до 10.", "hint": "for i in range(0, 11, 2)", "defaultCode": "for i in range(0, 11, 2):\n    print(i)", "expectedOutput": "0\n2\n4\n6\n8\n10"}
    ],
    "p2_lists": [
        {"type": "exercise", "question": "Какой метод добавляет элемент в конец списка?", "options": [".add()", ".append()", ".insert()", ".push()"], "correct": 1, "explanation": ".append(x) добавляет x в конец списка."},
        {"type": "code", "task": "Создай список чисел [5, 2, 8, 1, 9], отсортируй его и выведи.", "hint": "nums.sort()", "defaultCode": "nums = [5, 2, 8, 1, 9]\nnums.sort()\nprint(nums)", "expectedOutput": "[1, 2, 5, 8, 9]"}
    ],
    "p2_functions": [
        {"type": "exercise", "question": "Что вернёт функция если в ней нет return?", "options": ["0", "False", "None", "Ошибку"], "correct": 2, "explanation": "Функция без return возвращает None."},
        {"type": "code", "task": "Напиши функцию, которая принимает список и возвращает его длину.", "hint": "def my_len(lst): return len(lst)", "defaultCode": "def my_len(lst):\n    return len(lst)\n\nprint(my_len([10, 20, 30]))", "expectedOutput": "3"}
    ],
    "p2_algo": [
        {"type": "exercise", "question": "Какова сложность алгоритма поиска максимума?", "options": ["O(1)", "O(n)", "O(n\u00b2)", "O(log n)"], "correct": 1, "explanation": "Нужно просмотреть каждый элемент один раз — O(n)."},
        {"type": "code", "task": "Напиши функцию, которая считает количество нечётных чисел в списке.", "hint": "n % 2 != 0", "defaultCode": "def count_odd(numbers):\n    count = 0\n    for n in numbers:\n        if n % 2 != 0:\n            count += 1\n    return count\n\nprint(count_odd([1, 2, 3, 4, 5, 6]))", "expectedOutput": "3"}
    ],
    "p2_project": [
        {"type": "exercise", "question": "Что делает random.randint(1, 10)?", "options": ["Случайное число от 0 до 10", "Случайное целое от 1 до 10", "10 случайных чисел", "Ошибка"], "correct": 1, "explanation": "randint(1,10) — случайное целое число от 1 до 10 включительно."},
        {"type": "code", "task": "Напиши код, который симулирует бросок кубика (1-6) и выводит результат.", "hint": "import random; print(random.randint(1, 6))", "defaultCode": "import random\nresult = random.randint(1, 6)\nprint('You rolled:', result)", "expectedOutput": "You rolled:"}
    ],
    "p2_strings": [
        {"type": "exercise", "question": "Что вернёт 'hello'.upper()?", "options": ["'hello'", "'HELLO'", "'Hello'", "'hELLO'"], "correct": 1, "explanation": "upper() делает все буквы заглавными."},
        {"type": "exercise", "question": "Как разбить строку по пробелам?", "options": [".split()", ".divide()", ".cut()", ".break()"], "correct": 0, "explanation": ".split() разбивает строку по пробелам/разделителю."},
        {"type": "order", "question": "Расположи шаги для получения '!dlroW olleH':", "items": ["text = 'Hello World'", "text = text[::-1]", "print(text)"], "correct": [0, 1, 2]}
    ],
    "p2_dicts": [
        {"type": "exercise", "question": "Как обратиться к значению по ключу 'name' в словаре d?", "options": ["d.name", "d['name']", "d{'name'}", "d(name)"], "correct": 1, "explanation": "В Python: d['name'] или d.get('name')."},
        {"type": "exercise", "question": "Что вернёт len({'a': 1, 'b': 2, 'c': 3})?", "options": ["3", "6", "2", "Ошибка"], "correct": 0, "explanation": "В словаре 3 пары ключ-значение."},
        {"type": "order", "question": "Расположи шаги работы со словарём:", "items": ["d = {'x': 10, 'y': 20}", "d['z'] = 30", "print(d['y'])"], "correct": [0, 1, 2]}
    ]
}

# Engaging intro rewrites (first text block of each lesson)
intro_stories = {
    "p1_intro": "\U0001f9e0 Представь: ты — шеф-повар, а алгоритм — это твой фирменный рецепт.\n\nБез чёткого рецепта гости останутся голодными. Без алгоритма — компьютер не поймёт, что делать.\n\nАлгоритм — это последовательность шагов для решения задачи. Звучит сухо? А на деле это магия, которая превращает «хочу» в «сделано».\n\nПример: рецепт бутерброда — это алгоритм:\n  1. \U0001f95a Взять хлеб\n  2. \U0001f9c0 Намазать масло\n  3. \U0001f9c0 Положить сыр\n  4. \U0001f95a Накрыть вторым куском\n\nВ программировании мы используем псевдокод — язык, похожий на человеческий, но строгий и точный, как армейский устав.",
    "p1_vars": "\U0001f4e6 Переменная — это коробка с именем. Ты можешь положить в неё число, текст или что угодно, подписать коробку и в любой момент заглянуть внутрь.\n\nВ псевдокоде:\n  x = 5          \u2014 положили число 5 в коробку «x»\n  name = 'Анна'  \u2014 положили текст «Анна» в коробку «name»\n\nИмя переменной придумываешь ты. Хорошее имя — как понятная надпись на коробке: сразу ясно, что внутри. sum, name, age — отлично. a, b, c — в мусорку.",
    "p1_conditions": "\U0001f9d1\u200d\u26a1\ufe0f Твоя программа — это робот, который стоит на развилке. Налево пойдёшь — число проверишь, направо — строку выведешь.\n\nУсловия (ветвления) — то, что делает код «живым». Без них программа просто выполняет команды сверху вниз, как робот-зомби. С условиями она начинает ДУМАТЬ.\n\n  ЕСЛИ (гость голоден):\n      накормить\n  ИНАЧЕ:\n      предложить чай\n\nВот это уже похоже на искусственный интеллект!",
    "p1_loops": "\U0001f504 Циклы — суперсила программиста.\n\nХочешь вывести «Привет» 100 раз? Не нужно копировать print() сто строк. Цикл сделает это за 3 строки.\n\n  ПОКА (есть голодные люди):\n      готовить пиццу\n\nКомпьютер обожает повторять одно и то же. Люди — нет. Циклы позволяют человеку один раз объяснить, что делать, а компьютер сделает это миллион раз.",
    "p1_lists": "\U0001f4cb Список — это как рюкзак: туда можно сложить много вещей и обращаться к каждой по номеру.\n\n  студенты = ['Анна', 'Борис', 'Вика']\n  оценки = [85, 92, 78, 95]\n\nНомер элемента называется индексом. И да, программисты считают с 0. Почему? Потому что компьютер говорит «первый элемент находится на нулевом месте от начала». Привыкнешь!",
    "p1_functions": "\U0001f528 Функция — это твой личный инструмент. Хочешь — сделай дрель, хочешь — отвёртку.\n\nФункция — это именованный блок кода, который можно вызывать снова и снова:\n\n  ФУНКЦИЯ make_sandwich(хлеб, начинка):\n      ...собрать бутерброд...\n      ВЕРНУТЬ бутерброд\n\n  make_sandwich('ржаной', 'сыр')  \u2014 готов!\n  make_sandwich('белый', 'колбаса')  \u2014 готов!\n\nОдин раз написал — пользуешься вечно. Это и есть магия программирования.",
    "p1_algo": "\U0001f50d Теперь, когда у нас есть переменные, условия, циклы и функции, мы можем собрать из них НАСТОЯЩИЕ АЛГОРИТМЫ.\n\nПоиск максимума, подсчёт элементов, проверка наличия — это строительные блоки любой программы. Освоив их, ты сможешь написать что угодно: от калькулятора до поисковой системы.\n\nДержи алгоритм поиска максимума:\n  \U0001f4a1 Берём первый элемент как «чемпиона»\n  \U0001f50d Проходим по всем остальным\n  \U0001f91c Если находим больше — чемпион меняется\n  \U0001f3c6 В конце — чемпион объявляется максимумом",
    "p2_intro": "\U0001f40d Псевдокод — это чертёж. Python — настоящий дом.\n\nТы уже умеешь проектировать алгоритмы. Теперь научимся воплощать их в жизнь с помощью Python — самого популярного языка для начинающих.\n\n  Псевдокод          Python\n  ВЫВЕСТИ     \u2192    print()\n  ЕСЛИ        \u2192    if\n  ПОКА        \u2192    while\n\nPython читается почти как английский. Ты будешь писать код, который выглядит как обычный текст!",
    "p2_vars": "\U0001f4e6 В Python не нужно объявлять тип переменной — просто напиши имя и значение.\n\n  name = 'Анна'    \u2014 str\n  age = 25         \u2014 int\n  price = 99.99    \u2014 float\n  active = True    \u2014 bool\n\nPython сам понимает, что ты имеешь в виду. Хочешь число — пожалуйста. Хочешь текст — без проблем. Это называется динамическая типизация.",
    "p2_conditions": "\U0001f9e0 Python делает условия максимально читаемыми.\n\n  if age >= 18:\n      print('Welcome')\n  else:\n      print('Access denied')\n\nДвоеточие, отступы, никаких скобок и КОНЕЦ ЕСЛИ. Красота! В Python код выглядит так же, как ты его объясняешь другу.",
    "p2_loops": "\U0001f504 В Python циклы стали ещё элегантнее.\n\n  for i in range(5):\n      print(i)  # 0, 1, 2, 3, 4\n\n  while money > 0:\n      buy_coffee()\n      money -= 1\n\nRange, break, continue — у Python богатый арсенал для управления повторениями.",
    "p2_lists": "\U0001f4cb Списки в Python — это швейцарский нож структур данных.\n\n  nums = [1, 2, 3]\n  nums.append(4)     # [1, 2, 3, 4]\n  nums.sort()        # [1, 2, 3, 4]\n  nums[::-1]         # [4, 3, 2, 1]\n  len(nums)          # 4\n\nСрезы, методы, генераторы — Python даёт тебе всё, чтобы работать с коллекциями как профи.",
    "p2_functions": "\U0001f528 В Python функции создаются через def. Просто и элегантно.\n\n  def greet(name):\n      return f'Hello, {name}!'\n\n  print(greet('World'))  # Hello, World!\n\nПараметры по умолчанию, именованные аргументы, return нескольких значений — Python делает функции удобными и гибкими.",
    "p2_algo": "\U0001f4a1 Переносим наши алгоритмы с псевдокода на Python.\n\nТо, что мы писали на псевдокоде, в Python выглядит почти так же! Разница только в синтаксисе.\n\n  # Псевдокод:\n  #   ДЛЯ КАЖДОГО n ИЗ числа:\n  #       ЕСЛИ n > макс:\n  #           макс = n\n\n  # Python:\n  for n in numbers:\n      if n > max_val:\n          max_val = n\n\nВидишь? Почти один в один!",
    "p2_project": "\U0001f3ae Финальный проект: игра «Угадай число».\n\nКомпьютер загадывает число, ты угадываешь. Каждая попытка — подсказка: «Больше» или «Меньше».\n\nЭто первая игра, которую пишет каждый программист. Простая, но в ней есть всё: переменные, циклы, условия, ввод/вывод. И азарт!",
    "p2_strings": "\U0001f4dd Строки — это не просто текст. Это мощный инструмент с десятками встроенных функций.\n\n  'hello'.upper()      \u2192 'HELLO'\n  'a b c'.split()      \u2192 ['a', 'b', 'c']\n  '-'.join(['1','2'])  \u2192 '1-2'\n  'Hello'[0]           \u2192 'H'\n  'Hello'[1:4]         \u2192 'ell'\n\nСтроки в Python — как нож шеф-повара: с их помощью можно нарезать, клеить, чистить и украшать данные.",
    "p2_dicts": "\U0001f4ca Словарь — это как телефонная книга: по имени (ключу) находишь номер (значение).\n\n  student = {\n      'name': 'Анна',\n      'age': 20,\n      'grade': 4.8\n  }\n  print(student['name'])  # Анна\n\nВ реальном мире почти всё — пары ключ-значение: пользователи и их профили, товары и цены, страны и столицы.",
}

# Rewrite intro texts
for part_key in ['part1', 'part2']:
    for lesson in data[part_key]:
        lid = lesson['id']
        if lid in intro_stories:
            for block in lesson['content']:
                if block['type'] == 'text':
                    block['data'] = intro_stories[lid]
                    break

# Add new interactive blocks
for part_key in ['part1', 'part2']:
    for lesson in data[part_key]:
        lid = lesson['id']
        if lid in new_content:
            lesson['content'].extend(new_content[lid])

with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Stats
for part_key in ['part1', 'part2']:
    for lesson in data[part_key]:
        types = [b['type'] for b in lesson['content']]
        counts = dict((t, types.count(t)) for t in set(types))
        print(f"  {lesson['id']}: {len(lesson['content'])} blocks, {counts}")

total = sum(len(p) for p in [data['part1'], data['part2']])
all_blocks = sum(len(l['content']) for l in data['part1'] + data['part2'])
print(f"\nTotal: {total} lessons, {all_blocks} blocks")
print("Done!")
