import turtle
turtle.tracer(0)


def recursion(size):
    if size > 10:
        for _ in range(4):
            turtle.forward(size)
            turtle.rt(90)
        turtle.forward(size * 0.1)
        turtle.rt(10)
        recursion(size / 1.1)
        

def binary_tree(order, size):   
    turtle.colormode(255)    
    if order == 0:
        return
    else:
        cg = 255 - int(order * (250/6)) % 255
        turtle.forward(size)
        turtle.rt(30)
        binary_tree(order - 1, size / 2)
        turtle.lt(60) 
        binary_tree(order - 1, size / 2)
        turtle.color(0, cg, 0)
        turtle.rt(30)
        turtle.backward(size)
        

def branch_fractal(order, size):
    turtle.colormode(255) 
    if order == 0:
        turtle.left(180)
        return

    cg = 255 - int(order * (250/6)) % 255
    x = size / (order+1)
    for i in range(order):
        turtle.forward(x)
        turtle.left(45)
        branch_fractal(order-i-1, 0.5*x*(order-i-1))
        turtle.left(90)
        branch_fractal(order-i-1, 0.5*x*(order-i-1))
        turtle.color(0, cg, 0)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


def koch_curve(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch_curve(order - 1, size / 3)
        turtle.left(60)
        koch_curve(order - 1, size / 3)
        turtle.right(120)
        koch_curve(order - 1, size / 3)
        turtle.left(60)
        koch_curve(order - 1, size / 3)


def minkowski_curve(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        minkowski_curve(order - 1, size / 2)
        turtle.left(90)
        minkowski_curve(order-1, size / 2)
        turtle.right(90)
        minkowski_curve(order - 1, size / 2)
        turtle.right(90)
        minkowski_curve(order - 1, size / 2)
        minkowski_curve(order - 1, size / 2)
        turtle.left(90)
        minkowski_curve(order - 1, size / 2)
        turtle.left(90)
        minkowski_curve(order - 1, size / 2)
        turtle.right(90)
        minkowski_curve(order - 1, size / 2)


def ice_fractals_1(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        ice_fractals_1(order-1, size / 2)
        turtle.left(90)
        ice_fractals_1(order - 1, size / 4)
        turtle.left(180)
        ice_fractals_1(order - 1, size / 4)
        turtle.left(90)
        ice_fractals_1(order - 1, size / 2)


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


def cat_fractal(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        turtle.left(90)
        cat_fractal(order - 1, size/2)
        turtle.right(45)
        cat_fractal(order - 1, size/4)
        turtle.right(45)
        cat_fractal(order - 1, size / 4)
        turtle.left(90)


def spikes(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        turtle.fd(size)
        turtle.lt(45)
        spikes(order - 1, size)
        turtle.lt(45)
        turtle.fd(size)
        turtle.backward(size)
        turtle.rt(135)
        spikes(order - 1, size)
        turtle.lt(45)
        turtle.fd(size)
    
        

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
        '[12] Кошачий фрактал \n',
        '[13] Фрактал 3'
    )

    choise = int(input('Выберите фрактал: '))
    if choise == 1:
        turtle.up()
        turtle.goto(-100, 200)
        turtle.down()
        recursion(300)

    elif choise == 2:
        turtle.up()
        turtle.goto(0, -100)
        turtle.down()
        turtle.lt(90)
        binary_tree(6, 200)

    elif choise == 3:
        turtle.up()
        turtle.goto(0, -300)
        turtle.down()
        turtle.lt(90)
        branch_fractal(5, 800)

    elif choise == 4:
        turtle.up()
        turtle.goto(-300, 0)
        turtle.down()
        koch_curve(5, 600)

    elif choise == 5:
        turtle.up()
        turtle.goto(-300, 0)
        turtle.down()
        for _ in range(3):
            koch_curve(5, 600)
            turtle.right(120)

    elif choise == 6:
        turtle.up()
        turtle.goto(-300, 0)
        turtle.down()
        minkowski_curve(4, 50)

    elif choise == 7:
        turtle.up()
        turtle.goto(-300, 0)
        turtle.down()
        ice_fractals_1(4, 500)
    
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
        turtle.up()
        turtle.goto(-150, 0)
        turtle.down()
        cat_fractal(3, 500)

    elif choise == 13:
        turtle.up()
        turtle.goto(-150, 0)
        turtle.down()
        spikes(7, 5)


if __name__ == '__main__':
    main()
    turtle.update()
    turtle.done()
