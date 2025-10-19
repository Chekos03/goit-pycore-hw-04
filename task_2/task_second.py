from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, mode='r',encoding='utf-8') as file: 
            cats = []
            for line in file:
                id, name , years = line.strip().split(',')
                cats.append({'id':id, 'name':name, 'years':years })
            print(cats)
        return
    except FileNotFoundError:
        print(f'Помилка файл {path} не знайдено')

path = Path('task_2/cats_info.txt')
cats_info = get_cats_info(path)
print(cats_info)


