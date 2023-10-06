import os
def check_mode(file_name,selected_mode):
    if type(file_name) == list:
        open_file = open("temp.wsy", "w", encoding="utf-8")
        for line in file_name:
            open_file.write(str(line)+"\n")
        open_file.close()
        open_file = open("temp.wsy", "r", encoding="utf-8")
    else:
        try:
            open_file = open(file_name, "r", encoding="utf-8")
        except:
            return False

    if selected_mode == "ChatCompletion":
        for line in open_file.readlines():
            line = eval(line)
            # ChatCompletion格式
            if line.keys() == {"role", "content"}:
                if line["role"] in ["user", "assistant", "system"]:
                    continue
                else:

                    open_file.close()
                    if type(file_name) == list:
                        os.remove("temp.wsy")
                    return False

    if selected_mode == "Completion":
        for line in open_file.readlines():
            line = eval(line)
            # Completion格式
            if line.keys() == {"prompt", "completion"}:
                continue
            else:

                open_file.close()
                if type(file_name) == list:
                    os.remove("temp.wsy")
                return False

    if selected_mode == "Edit":
        for line in open_file.readlines():
            line = eval(line)
            # Edit格式
            if line.keys() == {"input", "instruction"}:
                continue
            else:
                open_file.close()
                if type(file_name) == list:
                    os.remove("temp.wsy")
                return False

    if selected_mode == "Embedding":
        for line in open_file.readlines():
            line = eval(line)
            # Embedding格式
            if line.keys() == {"input", "output"}:
                continue
            else:
                open_file.close()
                if type(file_name) == list:
                    os.remove("temp.wsy")
                return False

    if selected_mode == "Image.create":
        for line in open_file.readlines():
            line = eval(line)
            # Image.create格式
            if line.keys() == {"prompt", "output"}:
                continue
            else:
                open_file.close()
                if type(file_name) == list:
                    os.remove("temp.wsy")
                return False

    if selected_mode == "Image.create_edit":
        for line in open_file.readlines():
            line = eval(line)
            # Image.create_edit格式
            if line.keys() == {"image","mask","prompt","output"}:
                continue
            else:
                open_file.close()
                if type(file_name) == list:
                    os.remove("temp.wsy")
                return False
    #删除临时文件
    # 关闭文件
    open_file.close()
    if type(file_name) == list:
        os.remove("temp.wsy")
    return True

if __name__ == "__main__":
    file_name=[{"role":"system", "content":""},{"role":"user","content":""},{"role":"assistant","content":""}]
    format = check_mode(file_name, "Completion")
    print(format)
