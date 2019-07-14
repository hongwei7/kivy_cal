#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from decimal import Decimal
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class Calcualtor(App):
    def create_button(self,text,pos,method):
        self.num_buttons.append(Button(text=text, pos=pos))
        self.parent.add_widget(self.num_buttons[-1])
        self.num_buttons[-1].bind(on_release=method)
    def build(self):
        Window.size = (400, 450)
        self.parent = Widget()
        self.printer = Label(text='Hi', pos=(350, 700), font_size=150)
        self.parent.add_widget(self.printer)
        self.num_buttons = []
        pos=dict()
        for k in range(10):
            if k==0:
                pos['0']=(200,0)
            else:
                pos[str(k)]=(350+(k-1)%3*150,(k-1)//3*150)
            self.create_button(str(k),pos[str(k)],self.num_in)
        k = 0
        for s in ['+', '-', '*', '/', '%', '^']:
            pos[s]=(50+k%2*150,k//2*150+150)
            self.create_button(str(s),pos[str(s)],self.sign_in)
            k += 1
        self.create_button('=',(50,0),self.equal_method)
        self.create_button('AC',(500,450),self.init_)
        self.create_button('Back',(350,450),self.num_back)
        self.create_button('.',(650,450),self.num_in)
        return self.parent

    def on_start(self):
        self.init_(None)

    def init_(self, s):
        self.stroke = ''
        self.method = None
        self.memory = 0
        self.waiting = False
        self.print = self.memory
        self.print_sign = ''
        self.doted=False
        self.renew()

    def go(self):
        self.doted=False
        if self.waiting:
            b = self.stroke
            try:
                p = self.method_cal(self.memory,b, self.method)
                self.stroke=''
            except:
                self.method = b
                self.print_sign = b
                return
            self.waiting = False
            self.print = p
        else:
            p = self.stroke
        if p in ['+', '-', '*', '/', '%', '^']:
            self.print_sign = p
            if self.memory == None:
                return
            self.method = p
            self.waiting = True
            return
        elif p == '':
            self.print = self.memory
            return
        self.memory = p


    def method_cal(self, pre, back, method):
        pre = Decimal(pre)
        back = Decimal(back)
        if method == '+':
            return pre+back
        elif method == '-':
            return pre-back
        elif method == '*':
            return pre*back
        elif method == '/':
            if int(float(back))==0:
                return 'ERROR'
            return pre/back
        elif method == '%':
            return pre % back
        elif method == '^':
            try:
                return float(pre**back)
            except:
                return 'ERROR'

    def equal_method(self, k):
        if self.waiting:
            self.go()
        if self.stroke !='':
            self.memory=self.stroke
        self.print = self.memory
        self.renew()

    def sign_in(self, s):
        print(self.memory)
        if s.text=='-' and self.stroke=='' and self.memory == 0:
            self.num_in(s)
            return
        self.go()
        self.stroke = s.text
        self.go()
        self.stroke = ''
        self.renew(True)
        
    def num_in(self, s):
        if len(str(self.stroke)) > 7:
            return
        if s.text=='.' and self.doted:
            return
        elif s.text=='.':
            self.doted=True
        self.stroke += s.text
        self.print = self.stroke
        self.renew()

    def renew(self, sign=False):
        if self.memory=='.':
            self.memory='0'
        if self.memory=='ERROR': #divided by zero
            s=self.memory
            self.init_(None)
            self.printer.text=s
            return 
        if len(str(int(float(self.memory)))) > 8: #max error
            self.init_(None)
            self.printer.text='ERROR'
            return
        if str(self.print) !='0' and self.stroke =='' and not sign:
            self.print=int(float(self.print)*100)/100
        if sign:
            s = str(self.print)+' '+str(self.print_sign)
        else:
            s = str(self.print)
        self.printer.text = str(s)
    def num_back(self,s):
        try:
            if self.stroke[-1]=='.':
                self.doted=False
        except:
            pass
        if self.waiting and len(str(self.stroke))==0:
            self.waiting=False
            self.print_sign=self.stroke
            self.renew(True)
        elif self.stroke=='':
            pass
        else:
            self.stroke=self.stroke[:-1]
            if self.stroke=='':
                self.print='0'
            else:
                self.print=self.stroke
            self.renew()


if __name__ == "__main__":
    Calcualtor().run()
