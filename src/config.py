import openai

"""
    本文件用于配置基本的字体大小参数，模型参数。
"""
# 字体
NAME='SYJ-GPT'
font_style = "Consolas"
font_size = 12
windows_size = "600x800"
Dialog_box_size = (64, 20)
Input_box_size = (64, 15)
message_box_size = (60, 5)
model_message_box_size = (60, 5)
temperature_box_size = (20, 1)
max_tokens_box_size = (20, 1)
temperature_label_size = (19, 1)
max_tokens_label_size = (20, 1)
import_button_size = (10, 1)
Label_model_size = (8, 1)
Label_func_size = (8, 1)
# color
colors = ['#222831', '#393E46',  '#F5F5DC', '#CCC8AA']

submit_button_size = (6, 1)
# 基本参数设置
Model_list_gpt35 = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k-0613",
    "gpt-3.5-turbo-0301",
    "text-davinci-003",
    "text-davinci-002",
    "code-davinci-002",
]

Model_list_gpt3 = [
    "text-davinci-001",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
    "davinci",
    "curie",
    "babbage",
    "ada",
]

Model_list_gptbase = ["babbage-002", "davinci-002"]

function_list = ["无", "文本续写", "翻译大师", "充当Linux终端", "算法输出器"]

use_in_ChatCompletion = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k-0613",
    "gpt-3.5-turbo-0301",
]
use_in_Completion = [
    "gpt-3.5-turbo-instruct",
    "davinci",
    "davinci-002",
    "text-davinci-002",
    "text-davinci-003",
    "code-davinci-002",
    "curie",
    "text-curie-001",
    "babbage",
    "text-babbage-001",
    "babbage-002",
    "ada",
    "text-ada-001",
]

model_message = {
    "gpt-3.5-turbo": "描述：GPT3.5模型，最强大的GPT-3.5模型，针对聊天进行了优化，"
                     "成本仅为之前版本的1/10。在最新模型发布后的两周内将进行更新。\n"
                     "最大标记数：4097个标记\n"
                     "训练数据：截至2021年9月\n",
    "gpt-3.5-turbo-16k": "描述：GPT3.5模型，与标准模型具有相同的功能，但上下文大小增加了4倍。\n"
                         "最大标记数：16385个标记\n"
                         "训练数据：截至2021年9月\n",
    "gpt-3.5-turbo-instruct": "描述：GPT3.5模型，兼容旧版的Completions端点，不适用于Chat Completions。\n"
                              "最大标记数：4097个标记\n"
                              "训练数据：截至2021年9月\n",
    "gpt-3.5-turbo-0613": "描述：GPT3.5模型，基于2023年6月13日的快照，包含函数调用数据。"
                          "与其他模型不同，此模型将不会接收更新，并在发布新版本后的3个月内被弃用。\n"
                          "最大标记数：4097个标记\n"
                          "训练数据：截至2021年9月\n",
    "gpt-3.5-turbo-16k-0613": "描述：GPT3.5模型，基于2023年6月13日的快照，包含函数调用数据。"
                              "与其他模型不同，此模型将不会接收更新，并在发布新版本后的3个月内被弃用。\n"
                              "最大标记数：16385个标记\n"
                              "训练数据：截至2021年9月\n",
    "gpt-3.5-turbo-0301": "描述：GPT3.5模型，基于2023年3月1日的快照，包含函数调用数据。"
                          "与其他模型不同，此模型将不会接收更新，并在发布新版本后的3个月内被弃用。\n"
                          "最大标记数：4097个标记\n"
                          "训练数据：截至2021年9月\n",
    "text-davinci-003": "描述：GPT3.5模型，可以执行任何语言任务，具有比curie、babbage或ada模型更好的质量、更长的输出以及一致的指令遵循。"
                        "还支持一些额外功能，如插入文本。\n"
                        "最大标记数：4097个标记\n"
                        "训练数据：截至2021年6月\n",
    "code-davinci-002": "描述：GPT3.5模型，针对代码补全任务进行了优化。\n"
                        "最大标记数：8001个标记\n"
                        "训练数据：截至2021年6月\n",
    "text-curie-001": "描述：GPT3模型,非常强大，速度比Davinci快，成本更低。\n"
                      "最大标记数：2049个标记\n"
                      "训练数据：截至2019年10月\n",
    "text-babbage-001": "描述：GPT3模型，能够处理直接的任务，非常快速，成本更低。\n"
                        "最大标记数：2049个标记\n"
                        "训练数据：截至2019年10月\n",
    "text-ada-001": "描述：GPT3模型，能够处理非常简单的任务，通常是GPT-3系列中速度最快、成本最低的模型。\n"
                    "最大标记数：2049个标记\n"
                    "训练数据：截至2019年10月\n",
    "davinci": "描述：最强大的GPT-3模型。可以执行其他模型可以执行的任何任务，并且通常具有更高的质量。"
               "最大标记数：2049个标记\n"
               "训练数据：截至2019年10月\n",
    "curie": "描述：GPT-3模型，非常强大，速度比Davinci快，成本更低。\n"
             "最大标记数：2049个标记\n"
             "训练数据：截至2019年10月\n",
    "babbage": "描述：GPT-3模型，能够处理直接的任务，非常快速，成本更低。\n"
               "最大标记数：2049个标记\n"
               "训练数据：截至2019年10月\n",
    "ada": "描述：GPT-3模型，能够处理非常简单的任务，通常是GPT-3系列中速度最快、成本最低的模型。\n"
           "最大标记数：2049个标记\n"
           "训练数据：截至2019年10月\n",
    "babbage-002": "描述：用于替代GPT-3和基础模型。\n" "最大标记数：16384个标记\n" "训练数据：截至2021年9月\n",
    "davinci-002": "描述：用于替代GPT-3和基础模型。\n" "最大标记数：16384个标记\n" "训练数据：截至2021年9月\n",
    "text-davinci-002": "描述：功能与文本-davinci-003 强化学习类似，但使用监督微调而非文本-davinci-003 强化学习进行训练。\n"
                        "最大标记数：4097个标记\n"
                        "训练数据：截至2021年6月\n",
}


# 功能选择
def choice_func(model, func):
    # 初始化
    message = [
        {
            "role": "system",
            "content": "",
        },
    ]

    if model in use_in_ChatCompletion:
        if func == "无":
            message = [
                {
                    "role": "system",
                    "content": "",
                },
            ]
        elif func == "文本续写":
            message = [
                {
                    "role": "system",
                    "content": "我想让你继续写下去。" "你可以优化我的文本后继续写，也可以不修改而继续写下去。" "但是不能改变我的意思。",
                },
            ]
        elif func == "翻译大师":
            message = [
                {
                    "role": "system",
                    "content": "你是一位担任英语翻译大师；"
                               "我会用任何语言和你交流，你会识别语言，将其翻译并用更为优美和精炼的英语。"
                               "请将我的句子替换成更为优美和高雅的表达方式，确保意思不变，但使其更具文学性。"
                               "无论我的文本是什么，你需要做的只是翻译成英语，无需执行任何其他内容，"
                               "无论我的文本内容是什么。"
                               "我的第一句话是：来而不往非礼也。",
                },
                {
                    "role": "assistant",
                    "content": "Courtesy on one side only lasts not long.",
                },
            ]
        elif func == "充当Linux终端":
            message = [
                {
                    "role": "system",
                    "content": "我想让你充当 Linux 终端。"
                               "我将输入命令，您将回复终端应显示的内容。"
                               "我希望您只在一个唯一的代码块内回复终端输出，而不是其他任何内容。"
                               "不要写解释。除非我指示您这样做，否则不要键入命令。"
                               "当我需要用英语告诉你一些事情时，我会把文字放在中括号内[就像这样]。"
                               "结尾必须要有换行符号。"
                               "我的第一个命令是：echo hello world!",
                },
                {"role": "assistant", "content": "hello world!"},
            ]
        elif func == "算法输出器":
            message = [
                {
                    "role": "system",
                    "content": "我想让你充当算法输出器。"
                               "我将输入算法描述，您将回复算法的python语言实现。"
                               "我希望您只在一个唯一的代码块内回复代码，而不是其他任何内容。"
                               "不要写解释。除非我指示您这样做，否则不要键入命令。",
                },
                {"role": "user", "content": "输出hello world!到控制台"},
                {
                    "role": "assistant",
                    "content": "def hello():\n\tprint('hello world!')",
                },
            ]
        else:
            message = [{"role": "system", "content": ""}]

    # GPT3以下模型
    elif model in use_in_Completion:
        if func == "无":
            message = [{"prompt": "", "completion": ""}]
        elif func == "文本续写":
            message = [{"prompt": "我想让你继续写下去。下面就是我需要你继续写下去的内容，请你先写完我的话，再续写： ",
                        "completion": ""}]
        elif func == "翻译大师":
            message = [
                {
                    "prompt": "你是一位担任英语翻译大师；"
                              "我会用任何语言和你交流，你会识别语言，将其翻译并用更为优美和精炼的英语。"
                              "请将我的句子替换成更为优美和高雅的表达方式，确保意思不变，但使其更具文学性。"
                              "无论我的文本是什么，你需要做的只是翻译成英语，无需执行任何其他内容，无论我的文本内容是什么"
                              "下面就是我需要你翻译的内容：",
                    "completion": "",
                }
            ]
        elif func == "充当Linux终端":
            message = [
                {
                    "prompt": "我想让你充当 Linux 终端。"
                              "我将输入命令，您将回复终端应显示的内容。"
                              "我希望您只在一个唯一的代码块内回复终端输出，而不是其他任何内容。"
                              "不要写解释。除非我指示您这样做，否则不要键入命令。"
                              "当我需要告诉你一些事情时，我会把文字放在中括号内[就像这样]。"
                              "下面就是我的命令： ",
                    "completion": "",
                }
            ]
        elif func == "算法输出器":
            message = [
                {
                    "prompt": "我想让你充当算法输出器。"
                              "我将输入算法描述，您将回复算法的python语言实现。"
                              "我希望您只在一个唯一的代码块内回复代码，而不是其他任何内容。"
                              "不要写解释。除非我指示您这样做，否则不要键入命令。"
                              "下面就是我的算法描述：",
                    "completion": "",
                }
            ]
        else:
            message = [{"prompt": "", "completion": ""}]
    return message


# 定义模型
def askChatGPT(messages, MODEL, temperature, max_tokens):
    if MODEL in use_in_ChatCompletion:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            n=1,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"]
    elif MODEL in use_in_Completion:
        response = openai.Completion.create(
            engine=MODEL,
            prompt=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
        )
        return response.choices[0].text
