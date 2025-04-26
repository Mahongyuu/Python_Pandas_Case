import pandas as pd
from io import StringIO
from pandas import json_normalize
from glom import glom

# # 读取json文件
# df = pd.read_json('female_data.json', encoding='utf-8')
# print(df)

# # 从json字符串中读取
# json_str = '{"姓名": ["张三", "李四"], "age": [25, 30]}'
# df_0 = pd.read_json(StringIO(json_str))
# print(df_0)

# # 写入json文件
# df_1 = pd.read_csv('male_data.csv', encoding='utf-8')
# df_1.to_json('male_data.json', orient='records')

# # 处理嵌套json
# nested_data = [  # 嵌套数据
#     {
#         "name": "Alice",
#         "age": 25,
#         "address": {
#             "street": "123 Main St",
#             "city": "Boston"
#         }
#     },
#     {
#         "name": "Bob",
#         "age": 30,
#         "address": {
#             "street": "456 Oak Ave",
#             "city": "New York"
#         }
#     }
# ]
# # 方法1
# df_2 = json_normalize(nested_data)
# # 结果会自动展开嵌套字典
# print(df_2)

# # 通过 glom 模块来处理数据套嵌，glom 模块允许我们使用 . 来访问内嵌对象的属性。
# df_4 = pd.read_json('test.json')
# data_0 = df_4['students'].apply(lambda row: glom(row, 'grade.physics'))
# print(data_0)

# # 处理json数组
# data = {
#     "name": ["Alice", "Bob"],
#     "skills": [["Python", "SQL"], ["Java", "C++"]]
# }
# df_3 = pd.DataFrame(data)
# # 展开skills列
# df_4 = df_3.explode('skills')
# print(df_4)
