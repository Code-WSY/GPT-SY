# 更新：GPT-SY的一些改进

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/logo_gptsy.png" alt="logo" style="zoom:33%;" />

因为之前写的GUI还是太粗糙了，所以进行了许多地方的改进和优化。

源代码地址：

[Code-WSY/GPT-SY: A desktop application for GPT. (github.com)](https://github.com/Code-WSY/GPT-SY)

## 安装

### 安装`Openai`库

使用前请先保证自己的`python`环境安装了`opneai`库：

```bash
pip install openai
```

## 启动

直接运行`src/Main.py`启动界面：

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009173520955.png" alt="启动界面" style="zoom:50%;" />

## 登录

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009173612885.png" alt="image-20231009173612885" style="zoom:50%;" />

- `Latest API KEY`：直接登录最新添加的API KEY。

- `Create API KEY`：添加自己的API KEY。

  - API_KEY：必填。
  - API_BASE：可选，默认官方：`https://api.openai.com/v1`地址，如果采用其他中转，需修改此处。
  - API_note：对该API的备注信息。可选，默认是创建时间。

  ![API 创建](http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009175403839.png)

- `Choose API KEY`：从之前添加的API KEY选择账号登录。

- `Delete API KEY`：删除之前添加过得API KEY。

## 模式

![模式选项](http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009173945946.png)

- `ChatCompletion`：用于进行对话式交互的模式。在这种模式下，可以提出一个或多个问题、陈述或指令，模型提供相应的响应。ChatCompletion模式旨在模拟真实对话中的交互，因此模型的响应通常会考虑到上下文，并且可以**基于之前的对话进行连贯的回复**。
- `Completion`：单向生成文本的模式。在这种模式下，提供一个初始的文本片段，然后模型将根据这个片段生成一个完整的补全文本。Completion模式通常用于**生成文章、段落、故事、代码**等**长篇文本**。
- `Edit`：Edit模式是对现有文本进行编辑和修改**。在这种模式下，您提供一个初始的文本片段，并提供模型对其进行修改或编辑的建议。模型将尝试根据您的指示对文本进行修改，并生成一个经过编辑的版本。
- `Embedding`：将文本转换为向量表示的模式。在这种模式下，提供一个文本片段，然后模型将返回一个**向量**，该向量表示了该文本的语义信息。这种嵌入表示可以用于计算文本之间的相似性、进行**聚类分析、训练机器学习**模型等各种自然语言处理任务。

## 模型

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009174705360.png" alt="可用模型" style="zoom:50%;" />

- **可用引擎**：会输出该API目前可用的`engine`。

## 外观

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009174819665.png" alt="外观" style="zoom:50%;" />

用于修改当前界面的字体、字号、颜色和整体窗口大小。

## 清空

<img src="http://sy0316.oss-cn-hangzhou.aliyuncs.com/img/image-20231009174943424.png" alt="清空" style="zoom:50%;" />

- **清屏**：清除对话窗口内容，但不清除历史记录。
- **清空对话**：清空对话窗口信息和当前模式下的历史记录。

## 文本生成参数

### 温度

对应temperature参数，用于控制生成文本的多样性和随机性。较高的温度值会使生成的文本更加随机和多样化，而较低的温度值会使生成的文本更加确定和一致。温度参数会影响GPT生成下一个单词的概率分布。较高的温度值会使概率分布更加平均，使得不太可能的单词也有机会被选择，从而增加了多样性。较低的温度值会使概率分布更加尖锐，使得高概率的单词更有可能被选择，从而减少了多样性。根据应用需求，可以调整温度参数来控制生成文本的多样性和随机性。

### 输出长度

对应max_token参数，用于限制生成文本的长度。它指定了生成文本的最大标记数量。通过设置输出长度参数，可以控制生成文本的长度，以适应特定的应用场景或需求。

### 模型

该下拉栏会显示当前模式下的可用模型，方便进行选择。

### 功能

显示该模式下适用的提示库。

## 文件

- **打开**：选择文本，自动导入到输入窗口中。
- **保存**：保存当前模式下的历史对话记录（ChatLogs/）。
- **另存为**：将保存内容另存到其他地方。
- **导入历史记录**：将之前的对话记录导入到模型中，主要用于继续对话或者模型的预训练（通过修改历史对话内容实现）。

## 其他改进

- 为了更好的实现对话响应和长文本输出，采用文本流方式进行输出，实时输出文本。
