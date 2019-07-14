from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import time
class app(App):
    def build(self):
        parent=Widget()
        b=Button()
        self.l=Label(text=str(time.time()))
        parent.add_widget(b)
        b.bind(on_release=self.renew)
        parent.add_widget(self.l)
        return parent
    def renew(self,s):
        self.l.text=str(time.time())
if __name__ == "__main__":
    app().run()