from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    TestScreen:
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        Button:
            on_press:  root.manager.current = 'profile'
            Image:
                source: 'kivy.png'
                size: 250, 250
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            on_press:  root.manager.current = 'profile'
            Image:
                source: 'kivy.png'
                size: 250, 250
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Button:
            on_press:  root.manager.current = 'profile'
            Image:
                source: 'kivy.png'
                size: 250, 250
                center_x: self.parent.center_x
                center_y: self.parent.center_y

<TestScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
"""

class MenuScreen(Screen):
    pass


class TestScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(TestScreen(name='profile'))

class MainApp(MDApp):

    def build(self):
        # return scroll
        screen = Builder.load_string(screen_helper)
        return screen



MainApp().run()

