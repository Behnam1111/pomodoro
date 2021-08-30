from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'normal'))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=PINK, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=PINK, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = Label(text="✔", bg=YELLOW)
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)







window.mainloop()