

from random import randint
# 引入tk包          所有函数变量
from tkinter import *

class Randball():
    def __init__(self, canvas, scrnwidth, scrnheight):
        #初始化画布
        self.canvas = canvas
        #初始化球的圆心坐标
        self.x_pos = randint(20, int(scrnwidth))
        self.y_pos = randint(20, int(scrnheight))
        # 球的速度

        #球移动的距离
        self.x_move = randint(8, 12)
        self.y_move = randint(8, 12)
        #整个屏幕的宽和高
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        #初始化球的半径
        self.radius = randint(40, 70)
        #随机产生球的颜色
        rc = lambda :randint(0,255)
        self.color = '#%02x%02x%02x' % (rc(), rc(), rc())

    def create_ball(self):
        #计算得到用于创建球的四个坐标
        x1 = self.x_pos - self.radius
        y1 = self.y_pos - self.radius
        x2 = self.x_pos + self.radius
        y2 = self.y_pos + self.radius
        #画圆   create_oval   # fill 填充    #outline 轮廓线
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        '''按指定的距离移动球，如果球碰到障碍向相反的方向移动'''
        self.x_pos += self.x_move
        self.y_pos += self.y_move

        if self.x_pos >= self.scrnwidth - self.radius:
            self.x_move = -self.x_move
        if self.y_pos >= self.scrnheight - self.radius:
            self.y_move = -self.y_move
        if self.x_pos < self.radius:
            self.x_move = abs(self.x_move)
        if self.y_pos < self.radius:
            self.y_move = abs(self.y_move)
        self.canvas.move(self.item, self.x_move, self.y_move)

class Screensaver():
    balls = []
    def __init__(self, ball_nums):

        self.win = Tk()
        self.width = self.win.winfo_screenwidth()
        self.height = self.win.winfo_screenheight()

        # 如果为1 则视觉上窗体整个边框消失
        self.win.overrideredirect(True)

        self.win.attributes('-alpha', 0.3)
        #绑定事件，有任何动作退出屏保
        self.win.bind('<Any-Button>', self.exit_screensaver)
        self.win.bind('<Motion>', self.exit_screensaver)
        # 画布颜色为青绿色
        self.canvas = Canvas(self.win, width=self.width, height=self.height, bg='#00FFFF')
        #布局画布
        self.canvas.pack()

        for i in range(0,ball_nums):
            ball = Randball(self.canvas, scrnwidth=self.width, scrnheight=self.height)
            ball.create_ball()
            self.balls.append(ball)
            # 运行
        self.run_screensaver()
        # 等待循环
        self.win.mainloop()

    def run_screensaver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(20, self.run_screensaver)

    def exit_screensaver(self, event):
        self.win.destroy()


def main():
    Screensaver(50)


if __name__=='__main__':
    main()