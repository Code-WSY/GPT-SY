import tkinter.filedialog
from Bottom_Submit import *


def open_file():
    file_path = tk.filedialog.askopenfilename(
        title="选择文件", filetypes=[("All Files", "*")]
    )
    with open(file_path, "r", encoding="utf-8") as f:
        Input_box.delete("1.0", "end")
        Input_box.insert(tk.END, f.read())


def save_file():
    # 保存messages:
    save_file_path = (
        "../Chat_history/" + model_list.get() + "_" + func_list.get() + ".txt"
    )
    # 查看是否有重复文件
    try:
        i = 1
        while True:
            # 打开文件
            f = open(save_file_path, "r", encoding="utf-8")
            f.close()
            # 上面的语句没有报错，说明文件存在
            save_file_path = (
                "../Chat_history/"
                + model_list.get()
                + "_"
                + func_list.get()
                + "_"
                + str(i)
                + ".txt"
            )
            i += 1
    except:
        # 逐个写入
        with open(save_file_path, "w", encoding="utf-8") as f:
            for message in eval(messages_list.get()):
                f.write(str(message) + "\n")
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete(0.0, tk.END)
    model_message_box.insert(tk.END, "已保存：\n   " + save_file_path + "\n")
    model_message_box.config(state=tk.DISABLED)


# -----------------------------------------------------------------------------------#
filemenu_file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="文件", menu=filemenu_file)
file_com = tk.StringVar()
filemenu_file.add_command(label="打开", command=lambda: open_file())
filemenu_file.add_command(label="保存", command=lambda: save_file())
filemenu_file.add_separator()
filemenu_file.add_command(label="退出", command=lambda: window.quit())

if __name__ == "__main__":
    window.mainloop()
