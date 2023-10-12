from windows import *
# ---------------------------------------------------------------------------------#
# ----------------------------------对话显示栏--------------------------------------#
# ---------------------------------------------------------------------------------#
Dialog_box = tk.Text(
    window,
    width=Dialog_box_size[0],
    height=Dialog_box_size[1],
    bg=colors[0],
    fg=colors[1],
    font=(font_style, font_size),
    highlightcolor="#1E1E1E",
    highlightthickness=2,
)
Dialog_box.config(state=tk.DISABLED)  # 设置为不可编辑
if __name__ == "__main__":
    Dialog_box.grid(row=0, column=0, columnspan=1, sticky=tk.NSEW)
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.insert(tk.END, "1\n2\n3\n4\n")
    Dialog_box.config(state=tk.DISABLED)
    print(Dialog_box.get("1.0", tk.END))
    window.mainloop()
