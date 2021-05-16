from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="Hello")
        b2 = Button(text="Bye")
        self.add_widget(b1)
        self.add_widget(b2)

class MyApp(App):
    def build(self):
        return BoxLayoutExample()
        
MyApp().run()
