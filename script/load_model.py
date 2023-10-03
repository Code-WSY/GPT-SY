import json
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
# 基本参数设置
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
# 将集合中每一个字典的key和value转换为json中的key和value
# 例如：{"a":1,"b":2} -> {"key":"a","value":1},{"key":"b","value":2}
def dict_to_json(dict):
    json_list = []
    for key, value in dict.items():
        if key in use_in_ChatCompletion:
            json_list.append({"model": key, "description": value, "use_in": "ChatCompletion"})
        elif key in use_in_Completion:
            json_list.append({"model": key, "description": value, "use_in": "Completion"})
        else:
            json_list.append({"model": key, "description": value, "use_in": "None"})
    return json_list
json_list = dict_to_json(model_message)
#保存json文件
with open("../data/Model.json", "w", encoding="utf-8") as f:
    json.dump(json_list, f, ensure_ascii=False, indent=4)