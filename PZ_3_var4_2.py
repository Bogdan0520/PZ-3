#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B < 3».

a = input('Введите длину волны света в нм')

while type(a) != float:
    try:
        a = float(a)
    except:
        print('Неправильно ввели число a')
        a = input('Введите длину волны света в нм')
    

if a <= 450: print('Фиолетовый')
elif 450<a<480: print('Синий')
elif 480<=a<510: print('Сине-зеленый')
elif 510<=a<550: print('Зеленый')
elif 550<=a<570: print('Желто-зеленый')
elif 570<=a<590: print('Желтый')
elif 590<=a<630: print('Оранжевый')
elif a>=630: print('Красный')
