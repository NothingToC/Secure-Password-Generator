import random

digits = '1234567890'
lower_words = 'abcdefghijklmnopqrstuvwxyz'
upper_words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'
arr_variables = [digits, lower_words, upper_words, symbols]

def user_request():
    count_password = int(input("Сколько паролей вы хотите сгенерировать?: "))
    len_password = int(input("Какой длины вы хотите пароль?: "))

    return count_password, len_password

arr_request = user_request()

def generate_password(count_pas, len_pas):
    arr = [digits, upper_words, lower_words, symbols]
    all_chars = ''.join(arr)
    gener_passwords = []
    
    arr_chars = []
    for i in range(len(all_chars)):
        arr_chars.append(all_chars[i])

    for i in range(count_pas):
        password = ''
        for j in range(len_pas):
            password += random.choice(arr_chars)
        
        gener_passwords.append(password)

    return gener_passwords

print()
print(f"Сгенерируемые пароли {arr_request[0]}:")
print(*generate_password(arr_request[0], arr_request[1]), sep="\n")