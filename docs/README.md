# Общее описание решения
В проекте geometric_lib реализованно два файла circle и square в каждой есть две функции для расчета пложади и периметра.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Описание каждой функции с примерами вызова

## circle.py

- Функция Area, принимает число r и возвращает его в квадрате и умноженный на константу пи.

Пример вызова:
    print(area(5))

Терминал:
    78.5

- Функция Perimeter, принимает число r и возвращает его умноженный на константу пи и на два.

Пример вызова:
    print(perimetr(5))

Терминал:
    31.4

## square.py

- Функция Area, принимает число r и возвращает его квадрат.

Пример вызова:
    print(area(5))

Терминал:
    25

- Функция Perimeter, принимает число r и возвращает его умноженный на четыре.

Пример вызова:
    print(perimetr(5))

Терминал:
    20

## Triangle.py

- Функция Area, принимает числа a,b,c и возвращает их сумму делённую на два.
    

Пример вызова:
    print(area(5,5,4))

Терминал:
    7

- Функция Perimeter, принимает числа a,b,c и возвращает их сумму.

Пример вызова:
    print(perimetr(5,5,4))

Терминал:
    14

## calculate.py

1. Программа импортирует два модуля: circle и square, которые, скорее всего, содержат функции для вычисления периметра и площади (area) этих фигур.
2. Список figs содержит названия фигур — 'circle' и 'square', а список funcs — доступные функции: 'perimeter' и 'area'.
3. Функция calc(fig, func, size) принимает название фигуры, функцию для вычисления (периметр или площадь), а также размер фигуры.
   Через eval() программа вызывает соответствующую функцию из импортированных модулей и выводит результат.
4. Основной блок программы запрашивает у пользователя название фигуры, функцию и размеры,
   после чего вызывает функцию calc для выполнения расчета.

Пример:
    Enter figure name, available are ['circle', 'square']:
    square
    Enter function name, available are ['perimeter', 'area']:
    perimeter
    Input figure sizes separated by space, 1 for circle and square:
    4
Терминал:
    perimeter of square is 16

# История изменения проекта с хешами комитов (кроме последней записи)
```
commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
```