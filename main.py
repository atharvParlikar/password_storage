import encryption
import random_password_gen
import random
import pdb
import json


print('''

██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

███████╗████████╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝
███████╗   ██║   ██║   ██║██████╔╝███████║██║  ███╗█████╗
╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║██║   ██║██╔══╝
███████║   ██║   ╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████╗
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

''')
with open('user_data.json', 'r+') as file:
    choice = int(input('1]store passwords\n2]get stored passwords\n>>>'))
    if choice == 1:
        choice = int(input('1]store password for existing account\n2]get a random password for new account\n>>>'))
        if choice == 1:
            website = input('enter the website: ')
            password = input('password: ')
            password = (encryption.encrypt(password)).decode()
            user_dict = {website: password}
            with open('user_data.json', 'r+') as file:
                data = json.load(file)
                data.update(user_dict)
                file.seek(0)
                json.dump(data, file)
        elif choice == 2:
            website = input('enter the website lable: ')
            password = (encryption.encrypt(random_password_gen.randomPassword(random.randint(15,20)))).decode()
            user_dict = {website: password}
            with open('user_data.json', 'r+') as file:
                data = json.load(file)
                data.update(user_dict)
                file.seek(0)
                json.dump(data, file)
            print('Your password for ' + website + ' is ' + (encryption.decrypt(password.encode())).decode())
    elif choice == 2:
        website_to_find = input('enter the website lable: ')
        with open('user_data.json', 'r'):
            user_data_dict = json.load(file)
            password = user_data_dict[website_to_find]
            password = password.encode()
            print('The password for ' + website_to_find + ' is ' + (encryption.decrypt(password)).decode())
