from random import randrange as rnd, choice

import tkinter as tk

import math

import time

from random import randrange as rnd


# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, n):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.n = n
        self.x = g1.x + 20
        self.y = g1.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.down = 0
        self.color = choice(['blue', 'green', 'brown', 'yellow'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30
        self.accelerate()

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y -= self.vy
        canv.delete(self.id)
        for t in g1.balls:
            if t != self:
                if self.n != 4 and t.n != 4 and (
                   (self.x - t.x) ** 2 + (self.y - t.y) ** 2 <= (self.r + t.r) ** 2 or (
                    self.x < t.x and (self.y > t.y) and (self.x + self.vx >= t.x) and (
                     self.y - self.vy <= t.y)) or ((self.x < t.x) and (self.y < t.y) and (
                      self.x + self.vx >= t.x and (self.y - self.vy >= t.y)))):
                    self.x -= 1.01 * self.vx
                    self.y -= 1.01 * self.vy
                    t.x -= 1.01 * t.vx
                    t.y -= 1.01 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy

                if self.n != 4 and t.n == 4 and (
                   ((abs(self.x - t.x) <= self.r + t.r and abs(self.y - t.y) <= t.r) or (
                    abs(self.y - t.y) <= self.r + t.r and abs(self.x - t.x) <= t.r) or (
                    (self.x - (t.x - t.r)) ** 2 + (self.y - (t.y - t.r)) ** 2 <= self.r ** 2) or (
                     (self.x - (t.x - t.r)) ** 2 + (self.y - (t.y + t.r)) ** 2 <= self.r ** 2) or (
                      (self.x - (t.x + t.r)) ** 2 + (self.y - (t.y - t.r)) ** 2 <= self.r ** 2) or (
                       (self.x - (t.x + t.r)) ** 2 + (self.y - (t.y + t.r)) ** 2 <= self.r ** 2))):
                    self.x -= 1.01 * self.vx
                    self.y -= 1.01 * self.vy
                    t.x -= 1.005 * t.vx
                    t.y -= 1.005 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy

                if self.n == 4 and t.n != 4 and (
                   ((abs(self.x - t.x) <= self.r + t.r and abs(self.y - t.y) <= self.r) or (
                     abs(self.y - t.y) <= self.r + t.r and abs(self.x - t.x) <= self.r) or (
                     (t.x - (self.x - self.r)) ** 2 + (t.y - (self.y - self.r)) ** 2 <= t.r ** 2) or (
                      (t.x - (self.x - self.r)) ** 2 + (t.y - (self.y + self.r)) ** 2 <= t.r ** 2) or (
                       (t.x - (self.x + self.r)) ** 2 + (t.y - (self.y - self.r)) ** 2 <= t.r ** 2) or (
                        (t.x - (self.x + self.r)) ** 2 + (t.y - (self.y + self.r)) ** 2 <= t.r ** 2))):
                    self.x -= 1.005 * self.vx
                    self.y -= 1.005 * self.vy
                    t.x -= 1.01 * t.vx
                    t.y -= 1.01 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy

                if self.n == 4 and t.n == 4 and (
                   (abs(self.x - t.x) <= self.r + t.r) and (
                     abs(self.y - t.y) <= self.r + t.r)):
                    self.x -= 1.005 * self.vx
                    self.y -= 1.005 * self.vy
                    t.x -= 1.01 * t.vx
                    t.y -= 1.01 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy
        x = self.x
        y = self.y
        r = self.r
        color = self.color
        if self.n == 0:
            self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
        elif self.n == 4:
            self.id = canv.create_rectangle(x - r, y - r, x + r, y + r, fill=color)
        else:
            points = []
            for n in range(self.n):
                points.append(self.x + (self.r * math.sin(2 * n * math.pi / self.n)))
                points.append(self.y + (self.r * math.cos(2 * n * math.pi / self.n)))
            self.id = canv.create_polygon(points, fill=color)
                
        '''self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )'''
        
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.x -= 1.05 * self.vx
            self.vx = (-0.9) * self.vx
            self.vy = 0.9 * self.vy
        if self.y + self.r > 575:
            self.y = 575 - self.r
            self.vy = (-0.75) * self.vy
            self.vy -= 1
            self.vx = 0.75 * self.vx
            if self.vy < 3 and abs(self.vx) < 1 and self.down == 0:
                self.down = 1
                self.vy = 0
                self.vx = 0

    def accelerate(self):
        if self.down == 0 and self.vx == 0 and self.vy == 0:
            self.vy -= 3.5
        elif self.down < 10 and self.vx == 0 and self.vy == 0:
            self.down += 1
        else:
            self.down = 0
            self.vy -= 3.5
        self.vy -= 0.05 * self.vy
        if abs(self.vx) > 0.1:
            self.vx -= 0.1 * self.vx
        else:
            self.vx = 0
        if abs(self.vy) < 1:
            self.vy = 0
        '''if self.down == 10:
            canv.delete(self.id)'''
        root.after(100, self.accelerate)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        # FIXME

        if obj.n != 4 and ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2) or (
           self.x < obj.x <= self.x + self.vx and self.y > obj.y) and (
            self.y - self.vy <= obj.y or self.x < obj.x and self.y < obj.y) and (
             self.x + self.vx >= obj.x and self.y - self.vy >= obj.y):
            return True
        
        if obj.n == 4 and ((abs(self.x - obj.x) <= self.r + obj.r and abs(self.y - obj.y) <= obj.r) or (
           abs(self.y - obj.y) <= self.r + obj.r and abs(self.x - obj.x) <= obj.r) or (
           (self.x - (obj.x - obj.r)) ** 2 + (self.y - (obj.y - obj.r)) ** 2 <= self.r ** 2) or (
            (self.x - (obj.x - obj.r)) ** 2 + (self.y - (obj.y + obj.r)) ** 2 <= self.r ** 2) or (
             (self.x - (obj.x + obj.r)) ** 2 + (self.y - (obj.y - obj.r)) ** 2 <= self.r ** 2) or (
              (self.x - (obj.x + obj.r)) ** 2 + (self.y - (obj.y + obj.r)) ** 2 <= self.r ** 2)):
            return True
            
        else:
            return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.r = 7
        self.balls = []
        self.bullet = 0
        self.vx = 0
        self.vy = 0
        self.x = 40
        self.y = 450
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

        # FIXME: don't know how to set it...

        # self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=color)

        self.kol_1 = canv.create_oval(self.x - self.r, self.y + 5, self.x + self.r,
                                      self.y + 2 * self.r + 5, fill='brown')
        self.kol_2 = canv.create_oval(self.x - self.r + 20, self.y + 5, self.x + self.r + 20,
                                      self.y + 2 * self.r + 5, fill='brown')
        self.opora = canv.create_line(self.x - 15, self.y + 7, self.x + 40, self.y + 7, width=5)
        self.speed()

        '''canv.bind('<w>', self.move_up)
        canv.bind('<D>', self.move_right)
        canv.bind('<s>', self.move_down)
        canv.bind('<a>', self.move_left)
        canv.bind('<KeyRelease-w>', self.move_down)
        canv.bind('<KeyRelease-d>', self.move_left)
        canv.bind('<KeyRelease-s>', self.move_up)
        canv.bind('<KeyRelease-a>', self.move_right)

    def move_up(self, event):
        self.vy -= 5
        print('w')

    def move_down(self, event):
        self.vy += 5
        print('s')

    def move_right(self, event):
        self.vx += 5
        print('d')

    def move_left(self, event):
        self.vx -= 5
        print('a')'''

    def speed(self):
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        root.after(2000, self.speed)
    
    def move(self):
        canv.delete(self.id)
        canv.delete(self.kol_1)
        canv.delete(self.kol_2)
        canv.delete(self.opora)
        self.x += self.vx
        self.y += self.vy
        if self.x < 20:
            self.x = 20
        if self.x > 750:
            self.x = 750
        if self.y < 50:
            self.y = 50
        if self.y > 550:
            self.y = 550
        self.id = canv.create_line(self.x, 450, 50, 420, width=7)  # FIXME: don't know how to set it...
        self.kol_1 = canv.create_oval(self.x - self.r - 5, self.y + 10, self.x + self.r - 5,
                                      self.y + 2 * self.r + 10, fill='brown')
        self.kol_2 = canv.create_oval(self.x - self.r + 30, self.y + 10, self.x + self.r + 30,
                                      self.y + 2 * self.r + 10, fill='brown')
        self.opora = canv.create_line(self.x - 15, self.y + 7, self.x + 40, self.y + 7, width=5)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        # balls, bullet
        self.bullet += 1
        n = rnd(3, 8)
        if n == 3:
            n = 0
        new_ball = Ball(n)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        self.an = min(self.an, 0)
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        
        if event:
            self.an = math.atan((event.y - self.y) / (event.x - self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        self.move()
        self.an = min(self.an, 0)
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))
        
        '''canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )'''

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    
    def __init__(self, n):
        targets.append(self)
        self.n = n
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text='', font='28')
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.vx = 0
        self.vy = 0
        self.color = 0
        self.down = 0
        self.speed()
        # self.new_target()
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 20:
            self.x = 20
            self.vx = abs(self.vx)
        if self.x > 800:
            self.x = 800
            self.vx = -abs(self.vx)
        if self.y < 50:
            self.y = 50
            self.vy = abs(self.vy)
        if self.y > 550:
            self.y = 550
            self.vy = -abs(self.vy)
        for t in targets:
            if t != self:
                if self.n != 4 and t.n != 4 and (
                   (self.x - t.x) ** 2 + (self.y - t.y) ** 2 <= (self.r + t.r) ** 2 or (
                    self.x < t.x and (self.y > t.y) and (self.x + self.vx >= t.x) and (
                     self.y - self.vy <= t.y)) or ((self.x < t.x) and (self.y < t.y) and (
                      self.x + self.vx >= t.x and (self.y - self.vy >= t.y)))):
                    self.x -= 1.005 * self.vx
                    self.y -= 1.005 * self.vy
                    t.x -= 1.005 * t.vx
                    t.y -= 1.005 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy

                if self.n != 4 and t.n == 4 and (
                   ((abs(self.x - t.x) <= self.r + t.r and abs(self.y - t.y) <= t.r) or (
                    abs(self.y - t.y) <= self.r + t.r and abs(self.x - t.x) <= t.r) or (
                    (self.x - (t.x - t.r)) ** 2 + (self.y - (t.y - t.r)) ** 2 <= self.r ** 2) or (
                     (self.x - (t.x - t.r)) ** 2 + (self.y - (t.y + t.r)) ** 2 <= self.r ** 2) or (
                      (self.x - (t.x + t.r)) ** 2 + (self.y - (t.y - t.r)) ** 2 <= self.r ** 2) or (
                       (self.x - (t.x + t.r)) ** 2 + (self.y - (t.y + t.r)) ** 2 <= self.r ** 2))):
                    self.x -= 1.005 * self.vx
                    self.y -= 1.005 * self.vy
                    t.x -= 1.005 * t.vx
                    t.y -= 1.005 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy

                if self.n == 4 and t.n != 4 and (
                   ((abs(self.x - t.x) <= self.r + t.r and abs(self.y - t.y) <= self.r) or (
                     abs(self.y - t.y) <= self.r + t.r and abs(self.x - t.x) <= self.r) or (
                     (t.x - (self.x - self.r)) ** 2 + (t.y - (self.y - self.r)) ** 2 <= t.r ** 2) or (
                      (t.x - (self.x - self.r)) ** 2 + (t.y - (self.y + self.r)) ** 2 <= t.r ** 2) or (
                       (t.x - (self.x + self.r)) ** 2 + (t.y - (self.y - self.r)) ** 2 <= t.r ** 2) or (
                        (t.x - (self.x + self.r)) ** 2 + (t.y - (self.y + self.r)) ** 2 <= t.r ** 2))):
                    self.x -= 1.005 * self.vx
                    self.y -= 1.005 * self.vy
                    t.x -= 1.005 * t.vx
                    t.y -= 1.005 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy

                if self.n == 4 and t.n == 4 and (
                   (abs(self.x - t.x) <= self.r + t.r) and (
                     abs(self.y - t.y) <= self.r + t.r)):
                    self.x -= 1.005 * self.vx
                    self.y -= 1.005 * self.vy
                    t.x -= 1.005 * t.vx
                    t.y -= 1.005 * t.vy
                    vx = self.vx
                    vy = self.vy
                    self.vx = t.vx
                    self.vy = t.vy
                    t.vx = vx
                    t.vy = vy
                    
        if self.down == 0:
            x = self.x
            y = self.y
            r = self.r
            color = self.color
            canv.delete(self.id)
            if self.n == 0:
                self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
            elif self.n == 4:
                self.id = canv.create_rectangle(x - r, y - r, x + r, y + r, fill=color)
            else:
                points = []
                for n in range(self.n):
                    points.append(self.x + (self.r * math.sin(2 * n * math.pi / self.n)))
                    points.append(self.y + (self.r * math.cos(2 * n * math.pi / self.n)))
                self.id = canv.create_polygon(points, fill=color)

    def speed(self):
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        root.after(2000, self.speed)
        
    def new_target(self):
        """ Инициализация новой цели. """
        self.down = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        while self.down > 0:
            self.down = 0
            x = self.x = rnd(600, 780)
            y = self.y = rnd(300, 550)
            '''for i in range(len(targets)):
                if targets[i] != self and (
                 (self.x - targets[i].x) ** 2 + (self.y - targets[i].y) ** 2 <= (self.r + targets[i].r) ** 2):
                    self.down += 1'''
            for t in targets:
                if self != t and (((self.r + t.r) * 2) ** 2 >= (self.x - t.x) ** 2 + (self.y - t.y) ** 2):
                    self.down += 1
        self.down = 0
        color = self.color = 'red'

        canv.delete(self.id)

        # canv.coords(self.id, x - r, y - r, x + r, y + r)

        if self.n == 0:
            self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
        elif self.n == 4:
            self.id = canv.create_rectangle(x - r, y - r, x + r, y + r, fill=color)
        else:
            points = []
            for n in range(self.n):
                points.append(self.x + (self.r * math.sin(2 * n * math.pi / self.n)))
                points.append(self.y + (self.r * math.cos(2 * n * math.pi / self.n)))
            self.id = canv.create_polygon(points, outline='black', fill=color)

        # canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        for t in targets:
            t.points += points
        canv.itemconfig(targets[0].id_points, text=self.points)
        self.down = 1


targets = []
t1 = Target(0)
t2 = Target(4)
t3 = Target(5)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()

# gun, t1, screen1, balls, bullet


def new_game():

    for t in targets:
        t.new_target()
    g1.bullet = 0
    g1.balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    s = 0
    for t in targets:
        t.live = 1
        s += t.live
    
    while s:
        # g1.move()
        for t in targets:
            t.move()
        for b in g1.balls:
            b.move()
            if b.down == 10:
                canv.delete(b.id)
                g1.balls.pop(g1.balls.index(b))
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bullet) + ' выстрелов')
                    canv.update()
                    time.sleep(1)
                    canv.itemconfig(screen1, text='')
                    canv.bind('<Button-1>', g1.fire2_start)
                    canv.bind('<ButtonRelease-1>', g1.fire2_end)
        s = 0
        for t in targets:
            s += t.live
            
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    # canv.delete(gun)
    root.after(750, new_game)
    for b in g1.balls:
        canv.delete(b.id)
    g1.balls = []
    for t in targets:
        t.live = 1


new_game()

# print(t1.x, t1.y, t1.r)

tk.mainloop()
