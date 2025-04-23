import numpy as np
import pandas as pd

# 从列表创建
# data = [['张三', 18], ['李四', 19], ['王五', 20]]
# df = pd.DataFrame(data, columns=['name', 'age'])
# df['name'] = df['name'].astype(str)
# df['age'] = df['age'].astype(int)
# print(df)

# 从字典创建
# data = {'name': ['Mahongyu', 'Peichen', 'Wuhu'], 'professional': ['Student', 'unemployment', 'King']}
# df = pd.DataFrame(data)
# df['name'] = df['name'].astype(str)
# df['professional'] = df['professional'].astype(str)
# print(df)

# 从 NumPy 数组创建
# arr = np.array( ['Peichen', '18', 'BeiJin'],
#                 ['Mahongyu', '19', 'ShangHai'],
#                 ['Wuhu', '20', 'Shenzhen']
#                 ])
# df = pd.DataFrame(arr,columns=['Name', 'Age', 'Address'])
# print(df)

# DataFrame数据访问
data = {'姓名': ['张三', '李四', '王五', '刘六'],
        '年龄': [18, 20, 19, 30],
        '籍贯': ['河南', '海南', '云南', '四川']}
df = pd.DataFrame(data)
df['年龄'] = df['年龄'].astype(int)

# 按列选择
ages = df['年龄']
subset = df[['姓名', '籍贯']]
print('年龄列为:''\n', ages)
print('姓名和籍贯列为:\n', subset)

# 按行选择
row = df.loc[0]  # 第一行
print('第一行为:''\n', row)
# 按位置选择,即‘行’的索引
row = df.iloc[1]
print('第二行为:''\n', row)
# 切片选择多行
rows = df[1:3]
print('第二至三行为:''\n', rows)

# 条件选择
older = df[df['年龄'] > 18]
print('年龄大于18的为:''\n', older)
# 多条件选择
result = df[(df['年龄'] >= 20) & (df['籍贯'] == '四川')]
print('年龄大于20且籍贯位于四川的为:''\n', result)
