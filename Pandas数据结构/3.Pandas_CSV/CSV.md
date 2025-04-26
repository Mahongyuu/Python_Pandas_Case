Pandas CSV 文件操作详解
CSV (Comma-Separated Values) 是一种常用的数据存储格式，而 Pandas 是 Python 中最强大的数据处理库之一。Pandas 提供了简单易用的方法来读写 CSV 文件。

读取 CSV 文件
使用 pd.read_csv() 函数可以读取 CSV 文件：

import pandas as pd
# 基本读取
df = pd.read_csv('data.csv')
# 常用参数
df = pd.read_csv('data.csv',
sep=',',           # 分隔符，默认为逗号
header=0,         # 指定哪一行作为列名
index_col=0,      # 指定哪一列作为行索引
encoding='utf-8', # 编码方式
na_values=['NA', 'NULL'])  # 指定哪些值被视为缺失值
写入 CSV 文件
使用 to_csv() 方法将 DataFrame 写入 CSV 文件：

# 基本写入
df.to_csv('output.csv')
# 常用参数
df.to_csv('output.csv',
index=False,        # 不写入行索引
header=True,       # 写入列名
encoding='utf-8',  # 编码方式
sep=',',          # 分隔符
na_rep='NA')      # 缺失值表示方式
常用 CSV 操作示例

1. 查看数据
# 查看前5行
df.head()
# 查看后5行
df.tail()
# 查看数据概览
df.info()
# 查看统计信息
df.describe()

2. 处理缺失值
# 删除包含缺失值的行
df.dropna()
# 用特定值填充缺失值
df.fillna(0)
# 用前一个值填充缺失值
df.fillna(method='ffill')

3. 数据筛选
# 选择特定列
df[['column1', 'column2']]
# 条件筛选
df[df['column1'] > 100]
# 多条件筛选
df[(df['column1'] > 100) & (df['column2'] == 'value')]

4. 数据排序
# 按单列排序
df.sort_values('column1')
# 按多列排序
df.sort_values(['column1', 'column2'], ascending=[True, False])
处理大型 CSV 文件
对于大型 CSV 文件，可以使用以下技巧：

# 分块读取
chunk_size = 10000
chunks = pd.read_csv('large_data.csv', chunksize=chunk_size)
for chunk in chunks:
process(chunk)  # 处理每个数据块
# 只读取特定列
df = pd.read_csv('large_data.csv', usecols=['column1', 'column2'])
# 指定数据类型以减少内存使用
dtypes = {'column1': 'int32', 'column2': 'category'}
df = pd.read_csv('large_data.csv', dtype=dtypes)

常见问题解决
编码问题：尝试不同的编码方式，如 'utf-8', 'gbk', 'latin1'
分隔符问题：如果文件不是逗号分隔，指定正确的分隔符，如 sep='\t' 用于制表符分隔
日期解析：使用 parse_dates 参数解析日期列
df = pd.read_csv('data.csv', parse_dates=['date_column'])
Pandas 的 CSV 功能非常强大且灵活，可以处理各种复杂的数据格式和场景。

# 详细解读见
https://www.runoob.com/pandas/pandas-csv-file.html