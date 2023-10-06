from tkinter.ttk import Combobox
from windows import *
import openai
import os
from Box_Message import Message_box
login_file_path = "../API_KEY/API_KEY"
def Latest_API_KEY():
    # 读取../API_KEY/API_KEY
    try:
        with open(login_file_path, "r", encoding="utf-8") as f:
            api_key = f.read()
    except:
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "API_KEY文件不存在\n")
        Message_box.config(state=tk.DISABLED)
        return
    # 读取最后一行数据（字典）
    api_key = api_key.split("\n")[-2]
    # 转换为字典
    api = eval(api_key)
    # 读取
    openai.api_key = api["API_KEY"]
    openai.api_base = api["API_BASE"]
    # 显示
    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "已登陆\n")
    Message_box.config(state=tk.DISABLED)


def Reset_API_KEY():
    def login_api():
        key = api_key_entry.get()
        base = api_base_entry.get()
        note = api_name_entry.get()
        with open(login_file_path, "a", encoding="utf-8") as f:
            f.write("\n")
            f.write(str({"API_KEY": key, "API_BASE": base, "API_NAME": note}))
        # 读取
        openai.api_key = key
        openai.api_base = base
        # 关闭
        login.destroy()
        # 显示
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "已登陆\n")
        Message_box.config(state=tk.DISABLED)

    login = tk.Tk()
    login.title("Login")
    api_key_label = tk.Label(login, text="API_KEY:")
    api_key_entry = tk.Entry(login)
    api_base_label = tk.Label(login, text="API_BASE:")
    api_base_entry = tk.Entry(login)
    api_name_label = tk.Label(login, text="API_NOTE:")
    api_name_entry = tk.Entry(login)

    login_button = tk.Button(login, text="Login", command=lambda: login_api())

    api_key_label.pack()
    api_key_entry.pack()
    api_base_label.pack()
    api_base_entry.pack()
    api_name_label.pack()
    api_name_entry.pack()
    login_button.pack()


def choose_API_KEY():
    # 读取../API_KEY/API_KEY
    try:
        with open(login_file_path, "r", encoding="utf-8") as f:
            api_key = f.read()
    except:
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "API_KEY文件不存在\n")
        Message_box.config(state=tk.DISABLED)
        return
    # 读取每行数据中的API_NAME
    api_name = []
    api_key_list = []
    api_base_list = []
    for i in api_key.split("\n"):
        if i != "":
            api_name.append(eval(i)["API_NAME"])
            api_key_list.append(eval(i)["API_KEY"])
            api_base_list.append(eval(i)["API_BASE"])
    # 弹出选择窗口
    choosekey = tk.Tk()
    choosekey.title("Choose API_KEY")
    api_name_var = tk.StringVar()
    api_name_var.set(api_name[0])
    # 下拉框
    api_name_option = Combobox(
        choosekey, values=api_name
        , textvariable=api_name_var, state="readonly", background=colors[2], foreground=colors[3],
    )
    api_name_option.pack()

    # 确认按钮
    def confirm():
        # 读取
        openai.api_key = api_key_list[api_name.index(api_name_var.get())]
        openai.api_base = api_base_list[api_name.index(api_name_var.get())]
        # 关闭
        choosekey.destroy()
        # 显示
        Message_box.config(state=tk.NORMAL)
        Message_box.delete(0.0, tk.END)
        Message_box.insert(tk.END, "已登陆\n")
        Message_box.config(state=tk.DISABLED)
    confirm_button = tk.Button(choosekey, text="确定", command=lambda: confirm())
    confirm_button.pack()


# -----------------------------------------------------------------------------------#

# 创建一个菜单
filemenu_login = tk.Menu(menubar, tearoff=0)
# 设置单选
filemenu_login.add_command(label="Latest API_KEY", command=lambda: Latest_API_KEY())
filemenu_login.add_command(label="Reset API_KEY", command=lambda: Reset_API_KEY())
filemenu_login.add_command(label="Choose API_KEY", command=lambda: choose_API_KEY())
# -----------------------------------------------------------------------------------#
if os.path.exists(login_file_path):
    with open(login_file_path, "r", encoding="utf-8") as f:
        api_key = f.read()
    api_key = api_key.split("\n")[-1]
    # 转换为字典
    api = eval(api_key)
    # 读取
    openai.api_key = api["API_KEY"]
    openai.api_base = api["API_BASE"]
    # 显示
    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "已登陆\n")
    Message_box.config(state=tk.DISABLED)
