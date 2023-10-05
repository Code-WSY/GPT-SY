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
prompts_list.config(font=cbox_font)
# 设置 Combobox 的颜色
prompts_list.config(background=cbox_colors[6], foreground=cbox_colors[7])
# 标签：
Label_func = tk.Label(window, text="功能：")
Label_func.config(width=Label_func_size[0], height=Label_func_size[1],
                  bg=cbox_colors[4], fg=cbox_colors[5], font=cbox_font)
Label_func.config(anchor=tk.E)


if __name__ == "__main__":
    Label_func.grid(row=0, column=0, sticky=tk.W)
    prompts_list.grid(row=0, column=1, sticky=tk.W)

    window.mainloop()
