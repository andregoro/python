from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class tarefas(ScrollView):
	def __init__(self,tarefass,**kwargs):
		super().__init__(**kwargs)
		for tarefa in tarefass:
			self.ids.box.add_widget(Label(text=tarefa,font_size=30,size_hint_y=None,height=200))
			
class Test(App):
	def build(self):
		return tarefas(['andre','jojo','titica','andrei'])
		

Test().run()