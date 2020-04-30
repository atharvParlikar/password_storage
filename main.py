import encryption
import random_password_gen
import random
import pdb

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
web_file = open('websites.txt', 'a')
pass_file = open('passwords.txt', 'a')

choice = int(input('1]store password\n2]get stored password\n>>>'))
if choice == 1:
    choice = int(input('1]store password of an existing account\n2]get a random password for a new account\n>>>'))
    if choice == 1:
        website = input('website: ')
        existing_password = input('password: ')
        web_file.write(website + '\n')
        pass_file.write((encryption.encrypt(existing_password)).decode() + '\n')
        print('password saved successfully!')
    elif choice == 2:
        website = input('website: ')
        random_password = random_password_gen.randomPassword(random.randint(15,20))
elif choice == 2:
    web_file = open('websites.txt', 'r')
    pass_file = open('passwords.txt', 'r')
    website_search = input('website: ')
    iteration_counter = 0
    for i in web_file:
        if i == website_search:
            print(i)
