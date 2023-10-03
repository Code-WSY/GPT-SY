import tkinter as tk
from tkinter.ttk import Combobox
from windows import window
from config import (
    font_style,
    font_size,
    model_message,
    Label_model_size,
    model_use,
    message_box_size,
    ComboBox_model_size,
)
from Box_Message import model_message_box


"""
设计：
    创建一个下拉框，选项为可用的模型
    选中后更改标签的值
输出：
    model_list：下拉框（外部获取：model_list.get()：选中的值）
    Label_model：标签内容（外部获取：Label_model.cget("text")）
"""


def on_combobox_select_model(event):
    # Label_model.config(text="模型: " + model_list.get())
    Label_model.config(text="模型: ")
    display_model_message(None)


# 与模型下拉框绑定，当模型改变时，输入框的内容也会改变
def display_model_message(event):
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete("1.0", "end")
    model_message_box.insert("insert", model_list.get() + ":\n")
    model_message_info = model_message[model_list.get()]
    model_message_box.insert("insert", model_message_info)
    # 字体
    model_message_box.config(font=(font_style, font_size + 4))
    # 尺寸
    model_message_box.config(width=message_box_size[0], height=message_box_size[1])
    model_message_box.config(state=tk.DISABLED)


Label_model = tk.Label(window, text="模型：")
# 左对齐
Label_model.config(anchor=tk.E)
Label_model.config(width=Label_model_size[0], height=Label_model_size[1])
Label_model.config(fg="black", font=(font_style, font_size + 2))
selected_model = tk.StringVar()
selected_model.set("gpt-3.5-turbo")
model_list = Combobox(
    window, values=list(model_use.keys()), textvariable=selected_model, state="readonly"
)
# 设置长度
model_list.config(width=ComboBox_model_size[0])
model_list.bind("<<ComboboxSelected>>", on_combobox_select_model)
# 模型下拉框的大小
# 字体
model_list.config(font=(font_style, font_size))
# model_list.config(width=Label_model_size[0], height=Label_model_size[1])

if __name__ == "__main__":
    Label_model.grid(row=0, column=0, sticky=tk.W)
    model_list.grid(row=0, column=1, sticky=tk.W)
    window.mainloop()
