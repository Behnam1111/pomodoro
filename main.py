import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LIGHT = "#FFFFFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    checkmark_symbol = "✔"
    check_label.config(text=checkmark_symbol * int(reps / 2))
    if reps == 8:
        timer_label.config(text="REST", fg=RED)
        countdown(long_break)
    elif reps % 2 == 1:
        timer_label.config(text="WORK")
        countdown(work_sec)
    else:
        timer_label.config(text="BREAK", fg=PINK)
        countdown(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'normal'))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=LIGHT, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=LIGHT, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW)
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

window.mainloop()
