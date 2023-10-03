import tkinter as tk
from windows import window
from config import font_style, font_size, Dialog_box_size, colors

# ---------------------------------------------------------------------------------#
# ----------------------------------对话显示栏--------------------------------------#
# ---------------------------------------------------------------------------------#
"""
设计：
    1.对话框
    2.滚动条
输出：
    1.Dialog_box：对话框（外部获取内容：Dialog_box.get()）
"""
Dialog_box = tk.Text(
    window,
    width=Dialog_box_size[0],
    height=Dialog_box_size[1],
    bg=colors[0],
    fg="#EEEEEE",
    font=(font_style, font_size + 2),
    highlightcolor="#1E1E1E",
    highlightthickness=0,
)
Dialog_box.config(state=tk.DISABLED)  # 设置为不可编辑


if __name__ == "__main__":
    Dialog_box.grid(row=0, column=0, columnspan=1, sticky=tk.NSEW)
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.insert("insert", "123\n456\n\n\n\n\n\n\n`1121\n\n\n\n\n`")
    Dialog_box.config(state=tk.DISABLED)
    print(Dialog_box.get("1.0", tk.END))
    window.mainloop()
