from tkinter.ttk import Combobox
from Box_Message import *
def display_model_message(event):
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete("1.0", "end")
    model_message_box.insert(tk.END, model_list.get() + ":\n")
    model_message_info = model_message[model_list.get()]
    model_message_box.insert(tk.END, model_message_info)
    # 字体
    model_message_box.config(font=(font_style, font_size + 4))
    # 尺寸
    model_message_box.config(width=message_box_size[0], height=message_box_size[1])
    model_message_box.config(state=tk.DISABLED)


selected_model = tk.StringVar()
selected_model.set("gpt-3.5-turbo")
model_list = Combobox(
    window, values=list(model_use_format.keys()), textvariable=selected_model, state="readonly"
)

# 设置 Combobox 的样式
model_list.config(width=ComboBox_model_size[0])
model_list.config(font=(font_style, font_size))
Label_model = tk.Label(window, text="模型：")
# 设置 Label 的样式
Label_model.config(anchor=tk.E)
Label_model.config(width=Label_model_size[0], height=Label_model_size[1])
Label_model.config(fg="black", font=(font_style, font_size + 2))
# 绑定事件
model_list.bind("<<ComboboxSelected>>", display_model_message)

if __name__ == "__main__":
    Label_model.grid(row=0, column=0, sticky=tk.W)
    model_list.grid(row=0, column=1, sticky=tk.W)
    window.mainloop()
