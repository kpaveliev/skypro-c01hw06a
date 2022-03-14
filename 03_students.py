import utils

# Create dictionary from the file
scores_file = '03_scores.csv'
passed_file = '03_passed.txt'
failed_file = '03_failed.txt'

data = utils.read_csv(scores_file)

# Create passed, failed lists
passed = []
failed = []

for student, score in data.items():
    if int(score) >= 75:
        passed.append(student)
    else:
        failed.append(student)

# Write result into files
utils.write_to_txt(passed_file, passed)
utils.write_to_txt(failed_file, failed)



# # Ask for input and print definitions from dictionary if the word is found
# while True:
#     user_input = input('Введите слово: ').capitalize()
#
#     if user_input == 'Стоп':
#         break
#
#     else:
#         if user_input in data:
#             print(f'{user_input} - {data[user_input]}')
#         else:
#             print(f'По вашему запросу ничего не найдено, могу предложить:\n'
#                   f'{chr(10).join(data)}'
#                   )
