from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class EzPb(App):
    def build(self):
        layout = BoxLayout(
            orientation='vertical')

        welcome = Label(text='Welcome to the Ez PhotoBooth!')

        start = Button(text='Start', size_hint=(.2, .2))
        
        layout.add_widget(welcome)
        layout.add_widget(start)

        return layout

if __name__ == '__main__':
    EzPb().run()