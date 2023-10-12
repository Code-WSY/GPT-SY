from windows import *
# -----------------------------------------------------------------------------------#
# 创建一个菜单
filemenu_mode = tk.Menu(menubar, tearoff=0)
#menubar.add_cascade(label="模式 ", menu=filemenu_mode)
# -----------------------------------------------------------------------------------#
selected_mode = tk.StringVar()
selected_mode.set("ChatCompletion")
mode_dict_list=list(mode_dict.keys())
mode_dict_list.sort()
for i in mode_dict_list:
    filemenu_mode.add_radiobutton(
        label=i, variable=selected_mode, value=i
    )
selected_mode.set(mode_dict_list[0])


if __name__ == "__main__":
    window.mainloop()
