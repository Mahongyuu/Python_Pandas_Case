Pandas 数据结构 - DataFrame
DataFrame 是 Pandas 中最常用的数据结构，它是一个二维的、大小可变的、可以包含异构数据的表格结构，类似于电子表格或 SQL 表。

DataFrame 基本特性
二维结构：有行和列
可变大小：可以动态调整
异构数据：每列可以是不同的数据类型
标签索引：行和列都有标签
强大的数据操作：支持各种数据操作和分析功能

创建 DataFrame
从字典创建
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)

从列表创建
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

从 NumPy 数组创建
import numpy as np

arr = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris']
])

df = pd.DataFrame(arr, columns=['Name', 'Age', 'City'])
print(df)

访问 DataFrame 数据
选择列
# 选择单列
ages = df['Age']
# 选择多列
subset = df[['Name', 'City']]

选择行
# 使用 loc 按标签选择'行'
row = df.loc[0]  # 第一行
# 使用 iloc 按位置选择'行'
row = df.iloc[1]  # 第二行
# 切片选择多行
rows = df[1:3]  # 第二和第三行

条件选择
# 选择年龄大于30的行
older = df[df['Age'] > 30]

# 多条件选择
result = df[(df['Age'] > 25) & (df['City'] == 'London')]

修改 DataFrame
添加列
df['Salary'] = [70000, 80000, 90000]  # 添加新列
df['Senior'] = df['Age'] > 30  # 基于条件添加列
修改值
df.loc[0, 'Age'] = 26  # 修改单个值
df['Age'] = df['Age'] + 1  # 修改整列
删除数据
python
# 删除列
df = df.drop('Salary', axis=1)

# 删除行
df = df.drop(1, axis=0)  # 删除第二行
DataFrame 常用操作

基本信息
df.shape  # 返回 (行数, 列数)
df.info()  # 显示数据类型和内存信息
df.describe()  # 显示数值列的统计信息

排序
python
df.sort_values('Age')  # 按年龄升序
df.sort_values('Age', ascending=False)  # 降序

处理缺失值
python
df.isnull()  # 检查缺失值
df.fillna(0)  # 用0填充缺失值
df.dropna()  # 删除包含缺失值的行

分组聚合
df.groupby('City')['Age'].mean()  # 按城市分组计算平均年龄
输入输出

读取数据
# 从CSV文件读取
df = pd.read_csv('data.csv')
# 从Excel文件读取
df = pd.read_excel('data.xlsx')

# 从SQL数据库读取
# df = pd.read_sql('SELECT * FROM table', con)

写入数据
# 写入CSV文件
df.to_csv('output.csv', index=False)
# 写入Excel文件
df.to_excel('output.xlsx', index=False)
# 写入SQL数据库
# df.to_sql('table_name', con, if_exists='replace')
DataFrame 是 Pandas 的核心数据结构，提供了丰富的数据操作和分析功能，是数据科学和数据分析中的重要工具。

# 详细解读
https://www.runoob.com/pandas/pandas-dataframe.html