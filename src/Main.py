# 执行显示菜单,不能删除
from Menu_file import *
from Menu_clear import *
from UI import * #
from Menu_setting import *
# -----------------------------------------------------------------------------------#

# 打开文件
try:
    # 登录
    openai.api_key_path = "../API_KEY/API_KEY_OPENAI"
    openai.api_base = "https://api.openai.com/v1"
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
