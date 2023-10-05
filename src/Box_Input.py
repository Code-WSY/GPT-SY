from windows import *
# ---------------------------------------------------------------------------------#
# ----------------------------------输入栏-----------------------------------------#
# ---------------------------------------------------------------------------------#
# 创建一个文本消息框，用于显示内容，
Input_box = tk.Text(window, bg=colors[2])
# 框的大小
Input_box.config(width=Input_box_size[0], height=Input_box_size[1])
Input_box.config(state="normal")
Input_box.config(font=(font_style, font_size + 2))

# ---------------------------------------------------------------------------------#
# 创建两个输入框，用于输入内容
temperature_box = tk.Entry(window, width=temperature_box_size[0])
temperature_box.insert(0, "0.6")

max_tokens_box = tk.Entry(window, width=max_tokens_box_size[0])
max_tokens_box.insert(0, "50")

# 创建两个标签，用于显示提示信息
temperature_label = tk.Label(window, text="温度[0,1]：")
max_tokens_label = tk.Label(window, text="输出长度(tokens)：")
# 右对齐
temperature_label.config(anchor=tk.E)
max_tokens_label.config(anchor=tk.E)
# 字体
temperature_label.config(font=(font_style, font_size + 2))
temperature_label.config(
    width=temperature_label_size[0], height=temperature_label_size[1]
)

temperature_box.config(font=(font_style, font_size + 1))
max_tokens_label.config(font=(font_style, font_size + 2))
max_tokens_label.config(width=max_tokens_label_size[0], height=max_tokens_label_size[1])
max_tokens_box.config(font=(font_style, font_size + 1))

if __name__ == "__main__":
    # ---------------------------------------------------------------------------------#
    # 显示
    Input_box.grid(row=0, column=0,columnspan=4,sticky=tk.NSEW)
    temperature_label.grid(row=1, column=0, sticky=tk.E)
    temperature_box.grid(row=1, column=1, sticky=tk.W)
    max_tokens_label.grid(row=1, column=2, sticky=tk.E)
    max_tokens_box.grid(row=1, column=3, sticky=tk.W)

    window.mainloop()
