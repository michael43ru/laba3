from graph import *


windowSize(1000, 600)
canvasSize(1000, 600)

brushColor(180, 230, 255)
penColor(180, 230, 255)
rectangle(0, 0, 1000, 300)

brushColor(100, 200, 100)
rectangle(0, 300, 1000, 600)

brushColor(160, 140, 200)
penColor(160, 140, 200)

def ell(a, b, x0, y0):
    x = 0
    y = b
    l = [(x0, y0 + b)]
    for i in range(a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        l.append((x + x0, y + y0))
    for i in range(a):
        x += 1
        y = -((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        l.append((x + x0, y + y0))
    for i in range(a):
        x += 1
        y = -((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        l.append((x + x0, y + y0))
    for i in range(a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        l.append((x + x0, y + y0))
    l.append((x0, y0 + b))
    polygon(l)

def paren(x, y):

    ell(60, 130, x, y)

    brushColor(240, 230, 230)
    penColor(230, 230, 230)
    circle(x + 10, y - 170, 50)

    penColor('black')
    line(x - 40, y - 90, x - 190, y + 60)
    line(x + 40, y - 90, x + 220, y + 70)

    line(x - 20, y + 120, x - 90, y + 260)
    line(x - 90, y + 260, x - 120, y + 260)
    line(x + 30, y + 110, x + 50, y + 260)
    line(x + 50, y + 260, x + 80, y + 260)

def devka():

    brushColor(255, 100, 175)
    penColor(255, 100, 175)
    polygon([(600, 430), (700, 150), (800, 430), (600, 430)])

    brushColor(240, 230, 230)
    penColor(230, 230, 230)
    circle(700, 140, 50)

    penColor('black')
    line(520, 380, 675, 210)
    line(720, 210, 790, 295)
    line(790, 295, 890, 220)
    
    line(675, 430, 675, 570)
    line(725, 430, 725, 570)
    line(675, 570, 645, 570)
    line(725, 570, 755, 570)

def morozh(x, y):
     
    brushColor(240, 220, 50)
    penColor(240, 220, 50)
    polygon([(x, y), (x - 80, y - 45), (x - 5, y - 100)])

    brushColor('red')
    penColor('red')
    circle(x - 30, y - 95, 22)

    brushColor(70, 20, 0)
    penColor(70, 20, 0)
    circle(x - 65, y - 65, 22)

    brushColor('white')
    penColor('white')
    circle(x - 60, y - 100, 22)

def serdech(x, y, a):

    # вращение вокруг (x - 22, y + 78)
    penColor('black')
    line(x - 32, y + 108, x + 8, y - 22)
    
    brushColor('red')
    penColor('red')

    polygon([(x, y), (x, y - 92), (x + 68, y - 62)])
    circle(x + 18, y - 87, 20)
    circle(x + 53, y - 72, 20)

def povorot():
    

paren(300, 310)
devka()


serdech(912, 142)
morozh(120, 370)

run()

