import panduan

import zimua

#tashilei
# niyaoshilihua
# aa = zimua.Game()
# aa.a()
game =input("请选择游戏\n数字游戏()\n字母游戏()\n输入1或2:")
if game == "1":
    # 实例化对象
    gun_num = panduan.GameGum()
    gun_num.num_member(0,0)
elif game == "2":
    gun_nu = zimua.Game()
    gun_nu.a()
    gun_nu.l()
else:
    print("输入错误")
