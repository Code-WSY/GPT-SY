import json
"""
    本文件用于配置基本的字体大小参数，模型参数。以及全局变量。
"""
# 所有可变类型变量为了保证全局引用，不要对其进行赋值操作，只能对其进行修改操作
chat_history = []
load_content = []
#print("ID_chat_history:", id(chat_history))
# 提示库
prompts = {}
# 模型信息
model_message = {}
# 模型适用格式(函数)
model_use_format = {}
# 可用模式的类型
mode_list = ["Prompt-based", "Fine-tuning"]
# 可用对话函数的类型
format_list = ["ChatCompletion", "Completion", "Error"]
# 每一个模式可用的对话函数
can_use_in_mode = {"Fine-tuning": ["ChatCompletion", ],
                   "Prompt-based": ["ChatCompletion", "Completion"]
                   }
GPT3_add_prompt="我的第一个任务是："
#-----------------------------------------------------------------------------------#
# 字体
NAME = "GPT-SY"
font_style = "Consolas"
font_size = 12
# windows_size = "600x800"
# 设置窗口大小
window_height = 50
window_width = 70
# 1
Dialog_box_size = (window_width, int(window_height * 0.4))
# 2
message_box_size = (window_width, int(window_height * 0.2))
# 3
temperature_label_size = (int(window_width * 0.25), 1)
temperature_box_size = (int(window_width * 0.25), 1)
max_tokens_label_size = (int(window_width * 0.25), 1)
max_tokens_box_size = (int(window_width * 0.25), 1)
# 4
Label_model_size = (int(window_width * 0.25), 1)
Label_func_size = (int(window_width * 0.25), 1)
ComboBox_model_size = (int(window_width * 0.25), 1)
ComboBox_func_size = (int(window_width * 0.25), 1)

import_button_size = (int(window_width * 0.25), 1)
# 5
Input_box_size = (window_width, int(window_height * 0.3))
# 6
submit_button_size = (int(window_width * 0.5), 1)
# 界面颜色
colors = ["#222831", "#393E46", "#F5F5DC", "#CCC8AA"]
# -----------------------------------------------------------------------------------#
with open("../data/prompts.json", "r", encoding="utf-8") as f:
    prompts_load = json.load(f)
for i in prompts_load:
    prompts[i["act"]] = i["prompt"]
with open("../data/Model.json", "r", encoding="utf-8") as f:
    model_json = json.load(f)
for i in model_json:
    model_message[i["model"]] = i["description"]
    model_use_format[i["model"]] = i["use_in"]
# -----------------------------------------------------------------------------------#
