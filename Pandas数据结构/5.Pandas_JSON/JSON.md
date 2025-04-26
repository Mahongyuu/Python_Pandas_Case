Pandas 与 JSON 数据处理详解
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，而 Pandas 是 Python 中强大的数据分析库。Pandas 提供了多种方法来处理 JSON 数据，使得数据科学家能够轻松地将 JSON 数据转换为 DataFrame 进行分析。

1. 读取 JSON 数据
Pandas 提供了 read_json() 函数来从 JSON 文件或字符串创建 DataFrame。

基本用法
import pandas as pd

# 从JSON文件读取
df = pd.read_json('data.json')

# 从JSON字符串读取
json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]}'
df = pd.read_json(json_str)
# 在较新版本的 Pandas 中，直接向 read_json() 传递 JSON 字符串字面量的方式已被弃用，未来将会移除。建议将 JSON 字符串包装在 StringIO 对象中。
df = pd.read_json(StringIO(json_str))

参数详解
orient: 指定 JSON 字符串的预期格式

'split' : dict like {index -> [index], columns -> [columns], data -> [values]}

'records' : list like [{column -> value}, ... , {column -> value}]

'index' : dict like {index -> {column -> value}}

'columns' : dict like {column -> {index -> value}}

'values' : just the values array

# 不同orient参数的示例
data = {
"name": {"0": "Alice", "1": "Bob"},
"age": {"0": 25, "1": 30}
}
df = pd.read_json(json.dumps(data), orient='index')
dtype: 指定列的数据类型

convert_dates: 尝试解析日期列

lines: 对于行分隔的 JSON 文件（每行一个 JSON 对象），设置为 True

2. 将 DataFrame 转换为 JSON
   Pandas 提供了 to_json() 方法将 DataFrame 转换为 JSON 格式。

基本用法
# 将DataFrame转换为JSON字符串
json_str = df.to_json()

# 指定输出格式
json_str = df.to_json(orient='records')

# 写入JSON文件
df.to_json('output.json', orient='records')
参数详解
orient: 与 read_json 相同的格式选项

date_format: 日期格式化选项 ('epoch' 或 'iso')

double_precision: 编码浮点数时使用的小数位数

force_ascii: 强制将字符串编码为 ASCII

3. 处理嵌套 JSON
JSON 数据常常包含嵌套结构，Pandas 提供了几种方法来处理这种数据。

方法1: json_normalize
json_normalize() 是处理嵌套 JSON 的强大工具。

from pandas import json_normalize

nested_data = [
{
"name": "Alice",
"age": 25,
"address": {
"street": "123 Main St",
"city": "Boston"
}
},
{
"name": "Bob",
"age": 30,
"address": {
"street": "456 Oak Ave",
"city": "New York"
}
}
]

df = json_normalize(nested_data)
# 结果会自动展开嵌套字典
方法2: 使用 apply 和 pd.Series
# 假设df有一个包含嵌套字典的列
df['address'].apply(pd.Series)

4. 处理 JSON 数组
JSON 数组可以转换为 Pandas 的列表列，然后进一步展开。

data = {
"name": ["Alice", "Bob"],
"skills": [["Python", "SQL"], ["Java", "C++"]]
}

df = pd.DataFrame(data)

# 展开skills列
df_exploded = df.explode('skills')

5. 从API获取JSON数据
Pandas 可以直接从网络API获取JSON数据。

import requests

url = "https://api.example.com/data"
response = requests.get(url)
df = pd.read_json(response.text)

6. 处理大型JSON文件
   对于大型JSON文件，可以使用分块读取：

# 使用chunksize参数
chunks = pd.read_json('large_data.json', lines=True, chunksize=1000)
for chunk in chunks:
process(chunk)  # 处理每个块

7. 常见问题与解决方案
问题1: JSON解码错误
解决方案: 确保JSON格式正确，可以使用在线验证器检查。

问题2: 日期解析不正确
解决方案: 明确指定日期列和格式

df = pd.read_json(data, convert_dates=['date_column'])

问题3: 内存不足
解决方案: 使用分块读取或考虑使用更高效的数据格式如 Parquet。

8. 性能优化技巧
如果JSON文件很大，考虑使用lines=True并按行处理

只读取需要的列: pd.read_json(..., columns=['col1', 'col2'])

对于重复处理，考虑将JSON转换为更高效的格式如Parquet

9. 实际示例
   示例1: 处理Reddit API数据
   python
   import requests

url = "https://www.reddit.com/r/python.json"
headers = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
data = response.json()

# 提取帖子数据
posts = data['data']['children']
df = json_normalize([post['data'] for post in posts])

# 选择感兴趣的列
df = df[['title', 'score', 'num_comments', 'created_utc']]

# 转换时间戳
df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')

示例2: 处理嵌套的电商数据
order_data = {
"orders": [
{
"order_id": 1001,
"customer": {
"name": "Alice",
"email": "alice@example.com"
},
"items": [
{"product": "Laptop", "price": 999.99, "quantity": 1},
{"product": "Mouse", "price": 19.99, "quantity": 2}
]
},
{
"order_id": 1002,
"customer": {
"name": "Bob",
"email": "bob@example.com"
},
"items": [
{"product": "Keyboard", "price": 49.99, "quantity": 1}
]
}
]
}

# 展开订单数据
orders_df = json_normalize(
order_data['orders'],
meta=['order_id', ['customer', 'name'], ['customer', 'email']],
record_path='items'
)
通过掌握这些 Pandas 处理 JSON 的技巧，你可以高效地将各种 JSON 格式的数据转换为结构化的 DataFrame，为后续的数据分析做好准备。

# 详细讲解：
https://www.runoob.com/pandas/pandas-json.html