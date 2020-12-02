def check_password_validity(password):
    password_valid = False
    if password['password'][int(password['range'][0]) - 1] == password['letter']:
        password_valid = not password_valid
    if password['password'][int(password['range'][1]) - 1] == password['letter']:
        password_valid = not password_valid
    return password_valid


# Reading and parsing input
with open('./puzzle_input.txt') as input_file:
    policies_and_passwords = [line.strip() for line in input_file]
    parsed_input = []
    for input in policies_and_passwords:
        input = input.split(' ')
        parsed_input.append({
            'range': input[0].split('-'),
            'letter': input[1].replace(':', ''),
            'password': input[2]
        })

valid_passwords = 0
for password in parsed_input:
    if check_password_validity(password) is True:
        valid_passwords += 1

print(valid_passwords)