from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView


class MainApp(MDApp):
    
    def build(self):

        scroll = ScrollView()

        label = MDLabel(text="Hello, World", halign="center")

        scroll.add_widget(label)

        return scroll


MainApp().run()

# test