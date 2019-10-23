from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_string('''
<MainMenu>:
    orientation: 'vertical'
    size_hint_y: .5
    Label:
        text: 'Welcome to the Ez PhotoBooth!'
    # Label:
    #     text: root.logs
    BoxLayout:
        orientation: 'horizontal'
        size_hint: (1,.3)
        Button:
            text: 'Choose Printer'
            on_press: root.choose_printer()
        Button:
            text: 'Choose Overlay Image'
            on_press: root.choose_overlay()
        Button:
            text: 'Choose Destination Folder'
            on_press: root.choose_destination()
        Button:
            text: 'Start'
            on_press: root.start()
''')

class MainMenu(BoxLayout):
    def choose_printer(self):
        print("TODO: Find Printer")

    def choose_overlay(self):
        print("TODO: Select overlay image")

    def choose_destination(self):
        print("TODO: Set destination directory")

    def start(self):
        print("TODO: Start watching")

class Photobooth(App):
    def build(self):
        return MainMenu()

class Notifications(BoxLayout):
    def __init__(self):
        self.message = 'Welcome to the Ez Photobooth'

    def notify(self, message):
        self.message = message

if __name__ == '__main__':
    Photobooth().run()