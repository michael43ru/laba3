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



ell(60, 130, 300, 310)

brushColor(255, 100, 175)
penColor(255, 100, 175)
polygon([(600, 430), (700, 150), (800, 430), (600, 430)])

brushColor(240, 230, 230)
penColor(230, 230, 230)
circle(305, 140, 50)
circle(700, 140, 50)

penColor('black')

line(260, 220, 110, 370)
line(340, 220, 520, 380)
line(520, 380, 675, 210)
line(720, 210, 790, 295)
line(790, 295, 890, 220)
line(880, 250, 920, 120)

line(280, 430, 210, 570)
line(210, 570, 180, 570)
line(330, 420, 350, 570)
line(350, 570, 380, 570)

line(675, 430, 675, 570)
line(725, 430, 725, 570)
line(675, 570, 645, 570)
line(725, 570, 755, 570)

brushColor(240, 220, 50)
penColor(240, 220, 50)

polygon([(120, 370), (40, 325), (115, 270)])

brushColor('red')
penColor('red')

polygon([(912, 142), (912, 50), (980, 80)])
circle(930, 55, 20)
circle(965, 70, 20)

circle(90, 275, 22)

brushColor(70, 20, 0)
penColor(70, 20, 0)
circle(55, 305, 22)

brushColor('white')
penColor('white')
circle(60, 270, 22)





run()

