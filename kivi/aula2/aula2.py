from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box=BoxLayout(orientation="vertical")
        box2=BoxLayout(orientation="horizontal")

        bot=Button(text='Botao 1')
        bot2=Button(text='Botao 2')
        label=Label(text='Texto')
        label2=Label(text='Texto')
        box.add_widget(bot)
        box2.add_widget(bot2)
        box2.add_widget(label2)
        box.add_widget(label)
        box.add_widget(box2)

        return box

if __name__ == '__main__':
    Test().run()
