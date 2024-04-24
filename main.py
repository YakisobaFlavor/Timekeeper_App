from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
SUB_FONT = ("Courier", 10, "bold")
TIMER_FONT = ("Courier", 15)
TITLE_FONT = ("Courier", 30, "bold")
MAIN_FONT = ("Courier", 12, "bold")
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def time_reset():
    window.after_cancel(timer)
    header_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(main_img, image=idle_img)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def time_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    canvas.itemconfig(main_img, image=working_img)
    if reps % 8 == 0:
        count_down(long_break_min)
        header_label.config(text="Long Break!\nGet a Coffee", fg=RED)
        canvas.itemconfig(main_img, image=long_break_img)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        header_label.config(text="Short Break!\nTake a Deep Breath", fg=PINK)
        canvas.itemconfig(main_img, image=short_break_img)
    elif reps % 2 == 1:
        count_down(work_sec)
        header_label.config(text="Work Time!\nFocus Bro", fg="black")
        canvas.itemconfig(main_img, image=working_img)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min =  math.floor(count/60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        time_start()
        marks = ""
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            marks += "✓"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Working Alarm")
window.config(padx=20, pady=20, bg=YELLOW)

idle_img = PhotoImage(file="anya_ganbatta_face.png")
working_img = PhotoImage(file="anya_cunning_face.png")
short_break_img = PhotoImage(file="anya_short_breath.png")
long_break_img = PhotoImage(file="anya_heh_face.png")

canvas = Canvas(width=260, height=300)
main_img = canvas.create_image(130, 140, image=idle_img)
timer_text = canvas.create_text(130, 280, text="00:00", fill="black", font=TIMER_FONT)
canvas.grid(row=1, column=1)

header_label = Label(text="Timer", fg="black", bg=YELLOW, font=MAIN_FONT)
header_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=time_start, font=SUB_FONT)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=time_reset, font=SUB_FONT)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()