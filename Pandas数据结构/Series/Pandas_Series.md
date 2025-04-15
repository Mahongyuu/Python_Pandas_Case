Pandas 数据结构 - Series
Series 是 Pandas 中最基本的一维数据结构，类似于带标签的数组或字典。

Series 基本特性
一维数据结构：可以存储任何数据类型（整数、字符串、浮点数、Python对象等）

带标签的索引：可以自定义索引标签

类型统一：一个 Series 中的所有元素通常是相同的数据类型

创建 Series
可以使用 pd.Series() 构造函数创建一个 Series 对象，传递一个数据数组（可以是列表、NumPy 数组等）和一个可选的索引数组。

pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
参数说明：

data：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
index：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
dtype：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
name：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
fastpath：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。
从列表创建
import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data)
print(s)

从字典创建（字典的键会成为索引）
data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(data)
print(s)

指定索引
data = [10, 20, 30, 40]
index = ['A', 'B', 'C', 'D']
s = pd.Series(data, index=index)
print(s)
Series 基本操作
访问元素
# 通过索引位置
print(s[0])
# 通过索引标签
print(s['A'])
# 切片操作
print(s[1:3])
print(s['B':'D'])

基本属性
print(s.values)  # 获取值数组
print(s.index)   # 获取索引
print(s.dtype)   # 数据类型
print(s.shape)   # 形状
print(s.size)    # 元素数量

基本统计方法
print(s.sum())     # 求和
print(s.mean())    # 平均值
print(s.std())     # 标准差
print(s.min())     # 最小值
print(s.max())     # 最大值
print(s.describe()) # 描述性统计


Series 索引对齐
Pandas 的一个强大特性是索引自动对齐：
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
print(s1 + s2)
# 输出:
# a    NaN
# b    6.0
# c    8.0
# d    NaN
缺失数据处理
Pandas 用 NaN 表示缺失数据：
# 检测缺失值
print(s.isna())
# 删除缺失值
print(s.dropna())
# 填充缺失值
print(s.fillna(0))
向量化操作
Series 支持向量化操作，无需循环：


s = pd.Series([1, 2, 3, 4])
print(s * 2)           # 每个元素乘以2
print(s + s)           # 对应元素相加
print(np.log(s))       # 对每个元素取对数
Series 是 Pandas 的基础，DataFrame 实际上是由多个 Series 组成的。理解 Series 是掌握 Pandas 的关键。

详见：
https://www.runoob.com/pandas/pandas-series.html