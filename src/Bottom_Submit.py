from Box_Dialog import *
from Box_Input import *
from Cbox_Prompt import *
from Menu_mode import *
from Cbox_Model import *
from Button_Load import *
from scripts.add_chat import *
from scripts.check_format import *
from scripts.is_prompt_changed import *
from ask_GPT import *


# 提交用户输入设置的参数
def submit_user_parameter():
    # 将用户输入的文本提交到对话框
    user_content = Input_box.get("1.0", "end")
    Input_box.delete("1.0", "end")
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.insert(tk.END, "User：\n" + user_content + "\n")
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
        selected_model.get(), selected_prompt.get(),selected_mode.get()

# 检查格式并发送
def check_and_sendGPT(text, temperature, max_token, selected_model, selected_prompt,
                      selected_mode
                      ):
    # 检查对话记录格式
    chat_history_format, history = check_format(chat_history, format_list)
    # 检查对话记录与模型是否匹配
    if model_use_format[selected_model] == chat_history_format:
        #功能模式
        if selected_mode == mode_list[0]:
            # 检查期间是否更改了功能
            if is_prompt_changed(chat_history, chat_history_format, prompts[selected_prompt]):
                add_chat(prompts[selected_prompt], chat_history, chat_history_format, "system")
            # 添加用户输入
            if chat_history_format == format_list[0]:
                add_chat(text, chat_history, model_use_format[selected_model], "user")
            elif chat_history_format == format_list[1]:
                add_chat(GPT3_add_prompt + text, chat_history, model_use_format[selected_model], "user")
        #导入模式
        elif selected_mode == mode_list[1]:
            if chat_history_format == format_list[0]:
                #若从功能转导入，则为之前历史训练的延续，不需要添加prompt
                add_chat(text, chat_history, model_use_format[selected_model], "user")
            elif chat_history_format == format_list[1]:
                #若从功能转导入，则为无prompt的对话。
                add_chat("", chat_history,  model_use_format[selected_model], "system")
                add_chat(text, chat_history, model_use_format[selected_model], "user")

        # 交给GPT回答
        answer = askGPT(
            messages=chat_history,
            MODEL=selected_model,
            MODEL_fomat=chat_history_format,
            temperature=temperature,
            max_tokens=max_token,
        )
        # AI回答
        add_chat(answer, chat_history, model_use_format[selected_model], "assistant")
    else:
        # 报错显示格式有误
        Message_box.config(state=tk.NORMAL)
        Message_box.delete("1.0", "end")
        Message_box.insert(tk.END, "历史对话与模型不匹配")
        Message_box.config(state=tk.DISABLED)
        Dialog_box.see(tk.END)

def sumbit_text(event):
    # -------------------------------提交用户输入参数----------------------------------------#
    text, temperature, max_token, selected_model, selected_prompt,\
        selected_mode= submit_user_parameter()
    # -------------------------------------------------------------------------------------#
    # 如果对话记录为空，就初始化对话记录
    if chat_history == [] and selected_mode == mode_list[0]:
        # 如果对话记录为空，就添加用户输入
        add_chat(prompts[selected_prompt],
                 chat_history, model_use_format[selected_model], "system")

    check_and_sendGPT(text, temperature, max_token, selected_model, selected_prompt,selected_mode)

# 提交按钮
submit_button = tk.Button(window,
                          text="提交",
                          width=submit_button_size[0],
                          height=submit_button_size[1],
                          command=lambda: sumbit_text(None),
                          )

# 按钮的字体
submit_button.config(
    font=(font_style, font_size),
    background=colors[6],
    activebackground=colors[3],
    foreground=colors[7],
)

if __name__ == "__main__":
    submit_button.grid(row=1, column=0, sticky=tk.NSEW)
    window.mainloop()
