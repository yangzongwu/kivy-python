import kivy
kivy.require('1.11.1')  # 注意要把这个版本号改变成你现有的Kivy版本号!

from kivy.app import App  # 这里就是从kivy.app包里面导入App类
from kivy.uix.label import Label  # 这里是从kivy.uix.label包中导入Label控件，这里都注意开头字母要大写
# 。"kivy.uix"这个包的作用是容纳用户界面元素，比如各种输出布局和控件。

class MyApp(App):
    def build(self):  # 这里是实现build()方法
        return Label(text='Hello world')  # 在这个方法里面使用了Label控件


if __name__ == '__main__':
    MyApp().run()  # 这里就是运行了。
