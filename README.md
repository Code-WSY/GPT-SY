# GPT-SY

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/logo_gptsy.png" alt="logo" style="zoom:33%;" />

新版更新：

1. 将GPT回答的输出改为流式传输，好处在于**按需生成文本，而不需要等到整个文本都生成完毕**。这对于处理**大型文本生成任务**来说非常有用，因为它可以降低内存占用和网络带宽使用，并且可以更快地获得部分结果。
2. 优化默认配色，并增加了字体、颜色、字号的修改设置。
3. 解决了提出问题的用户。

最近趁着国庆假期，写了一个**GPT**的桌面端应用程序，目前主要开发了如下功能：

1. **GPT模型集成**：将目前已有的OpenAI的GPT模型（免费的）集成到了程序中，可自行选择模型。
2. **参数调整**：提供一些参数调整的选项，如温度和输出长度参数。可以根据自己的需求调整生成文本的多样性和长度。
3. **提示库**：收集了目前流行和常用的提示库，并将其集成到应用程序中，以便对GPT更好的提问，从而获取最佳答案。
4. **保存对话记录**：可以将历史对话保存，并自动生成可供预训练的文件格式。
5. **支持预训练模式**：允许通过导入对话来生成新对话。

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

直接运行`src/Main.py`文件。

## 模式选择

### Prompt-based

在这种模式下，通过选择`功能`选项，会先为GPT提供一个系统请求（prompt），然后再在输入框输入需要进行的任务内容。GPT会根据提示理解意图，并生成相应的回答。

<img src="C:\Users\WangSuyun\AppData\Roaming\Typora\typora-user-images\image-20231005212509480.png" alt="界面风格" style="zoom:50%;" />



注意：

1. 这是默认模式。

2. 如果在对话中途切换功能，对于`ChatCompletion`，会先将`system`的`prompt`提交，再将用户输入的文本提交。

3. 对于`Completion`，由于是无记忆的，并且`completion`非空，因此会直接在历史记录加入对应功能的`prompt`：

   ```json
   {"prompt": prompt+input, "completion": ""}
   ```

   具体参加`is_prompt_changed.py`。

   

### Fine-tuning

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231005212700689.png" alt="界面" style="zoom:50%;" />

在这种模式下，可以将先前的对话导入，并继续对话。这种模式利用了GPT已经在大规模文本数据上进行的预训练。通过将先前的对话作为输入，GPT可以根据之前的上下文来生成连贯的回复。这种模式适用于需要在现有对话基础上进行延续的场景。

如果不导入文件直接进行对话，

- 对于`ChatCompletion`,即为无任何提示词的对话。
- 对于`Completion`，

导入文件格式如下：

```json
{"role": "system", "content": Request}
{"role": "user", "content": question1}
{"role": "assistant", "content": answer1}
{"role": "user", "content": question2}
{"role": "assistant", "content": answer2}
```

**注意：**

1. 导入文件后，历史对话记录将会被清空，GPT将不会记得之前的对话内容（主要针对`ChatCompletion`）
2. 导入的文件对`Completion`对于的格式来说，没有意义，因为这是单文本对话，该形式的微调目前收费。
3. **未导入文件不能进行对话。**

## 模式切换

- 从Fine-tunning切换到Prompt-based，
  - 对于`ChatCompletion`，会根据选择的功能加入`system`语句并继续对话。
  - 对于`Completion`，由于是单文本对话，因此只是导入了历史记录，对话无影响。

- 从Prompt-based切换到Fine-tunning，
  - 对于`ChatCompletion`实际就是之前历史对话的延续，不会加入`system`语句。
  - 对于`Completion`，为无promote对话模式。

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

目前仅支持文本格式导入。

## 导出对话

如果希望将对话进行保存，可以通过`文件--→保存`，保存位置是`Chat_history`文件夹下，对话内容将保存为`jsonlines`的格式，方便下一次通过`Fine-tuning`模式导入。

## 示例

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231005212939448.png" alt="image-20231005212939448" style="zoom:50%;" />

在选择不同模型时，会提供该模型的基本信息：

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231005213213261.png" alt="image-20231005213213261" style="zoom:50%;" />

## 获取地址：

[Code-WSY/GPT-SY: A desktop application for GPT. (github.com)](https://github.com/Code-WSY/GPT-SY)

