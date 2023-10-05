from Box_Message import *
from tkinter import filedialog
from scripts.check_format import check_format

"""
导入按钮：
导入的格式必须正确
要保证历史记录：chat_history不出错

"""
def on_import_select(event):
    # 弹出一个窗口，选择文件
    import_file_path = tk.filedialog.askopenfilename()
    #获取文件名
    import_file_name = import_file_path.split("/")[-1]
    # 核实导入文件的格式是否正确
    format, content = check_format(import_file_path, format_list)
    Load_Format.set(format)
    if format == "Error":
        ISLOAD.set("导入失败")
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "导入失败\n" "请检查文件格式是否正确。\n")
        #设置字体为红色
        Message_box.tag_add("tag1", "1.0", "end")
        Message_box.tag_config("tag1", foreground="red")#设置tag1的字体颜色为红色
        Message_box.config(state=tk.DISABLED)
    else:
        ISLOAD.set("导入成功")
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "已导入文件：\n" + import_file_name + "\n")
        Message_box.config(state=tk.DISABLED)
        # 将内容储存删除
        chat_history.clear()
        for i in range(len(content)):
            chat_history.append(content[i])

#==================================================================================================#
#按钮标签
ISLOAD = tk.StringVar()
#记录导入状态
ISLOAD.set("未导入")
#记录导入格式
Load_Format = tk.StringVar()
# 创建一个按钮，点击之后弹出一个窗口，选择文件
import_button = tk.Button(window,textvariable=ISLOAD,command=lambda: on_import_select(None),highlightthickness=2,highlightcolor="#1E1E1E")
import_button.config(background=cbox_colors[6], foreground=cbox_colors[7])
# 按钮样式
import_button.config(width=import_button_size[0], height=import_button_size[1])
import_button.config(font=cbox_font)

import_label = tk.Label(window, text="导入文件：")
import_label.config(font=cbox_font)


if __name__ == "__main__":
    import_label.grid(row=0, column=0, sticky=tk.N)
    import_button.grid(row=0, column=1, sticky=tk.N)
    window.mainloop()
