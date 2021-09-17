from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Test(App):
    def build(self):
        self.box=BoxLayout(orientation="vertical")
        self.button=Button(text='Botao 1',font_size=30,on_release=self.incre)
        self.label=Label(text='texto 1',)
        self.box.add_widget(self.button)
        self.box.add_widget(self.label)
        return self.box

    def incre(self,bot):
        if self.label.text=="turururu":
            self.label.text ='texto 1'
        else:
            self.label.text = "turururu";

if __name__ == '__main__':
    Test().run()