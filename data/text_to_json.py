filename='日常管理助手.txt'
#读取文本并转换为json格式
lines=open(filename,'r',encoding='utf-8').readlines()
#转成一个字符串
text=''.join(lines)
# 并将转义字符转成可见的如\n变为\\n,"变为\"
text=''.join(lines).replace('\n','\\n')
text=text.replace('"','\\"')
print(text)



