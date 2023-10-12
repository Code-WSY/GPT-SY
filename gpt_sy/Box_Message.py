from windows import *

"""
设计：
    1.显示模型信息
    2.显示模型信息
    3.显示提示信息

输出：
    1.Message_box：显示信息（外部获取内容：Message_box.get()）

"""
# ---------------------------------------------------------------------------------#
# ------------------------------------显示模型信息----------------------------------------#
# ---------------------------------------------------------------------------------#
Message_box = tk.Text(window, bg=colors[2], fg=colors[3], highlightthickness=8, highlightcolor="#1E1E1E")
Message_box.insert(tk.END, "未登录")
Message_box.config(font=(font_style, font_size))
Message_box.config(width=message_box_size[0], height=message_box_size[1])
Message_box.config(state=tk.DISABLED)

# ---------------------------------------------------------------------------------#
if __name__ == "__main__":
    Message_box.grid(row=0, column=0, sticky=tk.NSEW)
    Message_box.config(state=tk.NORMAL)
    Message_box.delete("1.0", "end")
    Message_box.insert(tk.END, "123\n456")
    Message_box.config(state=tk.DISABLED)
    window.mainloop()
