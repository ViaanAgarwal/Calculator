from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Calculator(App):
    def build(self):
        return Label(text='Hello Calculator')
Calculator().run()
