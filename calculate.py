import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    '''
		Вычисляет и выводит результат функции (площадь или периметр) для указанной фигуры.

	    Принимает параметры:
	    - fig: строка, название фигуры ('circle' или 'square').
	    - func: строка, название функции для вычисления ('perimeter' или 'area').
	    - size: список чисел, размеры фигуры (например, радиус для круга или длина стороны для квадрата).

	    Программа использует функцию eval для вызова соответствующей функции из модуля (circle или square).
	    Выводит результат вычисления с указанием фигуры и выполняемой функции.
	'''
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)
