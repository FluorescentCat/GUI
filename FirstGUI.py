from guizero import App, Text, TextBox, PushButton, Slider, Picture

def SayMyName():
    WelcomeText.value = MyName.value
    
def ChangeTextSize(SliderValue):
    WelcomeText.size = SliderValue   


app = App(title="Hello world")


WelcomeText = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
MyName = TextBox(app, width=30)
UpdateText = PushButton(app, command=SayMyName, text="Display my name")
TextSize = Slider(app, command=ChangeTextSize, start=10, end=80)
CatStepen = Picture(app, image="stepen.gif", width=400, height=225)


app.display()

