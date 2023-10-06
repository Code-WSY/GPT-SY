import json

import openai

"""
    本文件用于配置基本的字体大小参数，模型参数。以及全局变量。
"""
# 提示库
prompts = {}
# 模型信息
model_message = {}
# 模型适用格式(函数)
model_use_mode = {}
# 模式列表
mode_dict=set() #{模式：适用模式的model列表}
mode_prompt_dict=set() #{模式：适用模式的prompt列表}
chat_history=set() #聊天记录
# -----------------------------------------------------------------------------------#
save_path_init = "../ChatLogs/"
# -----------------------------------------------------------------------------------#
with open("../data/Model.json", "r", encoding="utf-8") as f:
    model_json = json.load(f)
# -----------------------------------------------------------------------------------#
# 从模型列表中获取模式列表
for i in model_json:
    #key:模式，value:适用模式的model列表
    mode_dict.add(i["use_in"])
    #key:模式，value:适用模式的prompt列表
    mode_prompt_dict.add(i["use_in"])
    #key:模式，value:适用模式聊天记录
    chat_history.add(i["use_in"])
# -----------------------------------------------------------------------------------#
mode_dict={i:[] for i in mode_dict}
mode_prompt_dict={i:[] for i in mode_prompt_dict}
chat_history={i:[] for i in chat_history}
# -----------------------------------------------------------------------------------#
for i in model_json:
    mode_dict[i["use_in"]].append(i["model"])
# -----------------------------------------------------------------------------------#
# 模型信息
for i in model_json:
    model_message[i["model"]] = i["description"]
    model_use_mode[i["model"]] = i["use_in"]
# -----------------------------------------------------------------------------------#
# 提示库用于ChatCompletion模式和Completion模式
with open("../data/prompts.json", "r", encoding="utf-8") as f:
    prompts_load = json.load(f)
for i in prompts_load:
    prompts[i["act"]] = i["prompt"]
    mode_prompt_dict["ChatCompletion"].append(i["act"])
    mode_prompt_dict["Completion"].append(i["act"])
#其余模式不适用prompt，都加一个“”进去
for i in mode_prompt_dict:
    if i not in ["ChatCompletion","Completion"]:
        mode_prompt_dict[i].append("")
# -----------------------------------------------------------------------------------#
# 保存路径
save_file_path=[save_path_init, ]
#-----------------------------------------------------------------------------------#
# 字体
NAME = "GPT-SY"
font_style = "Consolas"
font_size = 11
# windows_size = "600x800"
# 设置窗口大小
window_height = 50
window_width = 70
# 1
Dialog_box_size = (window_width, int(window_height * 0.5))
# 2
message_box_size = (window_width, int(window_height * 0.15))
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
# 分别表示：
# 对话框背景颜色，对话框字体颜色，
# 消息框背景颜色，消息框字体颜色，
# 输入框背景颜色，输入框字体颜色，
# 提交按钮背景颜色，提交按钮字体颜色
colors = ["#192A56","#FFFFFF",
          "#E1F5FE", "#424242",
          "#1E2127","#FFFFFF",
          "#F1ECE9","#4E342E"]

# 下拉框颜色:
# 模型标签背景颜色，模型标签字体颜色，模型下拉框背景颜色，模型下拉框字体颜色，
# 功能标签背景颜色，功能标签字体颜色，功能下拉框背景颜色，功能下拉框字体颜色
cbox_colors=["#F1ECE9","#424242","#F1ECE9","#424242","#F1ECE9","#424242","#F1ECE9","#424242"]
cbox_font=(font_style,font_size+2)

#输入框颜色:
# 温度的标签背景颜色，温度标签字体颜色，
# 温度输入框背景颜色，温度输入框字体颜色，
# 最大长度的标签背景颜色，最大长度标签字体颜色，
# 最大长度输入框背景颜色，最大长度输入框字体颜色
#背景：米色 (#F1ECE9),字体：深灰色 #424242
entry_font=(font_style,font_size+2)
entry_colors=["#F1ECE9","#424242","#F1ECE9","#424242","#F1ECE9","#424242","#F1ECE9","#424242"]
