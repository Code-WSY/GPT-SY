import tkinter as tk
from windows import window
from config import use_in_ChatCompletion, use_in_Completion, choice_func, \
    askChatGPT,submit_button_size,font_style,font_size,colors
from Box_Input import Input_box, temperature_box, max_tokens_box
from Box_Dialog import Dialog_box
from Cbox_Model import model_list, selected_model
from Cbox_Promot import func_list
from Button_Load import Load_Content, Model_select, LOAD_BOOL
from Box_Message import model_message_box

"""
设计：
    1. 提交按钮
    2. 提交按钮的功能
输出：
    1. 提交按钮
    2.message_list:记录的对话历史的列表；将导入的对话也存储在这里
        可保存（外部获取：messages_list.get()）
"""
def sumbit_text(event):
    # 获取用户输入的文本
    text = Input_box.get("1.0", "end")
    Input_box.delete("1.0", "end")
    # 将用户输入的文本提交到对话框
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.insert("insert", "User：\n" + text + "\n")
    Dialog_box.see(tk.END)
    try:
        temperature = float(temperature_box.get())
    except:
        # 如果用户没有输入温度，就默认为0.9
        temperature = 0.6
    try:
        max_token = int(max_tokens_box.get())
    except:
        # 如果用户没有输入最大标记数，就默认为50
        max_token = 50

    # 历史对话列表
    messages = eval(messages_list.get())
    # -----------------------------------------------------------------------------------#
    # ----------------------------------导入模式------------------------------------------#
    if Model_select.get() == "导入模式" and LOAD_BOOL.get() == True:
        print("导入模式")
        load_messages = eval(Load_Content.get())
        if model_list.get() in use_in_ChatCompletion:
            for message in load_messages:
                messages.append(message)
            # 提问提交到message,并交给GPT回答
            messages.append({"role": "user", "content": text})
            answer = askChatGPT(
                messages=messages,
                MODEL=selected_model.get(),
                temperature=temperature,
                max_tokens=max_token,
            )
            # 将回答提交到对话框,并滚动到最后一行,并提交到message
            Dialog_box.insert("insert", "AI：\n" + answer + "\n\n")
            Dialog_box.see(tk.END)
            messages.append({"role": "assistant", "content": answer})

        elif model_list.get() in use_in_Completion:
            # 报错显示
            model_message_box.config(state=tk.NORMAL)
            model_message_box.delete("1.0", "end")
            model_message_box.insert("insert", "该模型不支持导入模式")
            model_message_box.config(state=tk.DISABLED)
            Dialog_box.see(tk.END)

    elif Model_select.get() == "导入模式" and LOAD_BOOL.get() == False:
        # 报错显示
        model_message_box.config(state=tk.NORMAL)
        model_message_box.delete("1.0", "end")
        model_message_box.insert("insert", "请先导入对话")
        model_message_box.config(state=tk.DISABLED)
        Dialog_box.see(tk.END)

    # -----------------------------------------------------------------------------------#
    # ----------------------------------普通模式------------------------------------------#
    elif Model_select.get() == "对话模式":
        if model_list.get() in use_in_ChatCompletion:
            # 首次提交
            if len(messages) == 0:
                messages.append(choice_func(model_list.get(), func_list.get())[0])
            # 中途切换功能：清空对话列表
            elif messages[0]["role"] == "system" and messages[0]["content"] != func_list.get():
                messages = [choice_func(model_list.get(), func_list.get())[0]]
                model_message_box.config(state=tk.NORMAL)
                model_message_box.delete("1.0", "end")
                model_message_box.insert("insert", "已切换功能\n"
                                                   "当前功能：" + func_list.get() + "\n"
                                         "历史对话已清空\n")
                model_message_box.config(state=tk.DISABLED)

            # 提问提交到message,并交给GPT回答
            messages.append({"role": "user", "content": text})
            answer = askChatGPT(
                messages=messages,
                MODEL=selected_model.get(),
                temperature=temperature,
                max_tokens=max_token,
            )
            # 将回答提交到对话框,并滚动到最后一行,并提交到message
            Dialog_box.insert("insert", "AI：\n" + answer + "\n\n")
            Dialog_box.see(tk.END)
            messages.append({"role": "assistant", "content": answer})

        elif model_list.get() in use_in_Completion:
            """
            由于是单轮对话，所以每次提交都会建立一个prompt，然后交给GPT回答
            """
            # system_message
            messages.append(choice_func(model_list.get(), func_list.get())[0])
            messages[-1]["prompt"] += text
            answer = askChatGPT(
                messages=messages[-1]["prompt"],
                MODEL=selected_model.get(),
                temperature=temperature,
                max_tokens=max_token,
            )
            messages[-1]["completion"] = answer
            Dialog_box.insert("insert", "AI：\n" + answer + "\n\n")
            Dialog_box.see(tk.END)
    # -----------------------------------------------------------------------------------#
    # 更新对话列表
    messages_list.set(str(messages))
    Dialog_box.config(state=tk.DISABLED)


# -----------------------------------------------------------------------------------#
# 对话列表，用于存储对话内容
messages_list = tk.StringVar()
messages_list.set("[]")
# 提交按钮

submit_button = tk.Button(window, text="提交",
                          width=submit_button_size[0], height=submit_button_size[1],
                          command=lambda: sumbit_text(None),
                          )
# 按钮的字体
submit_button.config(font=(font_style, font_size), background=colors[3],
                        activebackground=colors[3], foreground=colors[0],
                     )

if __name__ == "__main__":
    submit_button.grid(row=1, column=0, sticky=tk.NSEW)
    window.mainloop()