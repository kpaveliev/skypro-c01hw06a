"""
В файле messages.txt хранится список сообщений от пользователей
Со стандартного ввода подается поисковая строка.
Найдите сообщения, в которые входит эта строка без учета регистра
"""

# Load messages
filename = '04_messages.txt'
with open(filename, 'r', encoding='utf-8') as file:
    messages = file.read().split('\n')

# Ask for input
user_input = input('Введите слово для поиска: ')

# Calculate results
found_messages = []
found_count = 0

for message in messages:
    if user_input.lower() in message.lower():
        found_messages.append(message)
        found_count += 1

# Show results
print(
    f'Ищем: {user_input}\n'
    f'Найдено сообщений: {found_count}\n'
    f'Сообщения:\n'
    f'{chr(10).join(found_messages)}'
)
