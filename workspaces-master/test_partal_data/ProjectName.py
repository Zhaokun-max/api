import random

class Project_Name():

    def a(self):
        i=random.randrange(1,8)
        if i ==1:
            return '农村土地转让200亩地'
        if i ==2:
            return '这是一个生成的流转类型'
        if i ==3:
            return '关于蔡家镇的流转补贴'
        if i ==4:
            return '关于蔡家镇政府的项目'
        if i ==5:
            return '个人流转项目以及介绍'
        if i ==6:
            return '这是无尽空虚'
        if i ==7:
            return '情人大地'
        if i ==8:
            return '在那些苍翠的路上'
    @property
    def str_Name(self):
        ran = random.randrange(1, 1000)
        Name=self.a()+str(ran)
        return Name
