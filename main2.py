LOW_LIMIT = 0
UP_LIMIT = 1000
ONE = 1
TEN = 10
HUNGRED = 100
SQUARE = 2

num = LOW_LIMIT
while num <= LOW_LIMIT or num >= UP_LIMIT:
    num = int(input(f"Введите число от {LOW_LIMIT + ONE} до {UP_LIMIT - ONE}: "))

if num < TEN:
    result = f"Число {num} - цифра. Ее квадрат равен {num ** SQUARE}"
elif num < HUNGRED:
    prod = (num // TEN) * (num % TEN)
    result = f"Число {num} - двухзначное. Произведение цифр равно {prod}"
else:
    mirror = (num % TEN * HUNGRED) + (num // TEN % TEN * TEN) + (num // HUNGRED)
    result = f"Число {num} - трехзначное. Его зеркальное число - {mirror}"
print(result)

