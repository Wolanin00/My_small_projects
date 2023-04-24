from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(id=str(timer))
    title_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, check_mark
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown_mechanism(long_break_sec)
        title_label.config(text='Long Break', fg=PINK)
    elif reps % 2 == 0:
        countdown_mechanism(short_break_sec)
        title_label.config(text='Short Break', fg=RED)
    else:
        countdown_mechanism(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_mechanism(count):
    time1 = time.strftime("%M:%S", time.gmtime(count))
    canvas.itemconfig(timer_text, text=time1)
    if count > -1:
        global timer
        timer = window.after(1000, countdown_mechanism, count-1)
    else:
        start_timer()
        check_label.config(text=math.floor(reps / 2) * '✔')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato-timer")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 32, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=220, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(foreground=GREEN, background=YELLOW, font="bold")
check_label.grid(column=1, row=3)


window.mainloop()
