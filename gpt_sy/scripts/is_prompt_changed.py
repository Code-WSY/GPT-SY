def is_prompt_changed(chat_history,selected_mode,selected_prompt_title):
    if len(chat_history) == 0:
        return True
    for i in range(len(chat_history)-1, -1, -1):
        if selected_mode== "ChatCompletion":
            """
            对于ChatCompletion格式
            如果最新的role=system的元素的content与selected_prompt不同，就返回True
            或者如果没有找到role=system的元素，就返回True
            其余情况返回False
            """
            if chat_history[i]["role"] == "system":
                if chat_history[i]["content"] != selected_prompt_title:
                    return True
                else:
                    return False
            #如果没有找到role=system的元素，就返回True
            if i == 0:
                return True

        #单次对话模型
        elif selected_mode == "Completion":
            return True
        elif selected_mode == "Edit":
            return True
        elif selected_mode == "Embedding":
            return True
        elif selected_mode == "Image.create":
            return True
        elif selected_mode == "Image.create_edit":
            return True