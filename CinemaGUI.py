from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info


def Booking():
    price = 5
    if SeatChoice.value == "B" or SeatChoice.value == "M":
        price += 3
    if VipSeat.value == True:
        price += 2
    
    info("Booking", f"Thank you for booking!\nYour ticket price is: {price}€")

    

app = App(title="Cinema Booking", width=300, height=200, layout="grid")

FilmChoice = Combo(app, options=["Star Wars", "Indiana Jones", "Lord of the Rings"], grid=[1,0], align="left")
FilmDescription = Text(app, text="Which film?", grid=[0,0], align="left")

SeatType = Text(app, text="Seat type", grid=[0,1], align="left")
VipSeat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")

SeatLocation = Text(app, text="Seat location", grid=[0,2], align="left")
SeatChoice = ButtonGroup(app, options=[["Front", "F"], ["Middle", "M"], ["Back", "B"]], selected="M", horizontal=True, grid=[1,2], align="left")

BookSeats = PushButton(app, command=Booking, text="Book seat", grid=[1,3], align="left")


app.display()