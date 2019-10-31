from random import randrange as rnd, choice


import tkinter as tk


import math


import time


# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.down = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
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
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.x -= 1.05 * self.vx
            self.vx = (-0.8) * self.vx
            self.vy = 0.8 * self.vy
        if self.y + self.r >= 575:
            self.y += 1.005 * self.vy
            self.vy = (-0.6) * self.vy
            self.vy -= 1
            self.vx = 0.8 * self.vx
            if self.vy < 3 and abs(self.vx) < 1 and self.down == 0:
                self.down = 1
                self.vy = 0
                self.vx = 0
                self.y = 575 - self.r

    def accelerate(self):
        if self.down == 0:
            self.vy -= 3.5
        elif self.down < 10:
            self.down += 1
        self.vy -= 0.05 * self.vy
        if abs(self.vx) > 0.1:
            self.vx -= 0.1 * self.vx
        else:
            self.vx = 0
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
        
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2) or (
           (self.x < obj.x) and (self.y > obj.y) and (self.x + self.vx >= obj.x) and (self.y - self.vy <= obj.y)) or (
           (self.x < obj.x) and (self.y < obj.y) and (self.x + self.vx >= obj.x) and (self.y - self.vy >= obj.y)):
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.balls = []
        self.bullet = 0
        self.vx = 0
        self.vy = 0
        self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...
        self.x = 20
        self.y = 450

    def move_up(self, event):
        self.vy -= 5

    def move_down(self, event):
        self.vy += 5

    def move_right(self, event):
        self.vx += 5

    def move_left(self, event):
        self.vx -= 5

    def move(self):
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
        self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        # balls, bullet
        self.bullet += 1

        
        # global balls, bullet
        g1.bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.balls += [new_ball]
        g1.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = 0
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.delete(self.id)
        # canv.coords(self.id, x - r, y - r, x + r, y + r)
        self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
        # canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []

canv.bind('<w>', g1.move_up)
canv.bind('<d>', g1.move_right)
canv.bind('<s>', g1.move_down)
canv.bind('<a>', g1.move_left)
canv.bind('<KeyRelease-w>', g1.move_down)
canv.bind('<KeyRelease-d>', g1.move_left)
canv.bind('<KeyRelease-s>', g1.move_up)
canv.bind('<KeyRelease-a>', g1.move_right)

def new_game(event=''):
    # gun, t1, screen1, balls, bullet

def new_game(event=''):
    # global gun, t1, screen1, balls, bullet

    t1.new_target()
    g1.bullet = 0
    g1.balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    canv.bind('<w>', g1.move_up)
    canv.bind('<d>', g1.move_right)
    canv.bind('<s>', g1.move_down)
    canv.bind('<a>', g1.move_left)
    canv.bind('<KeyRelease-w>', g1.move_down)
    canv.bind('<KeyRelease-d>', g1.move_left)
    canv.bind('<KeyRelease-s>', g1.move_up)
    canv.bind('<KeyRelease-a>', g1.move_right)

    z = 0.03
    t1.live = 1
    while t1.live:
        g1.move()
    z = 0.03
    t1.live = 1
    while t1.live:
        for b in g1.balls:
            b.move()
            if b.down == 10:
                canv.delete(b.id)
                g1.balls.pop(g1.balls.index(b))
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bullet) + ' выстрелов')
                canv.update()
                time.sleep(1)
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
    t1.live = 1


new_game()
print(t1.x, t1.y, t1.r)

tk.mainloop()
