import tkinter as tk
from tkinter import ttk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

# 创建一个扁平风格的按钮
style = ttk.Style()
style.configure("alt.TButton", relief="flat", background="#ccc", borderwidth=0)
#还有其他的风格，如：sunken, raised, groove, ridge
style.map("Flat.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')]
            )

# 创建按钮并应用样式
button = ttk.Button(root, text="Click Me", style="Flat.TButton", command=button_clicked)
button.pack()

root.mainloop()
