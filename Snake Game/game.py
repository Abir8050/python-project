import turtle
import time
import random
import tkinter as tk

# ─────────────────────────────────────────────
#  MENU WINDOW
# ─────────────────────────────────────────────
def show_menu():
    result = {"start": False}

    root = tk.Tk()
    root.title("Snake Game")
    root.geometry("600x600")
    root.resizable(False, False)
    root.configure(bg="light blue")

    tk.Label(root, text="", bg="light blue").pack(pady=60)

    tk.Label(root, text="🐍 SNAKE GAME 🐍",
             font=("Courier", 30, "bold"),
             bg="light blue", fg="dark green").pack()

    tk.Label(root, text="by Abir, Tahmid & Mim",
             font=("Courier", 13, "italic"),
             bg="light blue", fg="black").pack(pady=10)

    tk.Label(root, text="", bg="light blue").pack(pady=30)

    def on_start():
        result["start"] = True
        root.destroy()

    def on_exit():
        root.destroy()

    tk.Button(root, text="START GAME",
              font=("Courier", 16, "bold"),
              bg="green", fg="white",
              width=15, height=2,
              cursor="hand2",
              command=on_start).pack(pady=10)

    tk.Button(root, text="EXIT GAME",
              font=("Courier", 16, "bold"),
              bg="red", fg="white",
              width=15, height=2,
              cursor="hand2",
              command=on_exit).pack(pady=10)

    root.mainloop()
    return result["start"]

# ─────────────────────────────────────────────
#  GAME  (original code + pause button)
# ─────────────────────────────────────────────
def run_game():
    delay = 0.1
    score = 0
    high_score = 0
    paused = {"value": False}

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake game by Abir, Tahmid, Mim")
    wn.bgcolor("light blue")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"


 # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

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

# Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(toggle_pause, "p")