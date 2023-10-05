import tkinter as tk
from sympy import sympify
calculation = ""

def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def eval_calc():
    global calculation
    try:
        calculation = str(sympify(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except ZeroDivisionError:
        clearfield()
        text_result.insert(1.0, "Error")
    

def clearfield():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def erase():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

root = tk.Tk()
root.title("Calculator")
root.geometry("390x330")
text_result = tk.Text(root, height=3, width=24, font=("Arial",24))
text_result.grid(columnspan=7)

btn_1 =tk.Button(root, text="1", command= lambda: add_to_calc(1), width=5, font=("Arial", 16))
btn_1.grid(row=2, column=1)
btn_2 =tk.Button(root, text="2", command= lambda: add_to_calc(2), width=5, font=("Arial", 16))
btn_2.grid(row=2, column=2)
btn_3 =tk.Button(root, text="3", command= lambda: add_to_calc(3), width=5, font=("Arial", 16))
btn_3.grid(row=2, column=3)
btn_4 =tk.Button(root, text="4", command= lambda: add_to_calc(4), width=5, font=("Arial", 16))
btn_4.grid(row=3, column=1)
btn_5 =tk.Button(root, text="5", command= lambda: add_to_calc(5), width=5, font=("Arial", 16))
btn_5.grid(row=3, column=2)
btn_6 =tk.Button(root, text="6", command= lambda: add_to_calc(6), width=5, font=("Arial", 16))
btn_6.grid(row=3, column=3)
btn_7 =tk.Button(root, text="7", command= lambda: add_to_calc(7), width=5, font=("Arial", 16))
btn_7.grid(row=4, column=1)
btn_8 =tk.Button(root, text="8", command= lambda: add_to_calc(8), width=5, font=("Arial", 16))
btn_8.grid(row=4, column=2)
btn_9 =tk.Button(root, text="9", command= lambda: add_to_calc(9), width=5, font=("Arial", 16))
btn_9.grid(row=4, column=3)
btn_0 =tk.Button(root, text="0", command= lambda: add_to_calc(0), width=5, font=("Arial", 16))
btn_0.grid(row=5, column=2)
btn_open =tk.Button(root, text="(", command= lambda: add_to_calc("("), width=5, font=("Arial", 16))
btn_open.grid(row=5, column=1)
btn_close =tk.Button(root, text=")", command= lambda: add_to_calc(")"), width=5, font=("Arial", 16))
btn_close.grid(row=5, column=3)
btn_plus =tk.Button(root, text="+", command= lambda: add_to_calc("+"), width=5, font=("Arial", 16))
btn_plus.grid(row=2, column=4)
btn_minus =tk.Button(root, text="-", command= lambda: add_to_calc("-"), width=5, font=("Arial", 16))
btn_minus.grid(row=3, column=4)
btn_mul =tk.Button(root, text="*", command= lambda: add_to_calc("*"), width=5, font=("Arial", 16))
btn_mul.grid(row=4, column=4)
btn_div =tk.Button(root, text="/", command= lambda: add_to_calc("/"), width=5, font=("Arial", 16))
btn_div.grid(row=5, column=4)
btn_Clr =tk.Button(root, text="Clr", command= clearfield, width=5, font=("Arial", 16))
btn_Clr.grid(row=6, column=4)
btn_eqauls =tk.Button(root, text="=", command= eval_calc, width=13, font=("Arial", 16))
btn_eqauls.grid(row=6, column=1, columnspan=2)
btn_Ers =tk.Button(root, text="←", command= erase, width=5, font=("Arial", 16))
btn_Ers.grid(row=6, column=3)
root.mainloop()
