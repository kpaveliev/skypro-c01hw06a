import csv
import utils

# Create dictionary from the file
words_file = '02_dictionary.csv'
data = utils.read_csv(words_file)

# Ask for input and print definitions from dictionary if the word is found
while True:
    user_input = input('Введите слово: ').capitalize()

    if user_input == 'Стоп':
        break

    else:
        if user_input in data:
            print(f'{user_input} - {data[user_input]}')
        else:
            print(f'По вашему запросу ничего не найдено, могу предложить:\n'
                  f'{chr(10).join(data)}'
                  )
