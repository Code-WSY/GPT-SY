import openai
import json

"""
    本文件用于配置基本的字体大小参数，模型参数。
"""
# 字体
NAME = 'GPT-SY'
font_style = "Consolas"
font_size = 12
# windows_size = "600x800"
#设置窗口大小
window_height = 30
window_width = 70
#1
Dialog_box_size = (window_width, int(window_height * 0.4))
#2
message_box_size = (window_width, int(window_height * 0.2))
#3
temperature_label_size = (int(window_width * 0.25), 1)
temperature_box_size = (int(window_width * 0.25), 1)
max_tokens_label_size = (int(window_width * 0.25), 1)
max_tokens_box_size = (int(window_width * 0.25), 1)
#4
Label_model_size = (int(window_width * 0.25), 1)
Label_func_size = (int(window_width * 0.25), 1)
ComboBox_model_size= (int(window_width * 0.25), 1)
ComboBox_func_size= (int(window_width * 0.25), 1)

import_button_size = (int(window_width * 0.25), 1)
#5
Input_box_size = (window_width, int(window_height * 0.3))
#6
submit_button_size = (int(window_width * 0.5), 1)
# 界面颜色
colors = ['#222831', '#393E46', '#F5F5DC', '#CCC8AA']

# 模型信息
# 导入../data/model.json
model_message = {}
model_use = {}

with open("../data/Model.json", "r", encoding="utf-8") as f:
    model_json = json.load(f)
for i in model_json:
    model_message[i['model']] = i['description']
    model_use[i['model']] = i['use_in']

# 提示信息
# 导入../data/prompts.json
prompts = {}

with open("../data/prompts.json", "r", encoding="utf-8") as f:
    prompts_load = json.load(f)
for i in prompts_load:
    prompts[i['act']] = i['prompt']


# 功能选择
def choice_func(model, func):
    message = []
    # ChatCompletion
    if model_use[model] == 'ChatCompletion':
        message = [{"role": "system", "content": prompts[func]}]
    # Completion
    elif model_use[model] == 'Completion':
        message = [{"prompt": prompts[func] + '我的第一个任务是：', "completion": ""}]
    return message


# 定义模型
def askGPT(messages, MODEL, temperature, max_tokens):
    if model_use[MODEL] == 'ChatCompletion':
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            n=1,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"]
    elif model_use[MODEL] == 'Completion':
        response = openai.Completion.create(
            engine=MODEL,
            prompt=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
        )
        return response.choices[0].text
