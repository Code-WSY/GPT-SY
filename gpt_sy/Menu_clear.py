from Box_Dialog import *
from Box_Message import *
from Menu_mode import *

def clear_display():
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.delete(0.0, tk.END)
    Dialog_box.config(state=tk.DISABLED)

def clear_mode_history():
    #获取当前模式Dialog_box的内容
    chat_history[selected_mode.get()].clear()
    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "成功清空当前模式的历史对话")
    Message_box.config(state=tk.DISABLED)
def clear_all():
    clear_display()
    clear_mode_history()

# -----------------------------------------------------------------------------------#
filemenu_clear = tk.Menu(menubar, tearoff=0)
#menubar.add_cascade(label="清空", menu=filemenu_clear)
clear_com = tk.StringVar()
filemenu_clear.add_command(label="清屏", command=lambda: clear_display())
filemenu_clear.add_command(label="清空对话", command=lambda: clear_all())

if __name__ == "__main__":
    window.mainloop()
