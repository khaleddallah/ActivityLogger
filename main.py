import kivy
from excel import xl
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
kivy.require('1.9.0')
Window.size = (800, 350)


class RootWidget(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''

    container = ObjectProperty(None)


    fld=ObjectProperty()
    que=ObjectProperty()
    num=ObjectProperty()

    xl1=xl.xll("excelfiles/plan.xlsx","ques")

    list_fld=xl1.feldlst
    list_ques=xl1.queslst
    list_typ=xl1.typlst
    c = 0

 #count
    initfld=str("\n-----\n"+list_fld[0]+"\n--------------------\n")

    def nextf (self):
        if int(self.c) >= int(self.xl1.ws.max_column-2):
            return
        self.c+=1
        self.num.text=str(int(self.c + 1))
        self.fld.text=str("\n-----\n"+self.list_fld[self.c]+"\n--------------------\n")
        self.que.text=self.list_ques[self.c]

    def backf (self):
        if int(self.c) <= 0 :
            return
        self.c-=1
        self.num.text=str(int(self.c+1))
        self.fld.text=str("\n-----\n"+self.list_fld[self.c]+"\n--------------------\n")
        self.que.text=self.list_ques[self.c]





class logApp(App):

    def build(self):
        self.root = Builder.load_file('kv/start.kv')


    def start(self):
        Builder.unload_file('kv/ques.kv')
        self.root.container.clear_widgets()
        screen = Builder.load_file('kv/ques.kv')

        self.root.container.add_widget(screen)

glApp = logApp()
glApp.run()

