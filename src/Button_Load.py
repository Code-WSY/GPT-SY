from Box_Message import *
from tkinter import filedialog

"""
设计:
    1.导入按钮
    2.点击按钮之后弹出一个窗口，选择文件
    3.读取文件内容，并存入messages中
输出：
    1.Load_Content：导入的内容（外部获取：Load_Content.get()）
    3.LOAD_BOOL：是否导入成功的Bool值 (外部获取：LOAD_BOOL.get())
    4.ISLOAD：按钮的标签变量（外部获取：ISLOAD.get()）
"""


def on_import_select(event):
    # 弹出一个窗口，选择文件
    import_file_path = tk.filedialog.askopenfilename()
    try:
        # 选择之后读取文件内容，并存入messages中
        with open(import_file_path, "r", encoding="utf-8") as f:
            # 逐行读取并加入messages
            messages_load = []
            for line in f.readlines():
                line = eval(line)
                messages_load.append(line)
        Load_Content.set(str(messages_load))
        ISLOAD.set("已导入")
        model_message_box.config(state=tk.NORMAL)
        model_message_box.delete(0.0, tk.END)
        filename = import_file_path.split("/")[-1]
        model_message_box.insert(tk.END, f"已导入：\n   " + filename + "\n")
        LOAD_BOOL.set(True)
    except:
        ISLOAD.set("导入失败")
        model_message_box.config(state=tk.NORMAL)
        model_message_box.delete(0.0, tk.END)
        model_message_box.insert(tk.END, "导入失败\n" "请检查文件格式是否正确。\n")
        pass


Load_Content = tk.StringVar()
ISLOAD = tk.StringVar()
LOAD_BOOL = tk.BooleanVar()

# 默认值
ISLOAD.set("未导入")
Load_Content.set("")
LOAD_BOOL.set(False)

# 创建一个按钮，点击之后弹出一个窗口，选择文件
import_button = tk.Button(
    window,
    textvariable=ISLOAD,
    command=lambda: on_import_select(None),
)
# 按钮的大小
import_button.config(width=import_button_size[0], height=import_button_size[1])
import_button.config(font=(font_style, font_size))
# 导入标签
import_label = tk.Label(window, text="导入文件：")
import_label.config(font=(font_style, font_size + 2))
# 字体

if __name__ == "__main__":
    import_label.grid(row=0, column=0, sticky=tk.N)
    import_button.grid(row=0, column=1, sticky=tk.N)
    window.mainloop()
