def is_prompt_changed(chat_history,selected_model_format,selected_prompt):
    #从后往前读取chat_history，直到遇到chat_history中的元素对应role=system
    for i in range(len(chat_history)-1, -1, -1):
        if selected_model_format=="ChatCompletion":
            """
            对于ChatCompletion格式，
            如果最新的role=system的元素的content与selected_prompt不同，就返回True
            或者如果没有找到role=system的元素，就返回True（导入转功能可能会出现这种情况）
            其余情况返回False
            """
            if chat_history[i]["role"] == "system":
                if chat_history[i]["content"] != selected_prompt:
                    return True
                else:
                    return False
            #如果没有找到role=system的元素，就返回True
            if i == 0:
                return True

        elif selected_model_format == "Completion":
            """
            对于Completion格式:
            直接返回True
            """
            return True