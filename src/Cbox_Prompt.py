from windows import *
from tkinter.ttk import Combobox
# ---------------------------------------------------------------------------------#
# 下拉框：
selected_prompt = tk.StringVar()
selected_prompt.set("初始对话")
prompts_list = Combobox(
    window, values=list(prompts.keys()), textvariable=selected_prompt, state="readonly"
)
# 设置 Combobox 的样式
prompts_list.config(width=ComboBox_func_size[0])
prompts_list.config(font=(font_style, font_size))
# 标签：
Label_func = tk.Label(window, text="功能：")
Label_func.config(width=Label_func_size[0], height=Label_func_size[1])
Label_func.config(fg="black", font=(font_style, font_size + 2))
Label_func.config(anchor=tk.E)


if __name__ == "__main__":
    Label_func.grid(row=0, column=0, sticky=tk.W)
    prompts_list.grid(row=0, column=1, sticky=tk.W)

    window.mainloop()
