from windows import *
from tkinter.ttk import Combobox
from Menu_mode import *
# ---------------------------------------------------------------------------------#
# 下拉框：
# 先获取当前的模式
selected_prompt_title = tk.StringVar()
# 获得当前的模式
selected_prompt_title.set(mode_prompt_dict[selected_mode.get()][0])
selected_prompt_list= mode_prompt_dict[selected_mode.get()]
# 创建下拉框
prompts_list = Combobox(
    window,
    values=selected_prompt_list,
    textvariable=selected_prompt_title,
    state="readonly"
)
# 绑定事件：模式改变时，改变模型列表
def change_prompt_list(event):
    prompts_list.config(values=mode_prompt_dict[selected_mode.get()])
    prompts_list.current(0)  # 设置默认值,即默认选择第一个
# -----------------------------------------------------------------------------------#
# 绑定
selected_mode.trace("w", lambda *args: change_prompt_list(None))

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
