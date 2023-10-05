from windows import *

"""
设计：
    1.显示模型信息
    2.显示模型信息
    3.显示提示信息

输出：
    1.model_message_box：显示模型信息（外部获取内容：model_message_box.get()）

"""
# ---------------------------------------------------------------------------------#
# ------------------------------------显示模型信息----------------------------------------#
# ---------------------------------------------------------------------------------#
model_message_box = tk.Text(window, bg=colors[1], fg=colors[2])
model_message_box.insert(tk.END, "未登录")
model_message_box.config(font=(font_style, font_size + 4))
model_message_box.config(width=message_box_size[0], height=message_box_size[1])
model_message_box.config(state=tk.DISABLED)

# ---------------------------------------------------------------------------------#
if __name__ == "__main__":
    model_message_box.grid(row=0, column=0, sticky=tk.NSEW)
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete("1.0", "end")
    model_message_box.insert(tk.END, "123\n456")
    model_message_box.config(state=tk.DISABLED)
    window.mainloop()
