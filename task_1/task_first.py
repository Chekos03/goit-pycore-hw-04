from pathlib import Path
path = Path('task_1/salary.txt')
def total_salary(path):
    try:
        with open(path,mode='r',encoding='utf-8') as file:
            splited_text = [i.strip().split(',') for i in file.readlines()]
            average_salary = 0
            count_of_itter = 0
            total_sum = 0 
            for i in splited_text:
                count_of_itter +=1
                for x in i:
                    if x.isdigit():
                        total_sum = total_sum + int(x)
            average_salary = total_sum / count_of_itter
        return total_sum , average_salary
    except FileNotFoundError:
        print (f'Помилка файл {path} не знайдено')

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
