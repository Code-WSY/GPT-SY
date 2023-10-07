import openai # 导入openai模块
openai.api_key = "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" # 设置openai的API密钥
model_list=openai.Model.list() # 获取openai的模型列表
engine_list=openai.Engine.list() # 获取openai的函数列表
# -----------------------------------------------------------------------------------#
"""
print("模型列表：")
for i in model_list["data"]:
    print(i["object"],i["id"],)
# ------------------------------------
"""
# -----------------------------------------------#
for i in engine_list["data"]:
    print(i["object"]+": "+i["id"],)
for j in engine_list["data"]:
    print(j)