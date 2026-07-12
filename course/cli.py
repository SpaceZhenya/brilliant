import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lessons import PART1_PSEUDOCODE, PART2_PYTHON


RESET = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
MAGENTA = '\033[95m'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    clear()
    line = '=' * 44
    print(f'{BOLD}{MAGENTA}{line}{RESET}')
    print(f'{BOLD}{MAGENTA}   ПСЕВДОКОД -> PYTHON{RESET}')
    print(f'{BOLD}{MAGENTA}   Интерактивный курс (в стиле Brilliant){RESET}')
    print(f'{BOLD}{MAGENTA}{line}{RESET}')
    print()


def show_lesson(lesson):
    input(f'{YELLOW}Нажми Enter, чтобы начать урок: {lesson["title"]}{RESET}')
    print()
    for block in lesson['content']:
        if block['type'] == 'text':
            print(f'{CYAN}{block["data"]}{RESET}')
            input(f'\n{YELLOW}Нажми Enter для продолжения...{RESET}')
            print()

        elif block['type'] == 'example':
            print(f'{GREEN}[Пример]:{RESET}')
            print(f'{GREEN}{block["data"]}{RESET}')
            input(f'\n{YELLOW}Нажми Enter для продолжения...{RESET}')
            print()

        elif block['type'] == 'exercise':
            while True:
                print(f'{YELLOW}[?] Вопрос: {block["question"]}{RESET}')
                for i, opt in enumerate(block['options']):
                    marker = f'{BOLD}→{RESET}' if i == block['correct'] else ' '
                    print(f'  [{i + 1}] {opt}')

                try:
                    choice = input(f'\n{BOLD}Твой ответ (1-{len(block["options"])}): {RESET}')
                    if choice.lower() == 'q':
                        print(f'{YELLOW}Правильный ответ: {block["options"][block["correct"]]}{RESET}')
                        break
                    idx = int(choice) - 1
                    if idx == block['correct']:
                        print(f'\n{GREEN}[+] Верно! {block["explanation"]}{RESET}')
                        break
                    else:
                        print(f'\n{RED}[-] Неверно. Попробуй ещё раз.{RESET}')
                        input(f'{YELLOW}Нажми Enter...{RESET}')
                        print()
                except (ValueError, IndexError):
                    print(f'\n{RED}Введи число от 1 до {len(block["options"])}.{RESET}')
                    input(f'{YELLOW}Нажми Enter...{RESET}')
                    print()

            input(f'\n{YELLOW}Нажми Enter для продолжения...{RESET}')
            print()

        elif block['type'] == 'order':
            print(f'{MAGENTA}[Упорядочивание]{RESET}')
            print(f'{CYAN}{block["question"]}{RESET}')
            items = block['items']
            correct = block['correct']
            print(f'\n{YELLOW}Элементы:{RESET}')
            for i, item in enumerate(items, 1):
                print(f'  {i}. {item}')
            print(f'\n{GREEN}Правильный порядок:{RESET}')
            ordered = [items[i] for i in correct]
            for i, item in enumerate(ordered, 1):
                print(f'  {i}. {item}')
            input(f'\n{YELLOW}Нажми Enter для продолжения...{RESET}')
            print()

        elif block['type'] == 'code':
            print(f'{BLUE}[Кодинг]{RESET}')
            print(f'{CYAN}{block["task"]}{RESET}')
            if 'hint' in block:
                print(f'\n{YELLOW}Подсказка: {block["hint"]}{RESET}')
            print(f'\n{GREEN}Начальный код:{RESET}')
            print(f'{BOLD}{block.get("defaultCode", "")}{RESET}')
            input(f'\n{YELLOW}Нажми Enter для продолжения...{RESET}')
            print()

    print(f'{GREEN}{BOLD}[OK] Урок "{lesson["title"]}" завершён!{RESET}')
    input(f'\n{YELLOW}Нажми Enter, чтобы вернуться в меню...{RESET}')


def show_progress(completed):
    if not completed:
        return f'{RED}0% пройдено{RESET}'
    total = len(PART1_PSEUDOCODE) + len(PART2_PYTHON)
    done = len(completed)
    pct = int(done / total * 100)
    bar = '#' * (pct // 10) + '-' * (10 - pct // 10)
    return f'{bar} {done}/{total} ({pct}%)'


def main():
    completed = set()

    try:
        import json
        save_path = os.path.join(os.path.dirname(__file__), '.progress.json')
        if os.path.exists(save_path):
            with open(save_path) as f:
                completed = set(json.load(f))
    except:
        pass

    all_lessons = [(1, lesson) for lesson in PART1_PSEUDOCODE] + \
                  [(2, lesson) for lesson in PART2_PYTHON]

    while True:
        print_header()
        print(f'{BOLD}ТВОЙ ПРОГРЕСС:{RESET} {show_progress(completed)}\n')

        print(f'{BOLD}{CYAN}--- ЧАСТЬ 1: ПСЕВДОКОД ---{RESET}')
        for i, lesson in enumerate(PART1_PSEUDOCODE, 1):
            mark = f'{GREEN}[x]{RESET}' if lesson['id'] in completed else f'{RED}[ ]{RESET}'
            print(f'  {mark} 1.{i} {lesson["title"]}')

        print(f'\n{BOLD}{CYAN}--- ЧАСТЬ 2: PYTHON ---{RESET}')
        for i, lesson in enumerate(PART2_PYTHON, 1):
            mark = f'{GREEN}[x]{RESET}' if lesson['id'] in completed else f'{RED}[ ]{RESET}'
            print(f'  {mark} 2.{i} {lesson["title"]}')

        print(f'\n  {BOLD}{YELLOW}q{RESET} — Выйти из курса')

        choice = input(f'\n{BOLD}Выбери номер урока (например 1.3 или 2.1): {RESET}').strip()

        if choice.lower() == 'q':
            print(f'\n{GREEN}До встречи! Продолжай учиться!{RESET}')
            break

        try:
            parts = choice.split('.')
            part = int(parts[0])
            num = int(parts[1]) - 1

            if part == 1 and 0 <= num < len(PART1_PSEUDOCODE):
                lesson = PART1_PSEUDOCODE[num]
                show_lesson(lesson)
                completed.add(lesson['id'])
            elif part == 2 and 0 <= num < len(PART2_PYTHON):
                lesson = PART2_PYTHON[num]
                show_lesson(lesson)
                completed.add(lesson['id'])
            else:
                print(f'{RED}Неверный номер урока.{RESET}')
                input(f'{YELLOW}Нажми Enter...{RESET}')
        except (ValueError, IndexError):
            print(f'{RED}Некорректный ввод. Используй формат: 1.1, 2.3 и т.д.{RESET}')
            input(f'{YELLOW}Нажми Enter...{RESET}')

        try:
            with open(save_path, 'w') as f:
                json.dump(list(completed), f)
        except:
            pass


if __name__ == '__main__':
    main()
