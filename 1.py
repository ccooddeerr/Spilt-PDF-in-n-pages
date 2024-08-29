import pandas as pd
import numpy as np

# 读取 Excel 文件
df = pd.read_excel('result.xlsx')

# 获取所有的序号
numbers = df['序号'].unique()

# 创建一个字典，用于存储每个序号对应的班号
number_class_dict = {}

# 为每个序号随机分配一个 1 - 19 的班号
for number in numbers:
    random_class_number = np.random.randint(1, 20)
    number_class_dict[number] = random_class_number

# 根据字典中的班号分配，更新数据帧中的班号
df['班号'] = df['序号'].map(number_class_dict)

# 保存结果到新的 Excel 文件
df.to_excel('shuffled_result.xlsx', index=False)
