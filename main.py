import turtle


def recursion():
    pass


def binary_tree():
    pass


def branch_fractal():
    pass


def koch_curve():
    pass


def koch_snowflake():
    pass


def minkowski_curve():
    pass


def ice_fractals_1():
    pass


def ice_fractals_2(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        ice_fractals_2(order - 1, size)
        turtle.lt(120)
        ice_fractals_2(order - 1, size / 2)
        turtle.lt(180)
        ice_fractals_2(order - 1, size / 2)
        turtle.lt(120)
        ice_fractals_2(order - 1, size / 2)
        turtle.lt(180)
        ice_fractals_2(order - 1, size / 2)
        turtle.lt(120)
        ice_fractals_2(order - 1, size)


def levy_curve(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        turtle.lt(45)
        levy_curve(order - 1, size)
        turtle.rt(90)
        levy_curve(order - 1, size)
        turtle.lt(45)


def dragon(order, size, n):
    if order == 0:
        turtle.fd(size)
    else:
        if n == 0:
            turtle.lt(45)
        else:
            turtle.rt(45)
        dragon(order - 1, size, 0)
        if n == 0:
            turtle.rt(90)
        else:
            turtle.lt(90)
        dragon(order - 1, size, 1)
        if n == 0:
            turtle.lt(45)
        else:
            turtle.rt(45)


def fshr_line(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        fshr_line(order - 1, size)
        turtle.rt(90)
        fshr_line(order - 1, size)
        turtle.lt(90)
        fshr_line(order - 1, size)
        turtle.lt(90)
        fshr_line(order - 1, size)
        turtle.rt(90)
        fshr_line(order - 1, size)


def fractal2():
    pass


def fractal3():
    pass


def main():
    print(
        '[0] Рекурсивные функции \n',
        '[1] Построение двочиного дерева \n',
        '[2] Фрактал "Ветка" \n',
        '[3] Кривая Коха \n',
        '[4] Снежинка Коха \n',
        '[5] Кривая Минковского \n',
        '[6] Ледяные фракталы 1 \n',
        '[7] Ледяные фракталы 2 \n',
        '[8] Кривая Леви \n',
        '[9] Фрактал 1 \n',
        '[10] Фрактал 2 \n',
        '[11] Фрактал 3'
    )

    choise = int(input('Выберите фрактал:'))
    if choise == 1:
        recursion()
    elif choise == 2:
        binary_tree()
    elif choise == 3:
        branch_fractal()
    elif choise == 4:
        koch_curve()
    elif choise == 5:
        koch_snowflake()
    elif choise == 6:
        ice_fractals_1()
    elif choise == 7:
        ice_fractals_2()
    elif choise == 8:
        levy_curve()
    elif choise == 9:
        fractal1()
    elif choise == 10:
        fractal2()
    elif choise == 11:
        fractal3()


if __name__ == '__main__':
    main()
