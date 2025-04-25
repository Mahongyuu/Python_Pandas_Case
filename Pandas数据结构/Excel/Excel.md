Pandas Excel 文件操作指南
Pandas 提供了强大的 Excel 文件读写功能，主要通过 read_excel() 和 to_excel() 方法实现。以下是详细的操作指南：

读取 Excel 文件
基本读取
import pandas as pd
# 读取整个 Excel 文件
df = pd.read_excel('file.xlsx')
# 读取特定工作表
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
# 或使用索引
df = pd.read_excel('file.xlsx', sheet_name=0)  # 第一个工作表

高级读取选项
# 指定列
df = pd.read_excel('file.xlsx', usecols=['A', 'C'])  # 读取A列和C列
df = pd.read_excel('file.xlsx', usecols=[0, 2])     # 读取第1和第3列
# 指定行范围
df = pd.read_excel('file.xlsx', skiprows=3)          # 跳过前3行
df = pd.read_excel('file.xlsx', nrows=100)           # 只读取前100行
# 处理标题
df = pd.read_excel('file.xlsx', header=None)         # 无标题行
df = pd.read_excel('file.xlsx', header=2)            # 使用第3行作为标题
# 指定索引列
df = pd.read_excel('file.xlsx', index_col=0)         # 使用第一列作为索引

写入 Excel 文件
基本写入
# 写入单个 DataFrame
df.to_excel('output.xlsx', index=False)
# 写入多个 DataFrame 到不同工作表
with pd.ExcelWriter('output.xlsx') as writer:
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')

高级写入选项
# 控制写入位置
df.to_excel('output.xlsx', startrow=2, startcol=3)  # 从第3行第4列开始写入
# 格式化
df.to_excel('output.xlsx',
float_format="%.2f",   # 浮点数格式
freeze_panes=(1, 1))    # 冻结首行首列
# 追加到现有文件
with pd.ExcelWriter('existing_file.xlsx', mode='a') as writer:
df.to_excel(writer, sheet_name='NewSheet')

处理多个工作表
# 读取所有工作表
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # 返回字典
# 访问特定工作表
sheet1 = all_sheets['Sheet1']
# 写入多个工作表
with pd.ExcelWriter('output.xlsx') as writer:
for sheet_name, df in dfs.items():
df.to_excel(writer, sheet_name=sheet_name)

处理大型 Excel 文件
对于大型文件，可以使用 chunksize 参数分块读取：
# 分块读取
chunk_size = 1000
chunks = pd.read_excel('large_file.xlsx', chunksize=chunk_size)

for chunk in chunks:
process(chunk)  # 处理每个块

注意事项
需要安装 openpyxl 或 xlrd 库：
pip install openpyxl xlrd
对于 .xls 文件使用 xlrd，对于 .xlsx 文件使用 openpyxl
处理大数据时，考虑使用 openpyxl 的只读模式以提高性能
写入时如果文件已存在，默认会覆盖整个文件
对于复杂格式的 Excel 文件，可能需要使用专门的 Excel 库如 openpyxl 或 xlsxwriter

# 详细解读
https://www.runoob.com/pandas/pandas-excel.html



# pd.read_excel() - 读取 Excel 文件
参数说明：
io：这是必需的参数，指定了要读取的 Excel 文件的路径或文件对象。

sheet_name=0：指定要读取的工作表名称或索引。默认为0，即第一个工作表。

header=0：指定用作列名的行。默认为0，即第一行。

names=None：用于指定列名的列表。如果提供，将覆盖文件中的列名。

index_col=None：指定用作行索引的列。可以是列的名称或数字。

usecols=None：指定要读取的列。可以是列名的列表或列索引的列表。

dtype=None：指定列的数据类型。可以是字典格式，键为列名，值为数据类型。

engine=None：指定解析引擎。默认为None，pandas 会自动选择。

converters=None：用于转换数据的函数字典。

true_values=None：指定应该被视为布尔值True的值。

false_values=None：指定应该被视为布尔值False的值。

skiprows=None：指定要跳过的行数或要跳过的行的列表。

nrows=None：指定要读取的行数。

na_values=None：指定应该被视为缺失值的值。

keep_default_na=True：指定是否要将默认的缺失值（例如NaN）解析为NA。

na_filter=True：指定是否要将数据转换为NA。

verbose=False：指定是否要输出详细的进度信息。

parse_dates=False：指定是否要解析日期。

date_parser=<no_default>：用于解析日期的函数。

date_format=None：指定日期的格式。

thousands=None：指定千位分隔符。

decimal='.'：指定小数点字符。

comment=None：指定注释字符。

skipfooter=0：指定要跳过的文件末尾的行数。

storage_options=None：用于云存储的参数字典。

dtype_backend=<no_default>：指定数据类型后端。

engine_kwargs=None：传递给引擎的额外参数字典。


# DataFrame.to_excel() - 将 DataFrame 写入 Excel 文件
参数说明：

excel_writer：这是必需的参数，指定了要写入的 Excel 文件路径或文件对象。

sheet_name='Sheet1'：指定写入的工作表名称，默认为 'Sheet1'。

na_rep=''：指定在 Excel 文件中表示缺失值（NaN）的字符串，默认为空字符串。

float_format=None：指定浮点数的格式。如果为 None，则使用 Excel 的默认格式。

columns=None：指定要写入的列。如果为 None，则写入所有列。

header=True：指定是否写入列名作为第一行。如果为 False，则不写入列名。

index=True：指定是否写入索引作为第一列。如果为 False，则不写入索引。

index_label=None：指定索引列的标签。如果为 None，则不写入索引标签。

startrow=0：指定开始写入的行号，默认从第0行开始。

startcol=0：指定开始写入的列号，默认从第0列开始。

engine=None：指定写入 Excel 文件时使用的引擎，默认为 None，pandas 会自动选择。

merge_cells=True：指定是否合并单元格。如果为 True，则合并具有相同值的单元格。

inf_rep='inf'：指定在 Excel 文件中表示无穷大值的字符串，默认为 'inf'。

freeze_panes=None：指定冻结窗格的位置。如果为 None，则不冻结窗格。

storage_options=None：用于云存储的参数字典。

engine_kwargs=None：传递给引擎的额外参数字典。

