import json
import re
#读取json文件
with open('promot_old.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    name=[]
    content=[]
    for i in data:
        if '我的第一' in i['prompt']:
            #讲i['prompt']中的\n替换为空
            i['prompt'] = re.sub('\n','',i['prompt'])
            #print(i['prompt'][i['prompt'].find('我的第一'):])
            #打印之前的内容
            name.append(i['act'])
            content.append(i['prompt'][:i['prompt'].find('我的第一')])

    for i in range(len(name)):
        print(name[i])
        print(content[i])
#写入json文件,处理后的数据
filename= '../data/prompts.json'
#每行包含；{"act":"name","promot":"content"}
new_data=[]
for i in range(len(name)):
    new_data.append({"act":name[i],"prompt":content[i]})

#写入json文件
with open(filename,'w',encoding='utf-8') as f:
    json.dump(new_data,f,ensure_ascii=False,indent=4) #indent=4表示缩进4个空格




