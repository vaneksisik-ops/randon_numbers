import random
from time import sleep
num1 = int(input("введите число от которого будет начинатся отчёт: "))
num2 = int(input("введите число которым будет заканчиватсья отчёт: "))
while True:
    random_number = random.randint(num1, num2)
    print(random_number)
    sleep(0.1)