# 执行显示菜单,不能删除
from Menu_file import *
from Menu_clear import *
from UI import * # 模式
from Menu_setting import *
# -----------------------------------------------------------------------------------#

# 打开文件
try:
    with open(API_file[0], "r", encoding="utf-8") as f:
        # 读取第一行内容
        API_KEY = f.readline().strip("\n")
    # 登录
    openai.api_key = API_KEY
    Message_box.config(state=tk.NORMAL)
    Message_box.delete(0.0, tk.END)
    Message_box.insert(tk.END, "已登陆\n")
    Message_box.config(state=tk.DISABLED)
except:
    Message_box.insert(tk.END, "未登录\n")
# -----------------------------------------------------------------------------------#
# 静止调整窗口大小
if __name__ == "__main__":
    window.resizable(0, 0)
    window.mainloop()
