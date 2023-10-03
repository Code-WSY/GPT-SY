from Box_Dialog import *
from Box_Input import *
from Cbox_Prompt import *
from Menu_mode import *

from Cbox_Model import *
from Button_Load import *


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
    Dialog_box.insert(tk.END, "User：\n" + text + "\n")
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
    if selected_mode.get() == "Fine-tuning" and LOAD_BOOL.get() == True:
        load_messages = eval(Load_Content.get())
        if model_use[model_list.get()] == "ChatCompletion":
            for message in load_messages:
                messages.append(message)
            # 提问提交到message,并交给GPT回答
            messages.append({"role": "user", "content": text})
            answer = askGPT(
                messages=messages,
                MODEL=selected_model.get(),
                temperature=temperature,
                max_tokens=max_token,
            )
            # 将回答提交到对话框,并滚动到最后一行,并提交到message
            Dialog_box.insert(tk.END, "AI：\n" + answer + "\n\n")
            Dialog_box.see(tk.END)
            messages.append({"role": "assistant", "content": answer})

        elif model_use[model_list.get()] == "Completion":
            # 报错显示
            model_message_box.config(state=tk.NORMAL)
            model_message_box.delete("1.0", "end")
            model_message_box.insert(tk.END, "该模型不支持Fine-tuning")
            model_message_box.config(state=tk.DISABLED)
            Dialog_box.see(tk.END)

    elif selected_mode.get() == "Fine-tuning" and not LOAD_BOOL.get():
        # 报错显示
        model_message_box.config(state=tk.NORMAL)
        model_message_box.delete("1.0", "end")
        model_message_box.insert(tk.END, "请先导入对话")
        model_message_box.config(state=tk.DISABLED)

    # -----------------------------------------------------------------------------------#
    # ----------------------------------普通模式------------------------------------------#
    elif selected_mode.get() == "Prompt-based":
        if model_use[model_list.get()] == "ChatCompletion":
            #print(messages)  # 对话历史
            #print(prompts[func_list.get()])  # 选择的功能
            # 首次提交
            if len(messages) == 0:
                messages.append(choice_func(model_list.get(), func_list.get())[0])
            # 中途切换功能：清空对话列表
            # messages[0]["role"] == "system" : 保证是系统消息
            # messages[0]["content"] != prompts[func_list.get()]: 保证不是当前功能
            elif (
                messages[0]["role"] == "system"
                and messages[0]["content"] != prompts[func_list.get()]
            ):
                messages = [choice_func(model_list.get(), func_list.get())[0]]
                model_message_box.config(state=tk.NORMAL)
                model_message_box.delete("1.0", "end")
                model_message_box.insert(
                    tk.END, "已切换功能\n" "当前功能：" + func_list.get() + "\n" "历史对话已清空\n"
                )
                #tk.END:插入到最后一行
                model_message_box.config(state=tk.DISABLED)


            # 提问提交到message,并交给GPT回答
            messages.append({"role": "user", "content": text})
            answer = askGPT(
                messages=messages,
                MODEL=selected_model.get(),
                temperature=temperature,
                max_tokens=max_token,
            )
            # 将回答提交到对话框,并滚动到最后一行,并提交到message
            Dialog_box.insert(tk.END, "AI：\n" + answer + "\n\n")
            Dialog_box.see(tk.END)
            messages.append({"role": "assistant", "content": answer})

        elif model_use[model_list.get()] == "Completion":
            """
            由于是单轮对话，所以每次提交都会建立一个prompt，然后交给GPT回答
            """
            # system_message
            messages.append(choice_func(model_list.get(), func_list.get())[0])
            messages[-1]["prompt"] += text
            answer = askGPT(
                messages=messages[-1]["prompt"],
                MODEL=selected_model.get(),
                temperature=temperature,
                max_tokens=max_token,
            )
            messages[-1]["completion"] = answer
            Dialog_box.insert(tk.END, "AI：\n" + answer + "\n\n")
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

submit_button = tk.Button(
    window,
    text="提交",
    width=submit_button_size[0],
    height=submit_button_size[1],
    command=lambda: sumbit_text(None),
)
# 按钮的字体
submit_button.config(
    font=(font_style, font_size),
    background=colors[3],
    activebackground=colors[3],
    foreground=colors[0],
)
if __name__ == "__main__":
    submit_button.grid(row=1, column=0, sticky=tk.NSEW)
    window.mainloop()
