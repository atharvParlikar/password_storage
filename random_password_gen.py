import random
import string

def randomPassword(length):
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+=-0987654321`;.,></?|'
    return ''.join((random.choice(letters) for i in range(length)))
