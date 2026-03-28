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

//

 # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

        # Check for a collision with the food
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.001
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

 # Pause text pen
    pause_pen = turtle.Turtle()
    pause_pen.speed(0)
    pause_pen.penup()
    pause_pen.hideturtle()
    pause_pen.color("dark green")

    # Pause button (tkinter button on top of turtle window)
    canvas = wn.getcanvas()
    tk_root = canvas.winfo_toplevel()

    def toggle_pause():
        paused["value"] = not paused["value"]
        if paused["value"]:
            pause_btn.config(text="RESUME", bg="green")
            pause_pen.goto(0, 0)
            pause_pen.write("  PAUSED  ", align="center", font=("Courier", 26, "bold"))
        else:
            pause_btn.config(text="PAUSE", bg="orange")
            pause_pen.clear()

    pause_btn = tk.Button(tk_root, text="PAUSE",
                          font=("Courier", 11, "bold"),
                          bg="orange", fg="white",
                          relief="flat", padx=8, pady=2,
                          cursor="hand2",
                          command=toggle_pause)
    pause_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-8, y=8)

//

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

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

