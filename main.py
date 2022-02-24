from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from decouple import config

WEATHER_API_KEY = config('WEATHER_API_KEY')

Window.size = (640/1.5, 1260/1.5)

screen_helper = """
ScreenManager:
    MenuScreen:
    TestScreen:
<MenuScreen>:
    name: 'menu'
    canvas.before:
        Color:
            rgba: 	58/255, 59/255, 60/255,  1
        Rectangle:
            pos: self.pos
            size: self.size
    ScrollView:
        GridLayout:
            cols: 1
            padding: 20
            spacing: 20
            size_hint: None, None
            width: root.width
            height: self.minimum_height
            Button:
                on_press:  root.manager.current = 'profile'
                size_hint_y: None
                height: dp(20)
                background_normal: ''
                background_color: [0,0,0,0]
            Button:
                # on_press: root.manager.current = 'profile'
                size_hint_y: None
                height: dp(150)
                background_normal: ''
                background_color: [255/255,204/255,0,1]
                border: 30, 30, 30, 30
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (255/255,204/255,0,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30,]
                Image:
                    source: 'assets/home_page/sunny_weather_TEMP.gif'
                    size: self.parent.size
                    x: self.parent.x + 100
                    y: self.parent.y
                    anim_delay: 0.1
                    mipmap: True
            Button:
                on_press: root.manager.current = 'profile'
                size_hint_y: None
                height: dp(150)
                background_normal: ''
                background_color: [1,1,1,1]
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30,]
                Image:
                    source: 'assets/home_page/calendar.gif'
                    size: self.parent.size
                    x: self.parent.x + 100
                    y: self.parent.y
                    anim_delay: 0.1
                    mipmap: True
            Button:
                on_press: root.manager.current = 'profile'
                size_hint_y: None
                height: dp(150)
                background_normal: ''
                background_color: [1,1,1,1]
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30,]
                Image:
                    source: 'assets/home_page/checklist.gif'
                    size: self.parent.width - 60, self.parent.height - 60
                    x: self.parent.x + 130
                    y: self.parent.y + 30
                    anim_delay: 0.2
                    mipmap: True
            Button:
                on_press: root.manager.current = 'profile'
                size_hint_y: None
                height: dp(150)
                background_normal: ''
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30,]
                
                Image:
                    source: 'assets/home_page/app_usage.gif'
                    size: self.parent.size
                    x: self.parent.x + 100
                    y: self.parent.y
                    anim_delay: 0.1
                    mipmap: True
            Button:
                on_press: root.manager.current = 'profile'
                size_hint_y: None
                height: dp(150)
                background_normal: ''
                background_color: [240/255,240/255,245/255,1]
                background_color: 0,0,0,0  # the last zero is the critical on, make invisible
                canvas.before:
                    Color:
                        rgba: (240/255,240/255,245/255,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [30,]
                Image:
                    source: 'assets/home_page/activity_usage.gif'
                    size: self.parent.size
                    x: self.parent.x + 100
                    y: self.parent.y
                    anim_delay: 0.1
                    mipmap: True

<TestScreen>:
    name: 'profile'
    canvas.before:
        Color:
            rgba: 	58/255, 59/255, 60/255,  1
        Rectangle:
            pos: self.pos
            size: self.size
    ScrollView:
        GridLayout:
            cols: 1
            padding: 20
            # spacing: 30
            height: self.minimum_height + 50
            CheckBox:
                # height: 50
                # active: True
                on_active: print(self.parent.minimum_height)
                
            
"""


class MenuScreen(Screen):
    pass


class TestScreen(Screen):
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")


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

