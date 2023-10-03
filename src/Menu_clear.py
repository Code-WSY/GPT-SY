from Bottom_Submit import *

def clear_display():
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.delete(0.0, tk.END)
    Dialog_box.config(state=tk.DISABLED)


def clear_messages_list():
    messages_list.set("[]")
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete(0.0, tk.END)
    model_message_box.insert("insert", "成功清空对话记录")
    model_message_box.config(state=tk.DISABLED)


# -----------------------------------------------------------------------------------#
filemenu_clear = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="清空", menu=filemenu_clear)
clear_com = tk.StringVar()
filemenu_clear.add_command(label="清空对话框", command=lambda: clear_display())
filemenu_clear.add_command(label="清空对话记录", command=lambda: clear_messages_list())

if __name__ == "__main__":
    window.mainloop()
