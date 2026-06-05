import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [22, 25, 23, 24],
    'score': [88, 92, 79, 95]
}
df = pd.DataFrame(data)
print(df)
print(df.head(2))      # 前2行
print(df.tail(2))      # 后2行
print(df.shape)        # 几行几列
print(df.dtypes)       # 每列的数据类型
print(df.describe())   # 统计摘要
print(df['name'])           # 取一列
print(df[['name', 'score']])  # 取多列
print(df.iloc[0])           # 取第一行
print(df.loc[df['score'] > 90])  # 条件筛选
print(df.loc[0]) # 取第一行，loc使用标签索引，iloc使用位置索引
