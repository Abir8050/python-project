import turtle

wn = turtle.Screen()
wn.title("Snake game by Abir, Tahmid, Mim")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        



#main game loop
while True:
    wn.update()

wn.mainloop()