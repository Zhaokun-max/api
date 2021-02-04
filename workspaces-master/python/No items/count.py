'''
- 模拟系统的计算器
- 实现一个简单的具有加减法等操作的计算机
- 使用tkinter
- 操作步骤
    - 画gui
    - 给每个控件配置相应的时间
    - 逻辑代码
'''
# 第一步画出面板
import tkinter
from tkinter import *

root = Tk()
#屏幕大小
root.geometry('300x400')

root.title('panda')
#定义面板
# bg 代表背景颜色，background
frame_show = Frame(width=300, height=400, bg='#dddddd')
frame_show.pack()
# 定义顶部区域
sv = StringVar()
sv.set('0')
# anchor 定义空间的锚点  font代表字体
show_loabel = Label(frame_show, textvariable=sv, \
                    bg='green', width=10, height=1, \
                    font=('黑体', 20, 'bold'), \
                    justify=LEFT, anchor='e')

show_loabel.pack(padx=10, pady=10)

def delete():
    print("删除")

def clear():
     print('清空')
def fan():
    print('fan')
def ce():
    print('ce')

#按键区域
frame_bord = Frame(width=400, height=350, bg='#cccccc')
b_del = Button(frame_bord, text="←", width=5, height=1, \
               command=delete).grid(row=0, column=0)
#b_del.grid(row=0, column=0)
b_clear = Button(frame_bord, text='C', width=5, height=1, \
                 command=clear).grid(row=0, column=1)
b_ce = Button(frame_bord, text='CE', width=5, height=1, \
               command=fan).grid(row=0, column=2)
b_fan = Button(frame_bord, text='fan', width=5, height=1, \
              command=ce).grid(row=0, column=3)
b_except = Button(frame_bord, text='/', width=5, height=2, \
             command=lambda :operation('/')).grid(row=1, column=3)
b_plus = Button(frame_bord, text='+', width=5, height=2, \
             command=lambda :operation('+')).grid(row=2,column=3)
b_ride = Button(frame_bord, text='*', width=5, height=2,\
                command=lambda :operation('*')).grid(row=3, column=3)
b_etc = Button(frame_bord, text='=', width=5, height=2, \
               command=lambda :operation('=')).grid(row=4, column=2)
b_reduce = Button(frame_bord, text='-', width=5, height=2, \
                  command=lambda :operation('-')).grid(row=4, column=3)
'''
1.按下数字
2.按下操作符号
3.只考虑两个操作数操作，
'''
num1 =''
num2 =''
operator = ''


def change(num):
    '''
    按下一个数字需要考虑两种
    1.数字属于第一次操作数
    2.数字属于第二个操作数
    3.判断是否属于第一个操作数，可以通过operator
    '''
    #加入操作数是None，表明肯定是一个操作数
    if not operator:
        global num1
        num1 = num1 + num
        #如果是第一个操作数，则只显示第一个操作数
        sv.set(num1)
    else:
        global num2
        #如果是第二个操作数，则应该显示完整的计算式子
        num2 += num
        sv.set(num+operator+num2)

def operation(op):
    global rst
    if op in ['+', '-', '*', '/']:
        operator = op
    else: #认为按下的是等于号
        if op == '+':
            rst = int(num1) + int(num2)
        if op == '-':
            rst = int(num1) + int(num2)
        if op == '*':
            rst = int(num1) + int(num2)
        if op == '/':
            rst = int(num1) + int(num2)
        if op =='=':
            rst = int(num1) + int(num2)
        sv.set(str(rst))


b_1 = Button(frame_bord, text='1', width=5, height=2, \
             command=lambda:change('1')).grid(row=1, column=0)
b_2 = Button(frame_bord, text='2', width=5, height=2, \
             command=lambda:change('2')).grid(row=1, column=1)
b_3 = Button(frame_bord, text='3', width=5, height=2, \
             command=lambda:change('3')).grid(row=1, column=2)
b_4 = Button(frame_bord, text='4', width=5, height=2, \
             command=lambda:change('4')).grid(row=2, column=0)
b_5 = Button(frame_bord, text='5', width=5, height=2, \
             command=lambda:change('5')).grid(row=2, column=1)
b_6 = Button(frame_bord, text='6', width=5, height=2, \
             command=lambda:change('6')).grid(row=2,column=2)
b_7 = Button(frame_bord, text='7', width=5, height=2, \
             command=lambda:change('7')).grid(row=3, column=0)
b_8 = Button(frame_bord, text='8', width=5, height=2, \
            command=lambda:change('8')).grid(row=3,column=1)
b_9 = Button(frame_bord, text='9', width=5, height=2, \
             command=lambda:change('9')).grid(row=3,column=2)
b_0 = Button(frame_bord, text='0', width=5, height=2, \
             command=lambda:change('0')).grid(row=4, column=0)
b_spot=Button(frame_bord, text='.', width=5, height=2, \
              command=lambda:change('.')).grid(row=4, column=1)







frame_bord.pack(padx=10, pady=10)
root.mainloop()

