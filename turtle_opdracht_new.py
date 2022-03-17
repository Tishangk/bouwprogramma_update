import turtle

def default_data(): 
    canvas_width = 1.0
    canvas_height = 1.0
    title_string = "Bouwprogramma"
    canvas_background = "#F5F5F5"
    canvas_tracker = 0 
    
    turtle.setup(width=canvas_width, height=canvas_height)
    turtle.title(title_string)
    turtle.bgcolor(canvas_background)
    turtle.tracer(canvas_tracker)
    
    
def login():
    global user 
    global userpass
    
    title_login_1 = "username"
    tekst_login_1 = "Geef uw username op:"
    title_login_2 = "wachtwoord"
    tekst_login_2 = "Geef uw wachtwoord op:"
    user = ""
    userpass = ""
    
    user = turtle.textinput(title_login_1, tekst_login_1)
    userpass = turtle.textinput(title_login_2, tekst_login_2)
    
    
def check_credentials():
    global user1 
    global userpass1 
    global canvas_write_denied
    global font_type
    global font_grootte
    
    user1 = "tisha"
    userpass1 = "tisha123"
    canvas_write_denied = "Acces denied"
    font_type = "Courier"
    font_grootte = 8
    

def check_input():
    global lengte
    global breedte
    global hoogte
    global canvas_write_denied
    
    lengte = ""
    breedte = ""
    hoogte = ""
    canvas_write_denied = "Je hebt de verkeerde maten opgegeven"
    font_type = "Courier"
    font_grootte = 8
    title = "Maten"
    
    tekst_lengte = "Geef de lengte in meters op (Max 75 meter)"
    tekst_breedte = "Geef de breedte in meters op (Max 25 meter)"
    tekst_hoogte = "Geef de hoogte in meters op (Max 25 meter)"
    lengte = turtle.numinput(title, tekst_lengte)
    breedte = turtle.numinput(title, tekst_breedte)   
    hoogte = turtle.numinput(title, tekst_hoogte)
    
    
    
def canvas_app():
    x = -500 
    for y in range(-280, 70 + 1, 10):
        turtle.penup()
        turtle.goto(x, y)  
        turtle.pendown()    
        turtle.forward(1000)

    y = 70
    turtle.right(90)
    for x in range(-500, 500 + 1, 10): 
        turtle.penup()
        turtle.goto(x, y) 
        turtle.pendown()
        turtle.forward(350)

    #we tekenen de x as 
    
    turtle.color("blue")
    turtle.right(-90)
    turtle.penup()
    turtle.goto(-625, 0) 
    turtle.pendown()
    turtle.forward(1250)

    pixel_blok = 0
    turtle.penup()
    turtle.goto(-625, 0)                
    for i in range(1, 26 + 1):           
        turtle.write(-625 + pixel_blok)  
        turtle.forward(50)              
        pixel_blok += 50

    turtle.penup()
    turtle.goto(-625, -20)                       
    turtle.write("x", font = ("Courier", 15))

   #we tekenen de y as 
   
    turtle.right(90)
    turtle.penup()
    turtle.goto(0, 350)                 
    turtle.pendown()
    turtle.forward(700)
    turtle.penup()

   
    pixel_blok = 0
    turtle.penup()
    turtle.goto(0, 350)                 
    for i in range(1, 15 + 1):          
        turtle.write(350 - pixel_blok)   
        turtle.forward(50)              
        pixel_blok += 50

   
    turtle.penup()
    turtle.goto(-20, 350)                        
    turtle.write("y", font = ("Courier", 15)) 
    
    #het tekstveld
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.goto(25, 300)
    
    turtle.pendown()
    turtle.forward(200)

    turtle.right(-90)
    turtle.forward(475)

    turtle.right(-90)
    turtle.forward(200)

    turtle.right(-90)
    turtle.forward(475)

    turtle.penup()
    
    turtle.end_fill()   

def tekst_in_tekstveld():
    vorm = ""
    volume = ""
    tekst = ""
    font_type = "Courier"
    font_grootte = 8
    volume_macht = 3
    turtle_x = 50
    turtle_y = 200
    
    if lengte == breedte and lengte == hoogte:
        vorm = "kubus"
        volume = str(int(lengte ** volume_macht))
   
    else:
        vorm = "balk"
        volume = str(int(lengte * hoogte * breedte))
    
    tekst = "Het object is een " + vorm + " en de volume is " + volume + " kubieke meter."

    turtle.goto(turtle_x, turtle_y)                        
    turtle.write(tekst, font = (font_type , font_grootte)) 
    
def object_display():
    global new_lengte
    global new_breedte
    global new_hoogte
    new_lengte = lengte * 10
    new_breedte = breedte * 10
    new_hoogte = hoogte * 10
    
    #voorvlak
    turtle.color("white", "black")
    turtle.begin_fill()
    
    turtle.right(-180)
    start = 0 - new_lengte / 2

    turtle.goto(start, -250)                

    turtle.pendown()
    turtle.forward(new_lengte)

    turtle.right(-90)
    turtle.forward(new_hoogte)

    turtle.right(-90)
    turtle.forward(new_lengte)

    turtle.right(-90)
    turtle.forward(new_hoogte)

    turtle.penup()
    turtle.end_fill()

    #zijvak
    start = 0 - new_lengte / 2
    start_2 = start + new_lengte
    
    turtle.color("white", "black")
    turtle.begin_fill()
    turtle.goto(start_2, -250)
    
    turtle.pendown()
    turtle.right(-120)
    turtle.forward(new_breedte)

    turtle.right(-60)
    turtle.forward(new_hoogte)

    turtle.right(-120)
    turtle.forward(new_breedte)

    turtle.right(-60)
    turtle.forward(new_hoogte)

    turtle.penup()
    turtle.end_fill()
    
    #bovenzijde
    start = 0 - new_lengte / 2
    turtle.color("white", "black")

    turtle.begin_fill()
    turtle.goto(start, -250 + new_hoogte)
    
    turtle.right(-120)

    turtle.pendown()
    turtle.forward(new_breedte)

    turtle.right(30)
    turtle.forward(new_lengte)

    turtle.right(150)
    turtle.forward(new_breedte)

    turtle.right(30)
    turtle.forward(new_lengte)

    turtle.penup()
    turtle.end_fill()
    
def main():
    default_data()
    login()
    check_credentials()
    if (user != user1 or userpass != userpass1):
        turtle.write(canvas_write_denied, font = (font_type, font_grootte))
    else:
        check_input()
        if lengte <= 75 and breedte <= 25 and hoogte <= 25:
            canvas_app()
            tekst_in_tekstveld()
            object_display()
        else: 
            turtle.write(canvas_write_denied, font = (font_type, font_grootte))

main()
turtle.done()