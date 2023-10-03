from Config import *
import tkinter as tk
# -----------------------------------------------------------------------------------#
# ------------------------------------主窗口------------------------------------------#
# -----------------------------------------------------------------------------------#
window = tk.Tk()
window.title(NAME)
window.resizable(width=True, height=True)
logo = tk.PhotoImage(file="../pic/logo.png")
window.iconphoto(True, logo)
# 创建一个顶层菜单栏
menubar = tk.Menu(window)
window.config(menu=menubar)
# 设置菜单栏颜色
menubar.config(bg=colors[2])
if __name__ == "__main__":
    # 进入消息循环
    window.mainloop()
