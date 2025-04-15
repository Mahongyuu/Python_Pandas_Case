import pandas as pd


class Series():

    # 创建series

    # 由数组创建series
    def create_from_array(self, arr):
        series = pd.Series(arr, name='data')
        return series

    # 由字典创建，key作为键
    def create_from_dict(self, dict):
        series_1 = pd.Series(dict, name='data_1')
        return series_1

    # 自定义索引创建
    def create_from_index(self, arr, index):
        series_2 = pd.Series(arr, index=index, name='data_2')
        return series_2

    # Series 索引对齐
    # Pandas 的一个强大特性是索引自动对齐：
    def index_alignment(self, arr, dict, index):
        series_3 = pd.Series(arr, index=index, name='data_3')
        series_4 = pd.Series(dict, name='data_4')
        series_5 = series_3 + series_4
        return series_5


arr = [1, 2, 3, 4, 5]
arr_1 = ['a', 'b', 'c', 'd', 'e']
index_1 = arr_1
dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
dict_1 = {'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
result_1 = Series().create_from_array(arr)
print(result_1, '\n', '该series的索引1的值为：', result_1[1])
result_2 = Series().create_from_dict(dict)
print(result_2, '\n', '该series的索引1的值为：', result_2[1])
result_3 = Series().create_from_index(arr_1, arr)
print(result_3, '\n', '该series的索引1的值为：', result_3[1])
result_4 = Series().index_alignment(arr, dict_1, index_1)
print(result_4, '\n', '该series的缺失值为：', result_4.isna())



