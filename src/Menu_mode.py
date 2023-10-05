from windows import *

# -----------------------------------------------------------------------------------#
# 创建一个菜单
filemenu_mode = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="模式 ", menu=filemenu_mode)
# -----------------------------------------------------------------------------------#
selected_mode = tk.StringVar()
for i in mode_list:
    filemenu_mode.add_radiobutton(
        label=i, variable=selected_mode, value=i
    )
selected_mode.set(mode_list[0])

if __name__ == "__main__":
    window.mainloop()
