import turtle
turtle.tracer(0)


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
        '[1] Рекурсивные функции \n',
        '[2] Построение двочиного дерева \n',
        '[3] Фрактал "Ветка" \n',
        '[4] Кривая Коха \n',
        '[5] Снежинка Коха \n',
        '[6] Кривая Минковского \n',
        '[7] Ледяные фракталы 1 \n',
        '[8] Ледяные фракталы 2 \n',
        '[9] Кривая Леви \n',
        '[10] Фрактал Дракон Хартера-Хейтуэя \n',
        '[11] Линия Фишера \n',
        '[12] Фрактал 2 \n',
        '[13] Фрактал 3'
    )

    choise = int(input('Выберите фрактал: '))
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
        minkowski_curve()
    elif choise == 7:
        ice_fractals_1()
    
    elif choise == 8:
        turtle.pu()
        turtle.goto(-400, 0)
        turtle.pd()
        ice_fractals_2(3, 100)
    
    elif choise == 9:
        turtle.pu()
        turtle.goto(-100, 0)
        turtle.pd()
        levy_curve(8, 10)

    elif choise == 10:
        turtle.pu()
        turtle.goto(-200, 0)
        turtle.pd()
        dragon(12, 6, 0)

    elif choise == 11:
        turtle.pu()
        turtle.goto(-300, 0)
        turtle.pd()
        fshr_line(4, 5)
        turtle.rt(180)
        fshr_line(4, 5)

    elif choise == 12:
        fractal2()
    elif choise == 13:
        fractal3()


if __name__ == '__main__':
    main()
    turtle.update()
    turtle.done()
