from kivy.app import App
from kivy.uix.gridlayout import GridLayout  # 布局
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    """
    我们在LoginScreen类中重新定义了初始化方法init()，这样来增加一些控件，并且定义了这些控件的行为
    一定要注意这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法。另外
    也要注意，这里调用super的时候没有省略掉**kwargs，这是一种好习惯。
    """
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        # 把子控件设置为两栏，然后加上用户名和密码的Label字符显示控件和TextInput字符输入控件。
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
