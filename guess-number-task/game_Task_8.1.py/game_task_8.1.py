import numpy as np
count = 0
number = np.random.randint(1, 101) # загадали список чисел
print("Компьютер сам загадывает и сам угадывает число от 1 до 100")
min = 0
max = 100
while True:
    predict = round((min+max)/2)
    count += 1
    if number == predict:
        break
    elif number > predict:
        min = predict
        print(f"Угадываемое число больше {predict}")
        print ({round((max + min) / 2)})
    elif number < predict:
        max = predict
        print(f"Угадываемое число меньше {predict}")
        print ({round((max+min)/2)})
print(f"Вы угадали число {number} за {count} попыток.")