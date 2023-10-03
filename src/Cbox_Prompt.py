from windows import *
from tkinter.ttk import Combobox
# ---------------------------------------------------------------------------------#
"""
设计：
    创建一个下拉框，选项为可用的功能
    选中后更改标签的值
输出：
    func_list：下拉框（外部获取：func_list.get()：选中的值）
    Label_func：标签（外部获取：Label_func.cget("text")）
    
"""


def on_combobox_select_func(event):
    func = func_list.get()
    # Label_func.config(text="功能: " + func)
    Label_func.config(text="功能: ")


# 标签：
Label_func = tk.Label(window, text="功能：")
Label_func.config(width=Label_func_size[0], height=Label_func_size[1])
Label_func.config(fg="black", font=(font_style, font_size + 2))
# 左对齐
Label_func.config(anchor=tk.E)
# 下拉框：
selected_func = tk.StringVar()
selected_func.set("初始对话")
func_list = Combobox(
    window, values=list(prompts.keys()), textvariable=selected_func, state="readonly"
)
# 设置长度
func_list.config(width=ComboBox_func_size[0])
func_list.bind("<<ComboboxSelected>>", on_combobox_select_func)
# 字体
func_list.config(font=(font_style, font_size))

if __name__ == "__main__":
    Label_func.grid(row=0, column=0, sticky=tk.W)
    func_list.grid(row=0, column=1, sticky=tk.W)

    window.mainloop()
