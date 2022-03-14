import utils

miles_file = '01_miles.txt'
kms_file = '01_kilometers.txt'

# Read file and create list with miles values
with open(miles_file, 'r', encoding='utf-8') as file:
    miles_values = file.read().split()

# Function to convert miles to kilometers with n decimal places
def miles_kms_converter(miles_value, decimals=2):
    kms_value = round(float(miles_value) * 1.60934, decimals)
    return kms_value

# Create list with values converted from miles to kilometers
kms_values = []

for value in miles_values:
    kms_values.append(miles_kms_converter(value, 2))

print(kms_values)

# Save values in kilometers into a file
utils.write_to_txt(kms_file, kms_values)
