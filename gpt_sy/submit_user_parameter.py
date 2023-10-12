from Box_Input import *
from Box_Dialog import *
from Cbox_Prompt import *
from Cbox_Model import *
def submit_user_parameter():
    # 将用户输入的文本提交到对话框
    user_content = Input_box.get("1.0", "end")
    Input_box.delete("1.0", "end")
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.insert(tk.END, "\nUser：\n" + user_content + "\n")
    Dialog_box.config(state=tk.DISABLED)
    Dialog_box.see(tk.END)
    Dialog_box.update()
    # 获取用户输入的参数
    try:
        temperature = float(temperature_box.get())
    except:
        # 如果用户没有输入温度，就默认为0.6
        temperature = 0.6
    try:
        max_token = int(max_tokens_box.get())
    except:
        # 如果用户没有输入最大标记数，就默认为50
        max_token = 50
    return user_content, temperature, max_token, \
        selected_model.get(), selected_prompt_title.get(),selected_mode.get()