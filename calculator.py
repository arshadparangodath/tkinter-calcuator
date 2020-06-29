from tkinter import *


value = ""

#defining buttons and it's functions
def btn_clicked(number):
    current = label.get()
    label.delete(0, END)
    label.insert(0, str(current) + str(number))

def btn_clear():
    label.delete(0, END)

def btn_add():
    first_number = label.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    label.delete(0, END)

def btn_substract():
    first_number = label.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    label.delete(0, END)

def btn_multiply():
    first_number = label.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    label.delete(0, END)

def btn_equals():
    second_number = label.get()
    label.delete(0, END)

    if math == "addition":
        label.insert(0, f_num + int(second_number))
    if math == "subtraction":
        label.insert(0, f_num - int(second_number))
    if math == "multiplication":
        label.insert(0, f_num * int(second_number))
    if math == "division":
        label.insert(0, f_num / int(second_number))



def btn_devide():
    first_number = label.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    label.delete(0, END)

window = Tk()
window.geometry("250x400+300+300")
window.resizable(0,0)  #couldn't resize the window
window.title("MAP Calculator")

#text appear field
frame = Frame(
    window,
    borderwidth = 5,
    relief = SUNKEN,
)
label = Entry(
    window,
    bg = "black",
    fg = "#ed7f09",
    font = "30",
    width = 30,
    borderwidth = 15,
    relief = FLAT,
)
label.pack(expand=True, fill="both")

#button row 1
btnr1 = Frame(window,)
btnr1.pack(expand=True, fill="both",)

btn1 = Button(
    btnr1,
    text="7",
    font="Verdana, 22",
    bg="black",
    fg = "gray",
    relief = GROOVE,
    border = 0,
    command = lambda: btn_clicked(7),
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnr1,
    text="8",
    bg="black",
    fg = "gray",
    font=("Verdana, 22"),
    relief = GROOVE,
    command = lambda: btn_clicked(8),
    border = 0,

)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    btnr1,
    text="9",
    bg="black",
    fg="gray",
    font=("Verdana, 22"),
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(9),
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4 = Button(
    btnr1,
    text="+",
    bg="black",
    fg="#ed7f09",
    font="Verdana, 22",
    relief = GROOVE,
    border = 0,
    command = btn_add
)
btn4.pack(side=LEFT, expand=True, fill="both",)


#button row 2
btnr2 = Frame(window,)
btnr2.pack(expand=True, fill="both",)

btn1 = Button(
    btnr2,
    bg="black",
    fg="gray",
    text="4",
    font="Verdana, 22",
    relief = GROOVE,
    command = lambda: btn_clicked(4),
    border = 0,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnr2,
    bg="black",
    fg="gray",
    text="5",
    font=("Verdana, 22"),
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(5),
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    btnr2,
    bg="black",
    fg="gray",
    text="6",
    font=("Verdana, 22"),
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(6),
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4 = Button(
    btnr2,
    text="-",
    font="Verdana, 22",
    bg="black",
    fg="#ed7f09",
    relief = GROOVE,
    border = 0,
    command = btn_substract
)
btn4.pack(side=LEFT, expand=True, fill="both",)

#button row 3
btnr3 = Frame(window, bg = "lightgray")
btnr3.pack(expand=True, fill="both",)

btn1 = Button(
    btnr3,
    bg="black",
    fg="gray",
    text="1",
    font="Verdana, 22",
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(1),
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnr3,
    bg="black",
    fg="gray",
    text="2",
    font=("Verdana, 22"),
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(2),
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    btnr3,
    text="3",
    font=("Verdana, 22"),
    bg="black",
    fg="gray",
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(3),
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4 = Button(
    btnr3,
    text="x",
    bg="black",
    fg="#ed7f09",
    font="Verdana, 22",
    relief = GROOVE,
    border = 0,
    command = btn_multiply,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

#button row 4
btnr4 = Frame(window, bg = "gray")
btnr4.pack(expand=True, fill="both",)

btn1 = Button(
    btnr4,
    bg="black",
    fg="gray",
    text="0",
    font="Verdana, 22",
    relief = GROOVE,
    border = 0,
    command=lambda: btn_clicked(0),
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnr4,
    text="C",
    bg="black",
    fg="#ed7f09",
    font=("Verdana, 22"),
    relief = GROOVE,
    border = 0,
    command = btn_clear,
)
btn2.pack(side=LEFT, expand=True, fill="both",)


btn3 = Button(
    btnr4,
    text="=",
    bg="black",
    fg="#ed7f09",
    font=("Verdana, 22"),
    relief = GROOVE,
    border = 0,
    command = btn_equals,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4 = Button(
    btnr4,
    text="/",
    bg="black",
    fg="#ed7f09",
    font="Verdana, 22",
    relief = GROOVE,
    border = 0,
    command = btn_devide,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

window.mainloop()
