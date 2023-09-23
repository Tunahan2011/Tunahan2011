import random

symbols="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk=int(input("Ne kadar uzun bir şifre istiyorsun?\n"))
password=""
for i in range(uzunluk):
    password=password + random.choice(symbols)
print(password)
