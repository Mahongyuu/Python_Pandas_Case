import pandas as pd
import numpy as np
import random

from faker import Faker

'''
生成随机数据用于测试Pandas中Excel的文件操作
此处生成男女数据（姓名，籍贯，身高，体重，婚恋）
各500条
'''


# 初始化Faker库生成随机数据
fake = Faker('zh_CN')

# 设置随机种子保证结果可复现
np.random.seed(42)
random.seed(42)


# 生成男生数据
def generate_male_data(num):
    data = []
    for _ in range(num):
        data.append({
            '姓名': fake.name_male(),
            '年龄': random.randint(18, 45),
            '籍贯': fake.province(),
            '身高': round(np.random.normal(172, 6), 1),
            '体重': round(np.random.normal(70, 8), 1),
            '婚恋': random.choice(['单身', '恋爱中', '已婚', '离异'])
        })
    return pd.DataFrame(data)


# 生成女生数据
def generate_female_data(num):
    data = []
    for _ in range(num):
        data.append({
            '姓名': fake.name_female(),
            '年龄': random.randint(18, 45),
            '籍贯': fake.province(),
            '身高': round(np.random.normal(162, 5), 1),
            '体重': round(np.random.normal(55, 6), 1),
            '婚恋': random.choice(['单身', '恋爱中', '已婚', '离异'])
        })
    return pd.DataFrame(data)


# 生成各100条数据
male_df = generate_male_data(500)
female_df = generate_female_data(500)

# 查看生成的数据样例
print("男生数据样例:")
print(male_df.head())
print("\n女生数据样例:")
print(female_df.head())

# 保存为CSV文件（可选）
male_df.to_csv('male_data.csv', index=False, encoding='utf-8-sig')
female_df.to_csv('female_data.csv', index=False, encoding='utf-8-sig')
