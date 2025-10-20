from pathlib import Path
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def tree_builder(path: Path, prefix: str=''):
    for item in path.iterdir():
        if item.is_dir():
            print(prefix + Fore.BLUE + f"📂 {item.name}" + Style.RESET_ALL)
            tree_builder(item, prefix + "    ")
        else:
            print(prefix + Fore.GREEN + f'📜 {item.name}' + Style.RESET_ALL)
    return

def main():
    dir_path = Path(sys.argv[1])

    if len(sys.argv) < 2:
        print(Fore.RED + 'Потрібно вказати шлях до директорії' + Style.RESET_ALL)
        print(Fore.RED + 'Наприклад python task_3/tree.py /Users/usernname/Desktop/goit-pycore-hw-04/task_2/task_second.py' + Style.RESET_ALL)

    if not dir_path.exists():
        print(Fore.RED + 'Вказаної директорії неіснує' + Style.RESET_ALL)

    if not dir_path.is_dir():
        print(Fore.RED + 'Даний шлях веде не до файлу' + Style.RESET_ALL)

    print(Fore.CYAN + f"\nСтруктура директорії: {dir_path}\n" + Style.RESET_ALL)
    tree_builder(dir_path)
    return

main()
































# def tree_builder(path: Path, prefix: str = ""):
#     for item in path.iterdir():
#         if item.is_dir():
#             print(prefix + Fore.BLUE + f"[Папка] {item.name}" + Style.RESET_ALL)
#             tree_builder(item, prefix + "    ")
#         else:
#             print(prefix + Fore.GREEN + f"- {item.name}" + Style.RESET_ALL)

# def main():
#     if len(sys.argv) < 2:
#         print(Fore.RED + "Помилка: потрібно вказати шлях до директорії!" + Style.RESET_ALL)
#         print("Приклад: python task_3/tree_view.py /Users/yourname/Documents")
#         return

#     dir_path = Path(sys.argv[1])

#     if not dir_path.exists():
#         print(Fore.RED + f"Помилка: шлях '{dir_path}' не існує." + Style.RESET_ALL)
#         return
#     if not dir_path.is_dir():
#         print(Fore.RED + f"Помилка: '{dir_path}' не є директорією." + Style.RESET_ALL)
#         return

#     print(Fore.CYAN + f"\nСтруктура директорії: {dir_path}\n" + Style.RESET_ALL)
#     tree_builder(dir_path)




