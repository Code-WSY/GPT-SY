from windows import *
# -----------------------------------------------------------------------------------#
# 创建一个菜单
filemenu_mode = tk.Menu(menubar, tearoff=0)
#menubar.add_cascade(label="模式 ", menu=filemenu_mode)
# -----------------------------------------------------------------------------------#
selected_mode = tk.StringVar()
mode_dict_list=list(mode_dict.keys())
mode_dict_list.sort()
for i in mode_dict_list:
    filemenu_mode.add_radiobutton(
        label=i, variable=selected_mode, value=i
    )

# 默认选中的模式
# 注意，修改后，需要在UI.py中的init_UI()函数中修改提交按钮的绑定函数
selected_mode.set(mode_dict_list[1])

if __name__ == "__main__":
    window.mainloop()
