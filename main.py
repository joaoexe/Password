import random
from file import argumenFile
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*(){}[]<>:,."

while True:
    try:
        len = int(input("[+] - PASSWORD LENGTH: "))
        quantity = int(input("[+] = AMOUNT OF PASSWORD: "))
    except ValueError:
        print("Invalid Entry!!!!")
    else:
        for x in range(0, quantity):
            passwd = ""
            for x in range(0, len):
                passchar = random.choice(char)
                passwd = passwd + passchar
            print("[+] - Generated Password: ", passwd)
            argumenFile(passwd)
        break
