from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class test(BoxLayout):
	def __init__(self,tarefas):
		super().__init__()
		for tarefa in tarefas:
			self.add_widget(Label(text=tarefa))

class i(App):
	def build(self):
		return test(["andre","jon"])

if __name__ == '__main__':
    i().run()