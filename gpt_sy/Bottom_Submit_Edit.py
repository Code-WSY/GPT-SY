from tkinter.simpledialog import askstring
from scripts.add_chat import *
from submit_user_parameter import *
from ask_GPT import *
# 提交用户输入设置的参数


# 检查格式并发送
def check_and_sendGPT_Edit(text, temperature, max_token, selected_model, selected_prompt_title,
                      selected_mode
                      ):
        #弹出窗口

        instructions="输入要求"
        instruction=askstring("要求", instructions)

        add_chat(instruction, chat_history[selected_mode], selected_mode, "system")
        add_chat(text, chat_history[selected_mode], selected_mode, "user")
        # 交给GPT回答
        answer = askGPT(messages=chat_history[selected_mode], MODEL=selected_model, MODEL_use_mode=selected_mode,
                        temperature=temperature, max_tokens=max_token)
        # AI回答
        add_chat(answer, chat_history[selected_mode], model_use_mode[selected_model], "assistant")

def sumbit_text_Edit(event):
    # -------------------------------提交用户输入参数----------------------------------------#
    text, temperature, max_token, selected_model, selected_prompt,\
        selected_mode= submit_user_parameter()
    # -------------------------------------------------------------------------------------#
    # -------------------------------检查格式并发送------------------------------------------#
    check_and_sendGPT_Edit(text, temperature, max_token, selected_model, selected_prompt, selected_mode)

#-----------------------------------------------------------------------------------#
# 提交按钮
submit_button_Edit = tk.Button(window,
                          text="提交",
                          width=submit_button_size[0],
                          height=submit_button_size[1],
                          command=lambda: sumbit_text_Edit(None),
                          )
# 按钮的字体
submit_button_Edit.config(
    font=(font_style, font_size),
    background=colors[6],
    activebackground=colors[3],
    foreground=colors[7],
)
if __name__ == "__main__":
    submit_button_Edit.grid(row=1, column=0, sticky=tk.NSEW)
    window.mainloop()
