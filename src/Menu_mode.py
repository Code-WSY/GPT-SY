import tkinter as tk
from windows import window, menubar

# -----------------------------------------------------------------------------------#
# 创建一个菜单
filemenu_mode = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="模式", menu=filemenu_mode)
selected_mode = tk.StringVar()
filemenu_mode.add_radiobutton(
    label="Prompt-based", variable=selected_mode, value="Prompt-based"
)
filemenu_mode.add_radiobutton(
    label="Fine-tuning", variable=selected_mode, value="Fine-tuning"
)
selected_mode.set("Prompt-based")

if __name__ == "__main__":
    window.mainloop()
