import tkinter as tk


import math


# Тут должен быть комментарий
# Пытался Сделать ООП, добавил класс игры
# Вторая итерация. Доделал класс игры, пытался начать генерить шарики, но все пошло в никуда,
# устранил ошибки, наделанные в первой итерации. Добавил цвета шарам.

from random import randrange as rnd, choice


# import time

class Game:
    def __init__(self):
        self.score = 0
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.canv = tk.Canvas(self.root, bg='white')
        self.canv.pack(fill=tk.BOTH, expand=1)
        self.balls = [0]
        self.g = 0
        self.g_arg = 0
        self.gx = 0
        self.gy = 0
        self.pole_g()

    def pole_g(self):
        self.g = rnd(-10, 10)
        self.g = self.g / 100
        self.g_arg = rnd(0, 360)
        self.gx = self.g * math.cos(self.g_arg)
        self.gy = self.g * math.sin(self.g_arg)
        self.root.after(5000, self.pole_g)
        
    def run(self):
        self.new_ball()
        # self.root.after(10, self.new_ball)
        self.root.mainloop()  

    def new_ball(self):
        ball = Ball()
        self.balls.append(ball)
        self.root.after(2000, self.new_ball)
        '''self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        colors = ['yellow','blue', 'red', 'green', 'black']
        color = choice(colors)
        self.obj = self.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill = color, width = 0)
        self.root.after(10, self.new_ball)'''


'''class Creation:
    def __init__(self):
        pass

    def new_ball(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        colors = ['yellow','blue', 'red', 'green', 'black']
        color = choice(colors)
        self.obj = self.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill=color, width=0)'''
    

class Ball:
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(20, 60)
        self.d = 0
        # delete
        i = 1
        while i < len(game.balls):
            if game.balls[i] != 0 and game.balls[i] != self and (((self.x - game.balls[i].x) ** 2
               + (self.y - game.balls[i].y) ** 2 <= (self.r + game.balls[i].r) ** 2)):
                self.x = rnd(100, 700)
                self.y = rnd(100, 500)
                i = 1
            else:
                i += 1

        self.arg = rnd(0, 360) * math.pi / 180
        # self.vx = rnd(-3, 3)
        # self.vy = rnd(-3, 3)
        # self.vx = 2.5
        # self.vy = 0.5
        self.v = rnd(-5, 5)
        while self.v == 0:
            self.v = rnd(-5, 5)
        self.vx = self.v * math.cos(self.arg)
        self.vy = self.v * math.sin(self.arg)
        colors = ['yellow', 'blue', 'red', 'green', 'black']
        self.color = choice(colors)
        self.obj = game.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill=self.color, width=0)
        self.rpd()
        self.accelerate()

    def __del__(self):
        # game.balls.pop(game.balls.index(self))
        self.d = 1
        game.canv.delete(self.obj)
        game.balls[game.balls.index(self)] = 0

    def rpd(self):
        game.canv.delete(self.obj)
        self.x += self.vx
        self.y += self.vy
        self.obj = game.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill=self.color, width=0)
        if self.d == 0: 
            game.root.after(15, self.rpd)
        if self.x <= self.r:
            self.vx = abs(self.vx)
            # self.arg = math.pi - self.arg
        if self.x + self.r >= 800:
            self.vx = -abs(self.vx)
        if self.y <= self.r:
            self.vy = abs(self.vy)
            # self.arg = -self.arg
        if self.y + self.r >= 600:
            self.vy = -abs(self.vy)

        self.arg = math.atan(self.vy / self.vx)
        if self.vx < 0:
            self.arg = math.pi - self.arg
        
        for i in range(len(game.balls)):
            if (game.balls[i] != 0) and (self != game.balls[i]) and (((self.x - game.balls[i].x) ** 2
               + (self.y - game.balls[i].y) ** 2 <= (self.r + game.balls[i].r) ** 2)):
                f = math.atan((game.balls[i].y - self.y) / (game.balls[i].x - self.x))
                v1 = self.v * math.cos(self.arg - f)
                v2 = game.balls[i].v * math.cos(game.balls[i].arg - f)
                v10 = self.v * math.sin(self.arg - f)
                v20 = game.balls[i].v * math.sin(game.balls[i].arg - f)

                self.v = (v10 ** 2 + v2 ** 2) ** 0.5
                game.balls[i].v = (v20 ** 2 + v1 ** 2) ** 0.5
                self.arg = math.atan(v10 / v2)
                game.balls[i].arg = math.atan(v20 / v1)
                if v2 < 0:
                    self.arg = math.pi - self.arg
                
                if v1 < 0:
                    game.balls[i].arg = math.pi - game.balls[i].arg
                self.arg += f
                game.balls[i].arg += f
                
                self.vx = self.v * math.cos(self.arg)
                self.vy = self.v * math.sin(self.arg)
                game.balls[i].vx = game.balls[i].v * math.cos(game.balls[i].arg)
                game.balls[i].vy = game.balls[i].v * math.sin(game.balls[i].arg)

                game.canv.delete(self.obj)
                d = (abs((((self.x - game.balls[i].x) ** 2
                + (self.y - game.balls[i].y) ** 2 - (self.r + game.balls[i].r) ** 2)) ** 0.5))
                d = d / 10
                self.x += (((self.x - game.balls[i].x) / abs(self.x - game.balls[i].x)) *
                d * abs(math.cos(f)))
                self.y += (((self.y - game.balls[i].y) / abs(self.y - game.balls[i].y)) *
                d * abs(math.sin(f)))
                self.obj = game.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                                 self.y + self.r, fill=self.color, width=0)
        
        self.arg = math.atan(self.vy / self.vx)
        if self.vx < 0:
            self.arg = math.pi - self.arg

    def accelerate(self):
        self.vx += game.gx
        self.vy += game.gy
        self.arg = math.atan(self.vy / self.vx)
        if self.vx < 0:
            self.arg = math.pi - self.arg
        if self.d == 0:
            game.root.after(10, self.accelerate)
                
        
def click(event):
    print(event.x, event.y)
    for i in range(1, len(game.balls)):
        if game.balls[i] != 0 and (((event.x - game.balls[i].x) ** 2
        + (event.y - game.balls[i].y) ** 2) <= game.balls[i].r ** 2):
            game.score += 1
            game.balls[i].__del__()
    print(game.score)   
    while 1 in game.balls:
        game.balls.pop(game.balls.index(1))


if __name__ == '__main__':
    game = Game()
    game.canv.bind('<Button-1>', click)
    game.run()
