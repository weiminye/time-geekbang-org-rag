# 读取当前目录下的data.xlsx文件
import pandas as pd

data = pd.read_excel('data.xlsx')

# 遍历数据框中的每一行数据
for index, row in data.iterrows():
    # 打印每一行的数据
    print(row['文本内容'])
