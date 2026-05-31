import pandas as pd
import numpy as np

df = pd.read_csv("projects/students.csv")
print("原始数据：")
print(df)
print()

print("===== 各科平均分 =====")
print(f"语文平均分: {df['语文'].mean():.1f}")
print(f"数学平均分: {df['数学'].mean():.1f}")
print(f"英语平均分: {df['英语'].mean():.1f}")
print()

print("===== 各科最高分/最低分 =====")
for subject in ['语文', '数学', '英语']:
    print(f"{subject} - 最高: {df[subject].max()} 最低: {df[subject].min()}")
print()

df['总分'] = df['语文'] + df['数学'] + df['英语']
df['个人平均'] = (df['总分'] / 3).round(1)
print("===== 学生总分排名 =====")
df_sorted = df.sort_values('总分', ascending=False)
print(df_sorted[['姓名', '语文', '数学', '英语', '总分', '个人平均']])
print()


def grade(score):
    if score >= 85:
        return '优秀'
    elif score >= 70:
        return '良好'
    elif score >= 60:
        return '及格'
    else:
        return '不及格'


df['语文等级'] = df['语文'].apply(grade)
print("===== 成绩等级 =====")
print(df[['姓名', '语文', '语文等级']])
print()

scores = df[['语文', '数学', '英语']].values
print("===== NumPy 统计 =====")
print(f"全体总平均分: {np.mean(scores):.1f}")
print(f"每科标准差: {np.std(scores, axis=0).round(1)}")
print(f"最高分学生总分: {np.max(df['总分'].values)}")
