# chat-to-clickhouse

一个可以访问 [ClickHouse](https://github.com/ClickHouse/ClickHouse) 数据库的 ChatBI。

## 一、技术栈

- **前端**: `Gradio`
- **后端**: `Qwen Agent`
- **数据库**: `ClickHouse`
- **MCP**: `mcp-clickhouse`

## 二、配置文件

LLM 和 数据库 的配置在 `.env` 文件中，按律不上传。

它的格式如下：

```
CH_HOST=localhost
CH_PORT=18123
CH_USER=admin
CH_PASSWORD=[YOUR_CLICKHOUSE_PASSWORD]
CH_DATABASE=entertainment
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_API_KEY=[YOUR_DEEPSEEK_API_KEY]
```

> **Note:** 请先在项目根目录下创建 `.env` 文件

## 三、本地运行

启动 Gradio：

```bash
# 一个 Chat APP，无法连接数据库
nohup python gradio_app.py

# 一个简单的 ChatBI，可以连接 ClickHouse 数据库
nohup python gradio_ch_agent.py
```

启动后，打开浏览器访问 [http://localhost:7860/](http://localhost:7860/)

如果你像我一样，导入了动漫数据集 [top-popular-anime](https://www.kaggle.com/datasets/tanishksharma9905/top-popular-anime)，可以这么提问：

- 所有动漫的平均评分是多少？
- ID 为 100 的动画的出品方是？
- 评分大于 9.0 的动画有多少？
- 评分人数最多的十部动漫是？
- 评分人数超过一万人的动画中，排名前 5 的是？
- 2023 年开始播出的动画有多少？
- 制作超过 15 部动漫的工作室有哪些？

> [!NOTE]
> 如果你希望了解 如何安装 ClickHouse 数据库，以及 如何向 ClickHouse 数据库导入数据，可以参考我的文章[《耶是 ClickHouse！我们有救了！！》](https://luochang212.github.io/posts/chat_to_clickhouse/)
