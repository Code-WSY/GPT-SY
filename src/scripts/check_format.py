import os
def check_format(file_name,format_list):
    """
    :param file_name: list or filename
    :param format_list: 可能的格式列表
    :return: file_name 符合的格式 in format_list
    """

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
            return format_list[-1], []
    # 检查每行的格式
    # 记录每行格式的列表
    line_format = []
    line_content = []
    try:

        for line in open_file.readlines():
            line = eval(line)
            # ChatCompletion格式

            if line.keys() == {"role", "content"}:
                if line["role"] in ["user", "assistant", "system"]:
                    line_format.append(format_list[0])
                    line_content.append(line)

                else:
                    line_format.append("Error")

            # Completion格式
            elif line.keys() == {"prompt", "completion"}:
                line_format.append(format_list[1])
                line_content.append(line)
            # 这里还可以加入其他格式
            # elif:.....

            # 格式错误
            else:
                return format_list[-1], line_content
        # 读取完毕，关闭文件
        open_file.close()
        try:
            os.remove("temp.wsy")
        except:
            pass
        # 检查格式是否一致
        if len(set(line_format)) == 1:
            return line_format[0], line_content
        else:
            return format_list[-1], line_content
    except:
        return format_list[-1], line_content



if __name__ == "__main__":
    format_list = ["ChatCompletion", "Completion", "Error"]
    file_name=[{"role":"system", "content":""},{"role":"user","content":""},{"role":"assistant","content":""}]
    #print(file_name_to_json)
    format, content = check_format(file_name, format_list)
    print(format)
    print(content)
