# pip install python-dotenv clickhouse-connect

import os
import clickhouse_connect

from dotenv import load_dotenv


# 加载 .env 文件
load_dotenv()


# 创建 ClickHouse 客户端连接
client = clickhouse_connect.get_client(
    host=os.getenv("CH_HOST"),          # Docker 宿主机 IP
    port=os.getenv("CH_PORT"),          # ClickHouse HTTP 端口
    username=os.getenv("CH_USER"),      # 用户名
    password=os.getenv("CH_PASSWORD"),  # 密码
    database=os.getenv("CH_DATABASE")   # 数据库名
)

query = "SELECT * FROM entertainment.anime_info LIMIT 3"
try:
    # 执行 SQL 查询
    result = client.query(query)

    # 打印查询结果
    print("查询结果：")
    for row in result.named_results():
        print(row)

    # 获取表结构信息
    schema_result = client.query("DESCRIBE entertainment.anime_info")
    print("\n表结构：")
    for column in schema_result.named_results():
        print(f"{column['name']}: {column['type']}")

except Exception as e:
    print(f"查询出错: {e}")
finally:
    client.close()
