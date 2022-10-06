from tkinter import *
import time
import math

# Constant variables
# Color Images from colorhunt.co

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
cancel_timer = "None"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(cancel_timer)
    # reset to 00:00 & label reset to Timer
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 8th rep
    if reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
        # if it's the 2nd/4th/6th reps
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # if it's the 1st/3rd/5th/7th rep
        count_down(work_sec)
        timer.config(fg=GREEN)
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
            tick.config(text=marks)
        timer.config(text="Timer", fg=GREEN)


# ---------------------------- Countdown Mechanism ------------------------------- #
def count_down(count):
    # count in terms of minutes
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global cancel_timer
        cancel_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        timer.config(fg=GREEN)
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
            tick.config(text=marks)
        timer.config(text="Timer", fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.maxsize(width=500, height=400)

canvas = Canvas(width=205, height=230, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(103, 115, image=image)
canvas.grid(column=2, row=2)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer.grid(column=2, row=1)
tick = Label(fg=GREEN, background=YELLOW)
tick.grid(column=2, row=4)
start_button = Button(text="Start", highlightthickness=0, background=YELLOW, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", highlightthickness=0, background=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
