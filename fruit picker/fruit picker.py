from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import random
KV = '''
MDScreen:
    md_bg_color:  0, 0, 0, 1 
    Image:
        id: fruit_image
        source: "images/apple.png"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint:  0.5, 0.5
    MDRectangleFlatButton:
        text: "choose fruit"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        line_color: app.theme_cls.disabled_hint_text_color
        md_bg_color: 0, 0, 1, .5
        text_color: 1, 0, 0, 1 
        on_release: app.choose_fruit()
            '''
class fruit_picker(MDApp, BoxLayout, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ui = Builder.load_string(KV)
        self.eui = BoxLayout()
        self.icon = "images/icon.png"


    def build(self):
        screen = Screen()
        screen.add_widget(self.ui)
        return screen

    def choose_fruit(self):
        fruit = random.choice(["apple.png","lemon.png","orange.png","watermelon.png"])
        self.filepath = "images/" + fruit
        print("[DEBUG]" + "    " + "fruit image source= " + self.ui.ids.fruit_image.source)
        self.ui.ids.fruit_image.source = self.filepath
fruit_picker().run()
