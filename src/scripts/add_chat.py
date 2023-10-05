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
        if user == "system":
            res= {"prompt": text, "completion": ""}
            chat_history.append(res)
            if len(chat_history) ==2 and chat_history[0]["completion"] == "":
                #说明是初始化，删除第一个元素
                chat_history.pop(0)

        elif user == "user":
            chat_history[-1]["prompt"] += text

        elif user == "assistant":
            chat_history[-1]["completion"] =text




