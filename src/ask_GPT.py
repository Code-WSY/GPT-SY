import openai
from Box_Dialog import *

def askGPT(messages, MODEL, MODEL_fomat, temperature, max_tokens):
    """
    :param messages: 历史记录
    :param MODEL: 应用的模型
    :param MODEL_fomat: 模型使用的输入格式
    :param temperature: 温度
    :param max_tokens: 最大输出长度
    :return:
    """
    output = ""
    Dialog_box.config(state=tk.NORMAL)
    Dialog_box.insert(tk.END, "AI：\n")
    Dialog_box.config(state=tk.DISABLED)

    if MODEL_fomat == "ChatCompletion":
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            n=1,
            max_tokens=max_tokens,
            stream=True,

        )
        for chunk in response:
            try:
                #正常输出
                answer = chunk["choices"][0]["delta"]["content"]
                output += answer
                Dialog_box.config(state=tk.NORMAL)
                Dialog_box.insert(tk.END, answer)
                Dialog_box.see(tk.END)
                Dialog_box.update()
                Dialog_box.config(state=tk.DISABLED)
            except:
                #输出最后
                Dialog_box.config(state=tk.NORMAL)
                Dialog_box.insert(tk.END, "\n")
                Dialog_box.see(tk.END)
                Dialog_box.update()
                Dialog_box.config(state=tk.DISABLED)
                pass


    elif MODEL_fomat == "Completion":

        response = openai.Completion.create(
            engine=MODEL,
            prompt=messages[-1]["prompt"],
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stream=True,

        )
        #输出对话
        for chunk in response:
            Dialog_box.config(state=tk.NORMAL)
            answer = chunk["choices"][0]["text"]
            output += answer
            Dialog_box.insert(tk.END, answer)
            Dialog_box.see(tk.END)
            Dialog_box.update()
            Dialog_box.config(state=tk.DISABLED)

        #输出最后一个换行符
        Dialog_box.config(state=tk.NORMAL)
        Dialog_box.insert(tk.END, "\n")
        Dialog_box.see(tk.END)
        Dialog_box.config(state=tk.DISABLED)
    return output


if __name__ == "main":
    pass
