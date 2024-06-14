from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager


class LoginScreen(Screen): #1
    pass


class MainScreen(Screen): #2
    pass


class UI(ScreenManager):
    pass

class dltApp(App):
    def build(self):
        return UI()
    
if __name__=='__main__':
    dltApp().run()