from tkinter.ttk import Combobox
from Box_Message import *
from Menu_mode import *
def display_model_message(event):
    Message_box.config(state=tk.NORMAL)
    Message_box.delete("1.0", "end")
    Message_box.insert(tk.END, model_list.get() + ":\n")
    model_message_info = model_message[model_list.get()]
    Message_box.insert(tk.END, model_message_info)
    # 字体
    Message_box.config(font=(font_style, font_size + 4))
    # 尺寸
    Message_box.config(width=message_box_size[0], height=message_box_size[1])
    Message_box.config(state=tk.DISABLED)
    Message_box.update()

#先获取当前的模式
selected_model = tk.StringVar()
#获得当前的模式
selected_model.set(mode_dict[selected_mode.get()][0])
#创建下拉框
model_list_list = mode_dict[selected_mode.get()]
model_list = Combobox(
    window, values=model_list_list
    , textvariable=selected_model, state="readonly",background=colors[2],foreground=colors[3],
)
#绑定事件：模式改变时，改变模型列表
def change_model_list(event):
    model_list.config(values=mode_dict[selected_mode.get()])
    model_list.current(0)#设置默认值,即默认选择第一个
# -----------------------------------------------------------------------------------#
#绑定
selected_mode.trace("w", lambda *args: change_model_list(None))


# 设置 Combobox 的样式
model_list.config(width=ComboBox_model_size[0])
model_list.config(font=cbox_font)
# 设置 Combobox 的颜色
model_list.config(background=cbox_colors[2], foreground=cbox_colors[3])
Label_model = tk.Label(window, text="模型：")
# 设置 Label 的样式
Label_model.config(anchor=tk.E)
Label_model.config(width=Label_model_size[0], height=Label_model_size[1])
Label_model.config(bg=cbox_colors[0], fg=cbox_colors[1], font=cbox_font)
# 绑定事件
model_list.bind("<<ComboboxSelected>>", display_model_message)

if __name__ == "__main__":
    Label_model.grid(row=0, column=0, sticky=tk.W)
    model_list.grid(row=0, column=1, sticky=tk.W)
    window.mainloop()
