from tkinter import *
from tkinter import ttk

expression = ""


def buttonClick(inputnum):
    global expression
    # concatenation of string
    expression = expression + str(inputnum)
    # update the expression by using set method
    equation.set(expression)


def key_pressed(e):
    inputChar = e.char
    if inputChar == '1':
        buttonClick(1)
    elif inputChar == '2':
        buttonClick(2)
    elif inputChar == '3':
        buttonClick(3)
    elif inputChar == '4':
        buttonClick(4)
    elif inputChar == '5':
        buttonClick(5)
    elif inputChar == '6':
        buttonClick(6)
    elif inputChar == '7':
        buttonClick(7)
    elif inputChar == '8':
        buttonClick(8)
    elif inputChar == '9':
        buttonClick(9)
    elif inputChar == '0':
        buttonClick(0)
    elif inputChar == '+' or inputChar == '-' or inputChar == '*' or inputChar == '/':
        buttonClick(inputChar)
    elif inputChar == '=':
        calculateTotal()


def calculateTotal():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""


if __name__ == '__main__':
    window = Tk()
    # window.geometry("500x500")
    window.title("Calculator")
    equation = StringVar()
    expression_field = Entry(window, textvariable=equation)
    expression_field.grid(columnspan=5, ipadx=70)

    window.resizable(True, True)
    ttk.Button(window, text="1", command=lambda: buttonClick(1)).grid(column=1, row=1)
    ttk.Button(window, text="2", command=lambda: buttonClick(2)).grid(column=2, row=1)
    ttk.Button(window, text="3", command=lambda: buttonClick(3)).grid(column=3, row=1)
    ttk.Button(window, text="+", command=lambda: buttonClick('+')).grid(column=4, row=1)

    ttk.Button(window, text="4", command=lambda: buttonClick(4)).grid(column=1, row=2)
    ttk.Button(window, text="5", command=lambda: buttonClick(5)).grid(column=2, row=2)
    ttk.Button(window, text="6", command=lambda: buttonClick(6)).grid(column=3, row=2)
    ttk.Button(window, text="-", command=lambda: buttonClick('-')).grid(column=4, row=2)

    ttk.Button(window, text="7", command=lambda: buttonClick(7)).grid(column=1, row=3)
    ttk.Button(window, text="8", command=lambda: buttonClick(8)).grid(column=2, row=3)
    ttk.Button(window, text="9", command=lambda: buttonClick(9)).grid(column=3, row=3)
    ttk.Button(window, text="*", command=lambda: buttonClick('*')).grid(column=4, row=3)

    ttk.Button(window, text="0", command=lambda: buttonClick(0)).grid(row=4, columnspan=4, sticky='nsew')
    ttk.Button(window, text="/", command=lambda: buttonClick('/')).grid(column=4, row=4)
    ttk.Button(window, text="=", command=lambda: calculateTotal()).grid(columnspan=5, row=5, sticky='nsew')

    window.bind("<Key>", key_pressed)
    window.mainloop()
