import os
import tkinter.filedialog
from Box_Input import *
from Cbox_Prompt import *
from Cbox_Model import *
def open_file():
    file_path = tk.filedialog.askopenfilename(
        title="选择文件", filetypes=[("All Files", "*")]
    )
    with open(file_path, "r", encoding="utf-8") as f:
        Input_box.delete("1.0", "end")
        Input_box.insert(tk.END, f.read())


def save_file():
    #先查看文件夹是否存在
    if not os.path.exists(save_file_path[0]):
        os.mkdir(save_file_path[0])
    save_file_name = save_file_path[0] + selected_model.get() + "_" + selected_prompt.get() + ".txt"
    # 查看是否有重复文件
    try:
        i = 1
        while True:
            # 打开文件
            f = open(save_file_name, "r", encoding="utf-8")
            f.close()
            # 上面的语句没有报错(能读取)，说明文件存在
            save_file_name = (
                    save_file_path[0]
                    + selected_model.get()
                    + "_"
                    + selected_prompt.get()
                    + "_"
                    + str(i)
                    + ".txt"
            )
            i += 1
    except:
        with open(save_file_name, "w", encoding="utf-8") as f:
            for message in chat_history:
                f.write(str(message) + "\n")

    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "已保存：\n   " + save_file_name + "\n")
    Message_box.config(state=tk.DISABLED)
    Message_box.update()


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
