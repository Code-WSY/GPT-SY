# GPT-SY

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/logo_gptsy.png" alt="logo" style="zoom:33%;" />

最近趁着国庆假期，写了一个**GPT**的桌面端应用程序，目前主要开发了如下功能：

1. **GPT模型集成**：将目前已有的OpenAI的GPT模型（免费的）集成到了程序中，可自行选择模型。
2. **参数调整**：提供一些参数调整的选项，如温度和输出长度参数。可以根据自己的需求调整生成文本的多样性和长度。
3. **提示库**：收集了目前流行和常用的提示库，并将其集成到应用程序中，以便对GPT更好的提问，从而获取最佳答案。
4. **保存对话记录**：可以将历史对话保存，并自动生成可供预训练的文件格式。

## 安装

### 安装`Openai`库

使用前请先安装`opneai`库：

```python
pip install openai
```

### API KEY

除了安装好`openai`的Python库之外，还需要有一个`API KEY`，一般注册`Openai`账号即可免费获得5美元的额度，足够日常使用。

存放的方式是在API_KEY文件夹下新建一个`API_KEY`文本（无后缀），将`API KEY`复制到第一行，每次运行会自动登录。

## 运行

直接运行`src/main.py`文件。

## 模式选择

### Promot-based

在这种模式下，通过选择`功能`选项，会先为GPT提供一个系统请求（prompt），然后再在输入框输入需要进行的任务内容。GPT会根据提示理解意图，并生成相应的回答。

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231003145334796.png" alt="image-20231003145334796" style="zoom:50%;" />



### Fine-tuning

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231003145736776.png" alt="image-20231003145736776" style="zoom:50%;" />

在这种模式下，可以将先前的对话导入到GPT中，并继续对话。这种模式利用了GPT已经在大规模文本数据上进行的预训练。通过将先前的对话作为输入，GPT可以根据之前的上下文来生成连贯的回复。这种模式适用于需要在现有对话基础上进行延续的场景。

注意：在切换到`Fine-tuning`前，请先清空历史对话。

导入文件格式如下：

```json
{"role": "system", "content": Request}
{"role": "user", "content": question1}
{"role": "assistant", "content": answer1}
{"role": "user", "content": question2}
{"role": "assistant", "content": answer2}
```

## 清空

### 清屏

仅仅是清空输出屏幕，不会清除历史对话

### 清空历史对话

会清空之前的对话内容，即消除GPT与你之间的对话记忆。

## 参数控制

### 温度

对应temperature参数，用于控制生成文本的多样性和随机性。较高的温度值会使生成的文本更加随机和多样化，而较低的温度值会使生成的文本更加确定和一致。温度参数会影响GPT生成下一个单词的概率分布。较高的温度值会使概率分布更加平均，使得不太可能的单词也有机会被选择，从而增加了多样性。较低的温度值会使概率分布更加尖锐，使得高概率的单词更有可能被选择，从而减少了多样性。根据应用需求，可以调整温度参数来控制生成文本的多样性和随机性。

### 输出长度

对应max_token参数，用于限制生成文本的长度。它指定了生成文本的最大标记数量。通过设置输出长度参数，可以控制生成文本的长度，以适应特定的应用场景或需求。

## 文本导入

如果有大段内容需要提交给GPT，可以通过`文件--→打开`，进行文本选择，内容将会导入到输入栏中。

## 导出对话

如果希望将对话进行保存，可以通过`文件--→保存`，保存位置是`Chat_history`文件夹下，对话内容将保存为`jsonlines`的格式，方便下一次通过`Fine-tuning`模式导入。

## **程序结构**

![image-20231003183729404](http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231003183729404.png)
