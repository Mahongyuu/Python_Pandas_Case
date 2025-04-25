# import pandas as pd
# from fontTools.ttx import process
# '''  需要安装 openpyxl 或 xlrd 库
#     才可以写入excel文件
#     对于 .xls 文件使用 xlrd，对于 .xlsx 文件使用 openpyxl
# '''
# # 读取整个excel文件
# df = pd.read_excel('male_data.xlsx')
# df.to_csv('male_data.csv')
# # 按特定工作表（sheet）读取 ，’参数‘ = sheet_name
# df_0 = pd.read_excel('male_data.xlsx', sheet_name='Sheet1')
# # 按索引获取工作表（sheet）
# df_1 = pd.read_excel('male_data.xlsx',sheet_name=0)  # 第一个工作表
#
# # 高级读取选项
# # 指定列 ’参数‘ = usecols=['列名']
# df_2 = pd.read_excel('file.xlsx', usecols=['A', 'C'])  # 读取A列和C列
# df_3 = pd.read_excel('file.xlsx', usecols=[0, 2])  # 读取第1和第3列
#
# # 指定行范围 ’参数‘ = skiprows,nrows
# df_4 = pd.read_excel('file.xlsx', skiprows=3)  # 跳过前3行
# df_5 = pd.read_excel('file.xlsx', nrows=100)  # 只读取前100行
#
# # 处理标题 ’参数‘ = header
# df_6 = pd.read_excel('file.xlsx', header=None)  # 无标题行
# df_7 = pd.read_excel('file.xlsx', header=2)  # 使用第3行作为标题
#
# # 指定索引列 ’参数‘ = index_col
# df_8 = pd.read_excel('file.xlsx', index_col=0)
#
#
# # 写入excel文件
# df_a = pd.read_csv('male_data.csv')
# df_b = pd.read_csv('female_data.csv')
# # 写入单个DataFrame
# df_a.to_excel('male_data.xlsx', index=False)
# df_b.to_excel('female_data.xlsx', index=False)
# # 写入多个DataFrame到不同工作表（sheet）
# with pd.ExcelWriter('all.xlsx') as writer:
#     df_a.to_excel(writer, sheet_name='Sheet1')
#     df_b.to_excel(writer, sheet_name='Sheet2')
#
# # 高级写入选项
# # 控制写入位置 '参数'=startrow，startcol
# df.to_excel('output.xlsx', startrow=2, startcol=3)  # 从第3行第4列开始写入
# # 格式化
# df.to_excel('output.xlsx',
#             float_format="%.2f",   # 浮点数格式
#             freeze_panes=(1, 1))    # 冻结首行首列
# # 追加到现有文件
# with pd.ExcelWriter('existing_file.xlsx', mode='a') as writer:
#     df.to_excel(writer, sheet_name='NewSheet')
#
#
# # 处理多个工作表
# # 读取所有工作表
# all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # 返回字典
# # 访问特定工作表
# sheet1 = all_sheets['Sheet1']
# # 写入多个工作表
# with pd.ExcelWriter('output.xlsx') as writer:
#     for sheet_name, df in df.items():
#         df.to_excel(writer, sheet_name=sheet_name)
#
# # 处理大型 Excel 文件
# # 对于大型文件，可以使用 chunksize 参数分块读取：
# # 分块读取
# chunk_size = 1000
# chunks = pd.read_excel('large_file.xlsx', chunksize=chunk_size)
#
# for chunk in chunks:
#     process(chunk)  # 处理每个块
