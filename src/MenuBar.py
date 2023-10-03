import tkinter as tk
from windows import window, menubar
from MenuBar_function import open_file, save_file
from UI import chat_UI, foget_all, load_UI
"""
设计：
    菜单栏：
        文件：
            -打开
            -保存
            -退出
        模式：
            -Prompt-based
            -Fine-tuning
        登录：(已删除)
            -API_KEY
        清空：
            -清空历史记录
    设计每一个菜单项的功能函数：
        -打开：open_file()
        -保存：save_file()
        -退出：window.quit()
        -Prompt-based：chat_UI()
        -Fine-tuning：load_UI()
        -API_KEY：login()
输出：
    1.selected_mode：模式选择（外部获取：selected_mode.get()）
"""
# -----------------------------------------------------------------------------------#
# 创建菜单项3个
filemenu_file = tk.Menu(menubar, tearoff=0)
filemenu_mode = tk.Menu(menubar, tearoff=0)
filemenu_login = tk.Menu(menubar, tearoff=0)
filemenu_clear = tk.Menu(menubar, tearoff=0)
# 菜单1
menubar.add_cascade(label="文件", menu=filemenu_file)
filemenu_file.add_command(label="打开", command=lambda: open_file())
filemenu_file.add_command(label="保存", command=lambda: save_file())
filemenu_file.add_separator()
filemenu_file.add_command(label="退出", command=lambda: window.quit())


# 菜单2
menubar.add_cascade(label="模式", menu=filemenu_mode)
selected_mode = tk.StringVar()
# 当用户选中某个模式时，会将value的值赋值给variable,而tk.StringVar()是一种特殊的变量。
# 通过检查selected_mode.get()的值，就可以知道用户选中了哪个模式。
filemenu_mode.add_radiobutton(label="Prompt-based", variable=selected_mode, value="Prompt-based")
filemenu_mode.add_radiobutton(label="Fine-tuning", variable=selected_mode, value="Fine-tuning")
selected_mode.set("Prompt-based")

def change_UI():
    if selected_mode.get() == "Prompt-based":
        foget_all()
        chat_UI()
    elif selected_mode.get() == "Fine-tuning":
        foget_all()
        load_UI()


selected_mode.trace("w", lambda *args: change_UI())


# 菜单3
#menubar.add_cascade(label="登录", menu=filemenu_login)
#filemenu_login.add_command(label="API_KEY", command=lambda: login())

# 菜单4
def clear_display():
    from Box_Dialog import Dialog_box
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.delete(0.0, tk.END)
    Dialog_box.config(state=tk.DISABLED)
menubar.add_cascade(label="清空", menu=filemenu_clear)
def clear_messages_list():
    from Bottom_Submit import messages_list
    from Box_Message import model_message_box
    messages_list.set("[]")
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete(0.0, tk.END)
    model_message_box.insert("insert", "成功清空对话记录")
    model_message_box.config(state=tk.DISABLED)
filemenu_clear.add_command(label="清屏", command=lambda: clear_display())
filemenu_clear.add_command(label="清空对话记录", command=lambda: clear_messages_list())


if __name__ == "__main__":
    window.mainloop()