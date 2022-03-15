"""
В файле todo.txt хранится список дел
При запуске программа выводит по одному еще не сделанные дела и спрашивает, выполнено ли оно
Пользователь отвечает y/n, и программа записывает новый список дел
"""

# Load todo list
file_initial = '06_todo.txt'
file_result = '06_todo_new.txt'

with open(file_initial, 'r', encoding='utf-8') as file:
    data = file.readlines()
    # todolist = [line.strip('\n') for line in data]
    todolist = [line.strip('\n').split(': ') for line in data]

print(todolist)

# Show status
done = 0
total = 0

for line in todolist:
    total += 1
    if 'DONE' in line[1]:
        done += 1

print(f'В списке {total} дел\n'
      f'Сделано {done}/{total}\n'
      f'Давай пройдемся по твоим делам!\n')

# Ask done/not done
for line in todolist:
    if line[1] != 'DONE':
        user_input = input(f'{line[0]} - сделано? (y/n)\n').lower()
        if user_input not in ['y', 'n']:
            user_input = input(f'Принимаются только указанные значения, '
                               f'повторите ввод (y/n),\n')
        else:
            if user_input == 'y':
                line[1] = 'DONE'
            elif user_input == 'n':
                line[1] = 'TODO'

# Write results into file
with open(file_result, 'w', encoding='utf-8') as file:
    for line in todolist:
        file.writelines(': '.join(line) + '\n')
