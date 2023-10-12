def add_chat(text, chat_history,  model_use_format, user):
    """
    :param text: 补充的文本
    :param chat_history: 历史记录
    :param model_use_format: 模型使用的输入格式
    :param user: 生成文本的用户
    :return:
    """
    if model_use_format == "ChatCompletion":
        """
        对于ChatCompletion情况，直接添加
        """
        res = {"role": user, "content": text}
        chat_history.append(res)

    elif model_use_format == "Completion":
        """
        对于Completion情况：
        system：是系统生成的文本(不包括用户输入的文本 prompt)
        user：是用户输入的文本加入到系统生成的文本之后 prompt+user)
        assistant：添加到completion中的文本
        """
        completion='好了，我的第一个任务是：'
        if user == "system":
            res= {"prompt": text+completion, "completion": ""}
            chat_history.append(res)
        elif user == "user":
            chat_history[-1]["prompt"] += text
        elif user == "assistant":
            chat_history[-1]["completion"] =text

    elif model_use_format == "Edit":
        if user== "system":
            res = {"input":"", "instruction": "text", "output": ""}
            chat_history.append(res)
        elif user == "user":
            chat_history[-1]["input"] = text
        elif user == "assistant":
            chat_history[-1]["output"] = text

    elif model_use_format == "Embedding":
        if user== "system":
            res = {"input":"", "output": ""}
            chat_history.append(res)
        elif user == "user":
            chat_history[-1]["input"] = text
        elif user == "assistant":
            chat_history[-1]["output"] = text

    elif model_use_format == "Image.create":
        if user== "system":
            chat_history.append({"prompt": "", "output": ""})
        elif user == "user":
            chat_history[-1]["prompt"] = text
        elif user == "assistant":
            chat_history[-1]["output"] = text

    elif model_use_format == "Image.create_edit":
        if user== "system":
            chat_history.append({"image": "", "mask": "",
                                 "prompt": "", "output": ""})
        elif user == "user":
            chat_history[-1]["prompt"] = text
        elif user == "assistant":
            chat_history[-1]["output"] = text







