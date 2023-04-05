import tkinter as tk

calculation = ""

# ===== Functions =====
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Result Object
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Clear Object
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# ===== Root Tkinter
window = tk.Tk()
window.title("Calculator")
window.iconbitmap('icon.ico')
window.resizable(False, False)

# ===== Result =====
text_result = tk.Text(window, height=2, width=9, font=("Inter", 24))
text_result.grid(columnspan=5)

# ===== Numbers buttons =====
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=3, font=("Inter", 14), bg="#eeeee4")
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=3, font=("Inter", 14), bg="#eeeee4")
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=3, font=("Inter", 14), bg="#eeeee4")
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=3, font=("Inter", 14), bg="#eeeee4")
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=3, font=("Inter", 14), bg="#eeeee4")
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=3, font=("Inter", 14), bg="#eeeee4")
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=3, font=("Inter", 14), bg="#eeeee4")
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=3, font=("Inter", 14), bg="#eeeee4")
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=3, font=("Inter", 14), bg="#eeeee4")
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=3, font=("Inter", 14), bg="#eeeee4")
btn_0.grid(row=5, column=2)

# ===== Clear Button =====
btn_clear = tk.Button(window, text="C", command=clear_field, width=3, font=("Inter", 14), bg="#E27268")
btn_clear.grid(row=2, column=4)

# ===== Operators Buttons =====
btn_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width=3, font=("Inter", 14), bg="#c1c1c1")
btn_plus.grid(row=3, column=4)

btn_minus = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width=3, font=("Inter", 14), bg="#c1c1c1")
btn_minus.grid(row=4, column=4)

btn_mutp = tk.Button(window, text="*", command=lambda: add_to_calculation("*"), width=3, font=("Inter", 14), bg="#c1c1c1")
btn_mutp.grid(row=5, column=4)

btn_div = tk.Button(window, text="/", command=lambda: add_to_calculation("/"), width=3, font=("Inter", 14), bg="#c1c1c1")
btn_div.grid(row=6, column=4)

btn_open = tk.Button(window, text="(", command=lambda: add_to_calculation("("), width=3, font=("Inter", 14), bg="#abdbe3")
btn_open.grid(row=5, column=1)

btn_close = tk.Button(window, text=")", command=lambda: add_to_calculation(")"), width=3, font=("Inter", 14), bg="#abdbe3")
btn_close.grid(row=5, column=3)

# ===== Equal Button =====
btn_equal = tk.Button(window, text="=", command=evaluate_calculation, width=7, font=("Inter", 14), bg="#36F2B3")
btn_equal.grid(row=6, column=1, columnspan=2)

btn_dot = tk.Button(window, text=".", command=lambda: add_to_calculation("."), width=3, font=("Inter", 14), bg="#eab676")
btn_dot.grid(row=6, column=3)

# Run
window.mainloop()