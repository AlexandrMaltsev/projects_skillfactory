import numpy as np

# count = 0                           # счетчик попыток
# number = np.random.randint(1,101)   # загадали число
# print ("Загадано число от 1 до 100")

# for count in range(1,101):         # более компактный вариант счетчика
#     if number == count: break      # выход из цикла, если угадали      
# print (f"Вы угадали число {number} за {count} попыток.")
    
# while True:                        # бесконечный цикл
#     predict = int(input())         # предполагаемое число
#     count += 1                     # плюсуем попытку
#     if number == predict: break    # выход из цикла, если угадали
#     elif number > predict: print (f"Угадываемое число больше {predict} ")
#     elif number < predict: print (f"Угадываемое число меньше {predict} ")
            
# print (f"Вы угадали число {number} за {count} попыток.")    


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_perfect(number):
    # Устанавливаем диапазон в середину диапазона, в зависимости больше или меньше первое предсказание от загаданного числа, следующее предсказание будет в середине левой или правой полудиапазона, повтаряем пока не найдем. С учетом попыток начинать с центра эффективнее всегда, потому что в среднем на одну попытку меньше, чем если сначала выбирать рандомное число
    
    count = 1
    # predict = np.random.randint(1,101)
    predict = 50
    border_min = 1
    border_max = 101
    
    while number != predict:
        count+=1
        if number > predict: 
            border_min = predict
            predict =int((border_min+border_max)/2)
        elif number < predict:
            border_max = predict 
            predict =int((border_min+border_max)/2)
    return(count) # выход из цикла, если угадали

score_game(game_core_perfect)