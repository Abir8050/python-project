import turtle
wn = turtle.Screen()
wn.title("Snake game by Abir, Tahmid, Mim")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
wn.mainloop()