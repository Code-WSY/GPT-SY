from UI import *
# -----------------------------------------------------------------------------------#
filename = "../API_KEY/API_KEY"
# 打开文件
try:
    with open(filename, "r", encoding="utf-8") as f:
        # 读取第一行内容
        API_KEY = f.readline().strip("\n")
    # 登录
    openai.api_key = API_KEY
    model_message_box.config(state=tk.NORMAL)
    model_message_box.delete(0.0, tk.END)
    model_message_box.insert(tk.END, "已登陆\n")
    model_message_box.config(state=tk.DISABLED)
except:
    model_message_box.insert(tk.END, "未登录\n")
# -----------------------------------------------------------------------------------#
# 静止调整窗口大小
if __name__ == "__main__":
    window.resizable(0, 0)
    window.mainloop()
