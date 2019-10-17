import tkinter as tk

#Тут должен быть комментарий
#Пытался Сделать ООП, добавил класс игры
#Вторая итерация. Доделал класс игры, пытался начать генерить шарики, но все пошло в никуда, устранил ошибки, наделанные в первой итерации. Добавил цвета шарам.

from random import randrange as rnd, choice

import time

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.canv = tk.Canvas(self.root, bg = 'white')
        self.canv.pack(fill = tk.BOTH, expand=1)
    
    def run(self):
        self.new_ball()
        self.root.after(10, self.new_ball)
        self.root.mainloop()  
    
    def new_ball(self):
        ball = Ball()
        '''self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        colors = ['yellow','blue', 'red', 'green', 'black']
        color = choice(colors)
        self.obj = self.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill = color, width = 0)
        self.root.after(10, self.new_ball)'''


class Creation:
    def __init__(self):
        pass
    
    def new_ball(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        colors = ['yellow','blue', 'red', 'green', 'black']
        color = choice(colors)
        self.obj = self.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill = color, width = 0)
    

class Ball:
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        colors = ['yellow','blue', 'red', 'green', 'black']
        self.color = choice(colors)
        self.obj = game.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill = self.color, width = 0)
    def rpd(self):
        game.canv.delete(self.obj)
        self.x += self.vx
        self.y += self.vy
        self.obj = game.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, 
                                         self.y + self.r, fill = self.color, width = 0)
        game.root.after(10, self.rpd)
        
        
def click(event):
    print(event.x, event.y)


if __name__ == '__main__':
    game = Game()
    game.canv.bind('<Button-1>', click)
    game.run()







