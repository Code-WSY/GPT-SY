import os
import tkinter.filedialog
from Box_Input import *
from Cbox_Prompt import *
from Cbox_Model import *
from scripts.check_mode import check_mode
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
    save_file_name = save_file_path[0] + selected_model.get() + "_" + selected_prompt_title.get() + ".txt"
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
                    + selected_prompt_title.get()
                    + "_"
                    + str(i)
                    + ".txt"
            )
            i += 1
    except:
        with open(save_file_name, "w", encoding="utf-8") as f:
            for message in chat_history[selected_mode.get()]:
                f.write(str(message) + "\n")

    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "已保存当前模式的对话：\n   " + save_file_name + "\n")
    Message_box.config(state=tk.DISABLED)
    Message_box.update()

def save_file_other():
    #先查看文件夹是否存在
    save_file_name = tk.filedialog.asksaveasfilename(
        title="另存为", filetypes=[("All Files", "*")]
    )
    with open(save_file_name, "w", encoding="utf-8") as f:
        for message in chat_history:
            f.write(str(message) + "\n")
    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "已保存：\n   " + save_file_name + "\n")
    Message_box.config(state=tk.DISABLED)
    Message_box.update()

def on_import_select(event):
    # 弹出一个窗口，选择文件
    import_file_path = tk.filedialog.askopenfilename()
    import_file_name = import_file_path.split("/")[-1]
    if check_mode(import_file_path, selected_mode.get()):
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "已导入文件：\n" + import_file_name + "\n"+"导入后请勿更改模式\n")
        Message_box.config(state=tk.DISABLED)
        # 将内容储存删除
        chat_history[selected_mode.get()].clear()
        with open(import_file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = eval(line)
                chat_history[selected_mode.get()].append(line)
    else:
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "导入失败\n" "请检查文件格式是否与当前模式输入一致。\n")
        #设置字体为红色
        Message_box.tag_add("tag1", "1.0", "end")
        Message_box.tag_config("tag1", foreground="red")#设置tag1的字体颜色为红色
        Message_box.config(state=tk.DISABLED)




# -----------------------------------------------------------------------------------#
filemenu_file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="文件", menu=filemenu_file)
file_com = tk.StringVar()
filemenu_file.add_command(label="打开", command=lambda: open_file())
filemenu_file.add_command(label="保存", command=lambda: save_file())
filemenu_file.add_command(label="另存为", command=lambda: save_file_other())
filemenu_file.add_command(label="导入历史记录", command=lambda: on_import_select(None))
filemenu_file.add_separator()
filemenu_file.add_command(label="退出", command=lambda: window.quit())

if __name__ == "__main__":
    window.mainloop()
