import random
from time import sleep
num1 = int(input("введите число от которого будет начинатся отчёт: "))
num2 = int(input("введите число которым будет заканчиватсья отчёт: "))
random_number = random.randint(num1, num2)
print(random_number)
print("рандомное число сгенирировалось")
sleep(0.1)
number_of_users = int(input("введите ваше число"))
if number_of_users == random_number:
    print("вы угадали!")
