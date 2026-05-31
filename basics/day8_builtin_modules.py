from datetime import datetime
import os
import random
import json

names = ["小明", "小红", "小华", "小李", "小王"]
students = []
for name in names:
    students.append({
        "name": name,
        "score": random.randint(60, 100)
    })

for s in students:
    print(f"{s['name']}: {s['score']}分")

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

with open("students.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

best = loaded[0]
for s in loaded:
    if s["score"] > best["score"]:
        best = s


now = datetime.now()
print(f"当前时间：{now.strftime('%Y年%m月%d日 %H:%M:%S')}")

folder_name = f"back_up_{now.strftime('%Y%m%d')}"
os.makedirs(folder_name, exist_ok=True)
print(f"已创建文件夹:{folder_name}")

path = os.path.join(folder_name, "students.json")
print(f"备份路径：{path}")

if os.path.exists("students.json"):
    print("studengts.json 存在")
else:
    print("students.json 不存在")

print("\n当前目录的 .py 文件：")
for f in os.listdir("."):
    if f.endswith(".py"):
        print(f" {f}")
print(f"\n最高分：{best['name']}{best['score']}分")
print("\n已保存到 students.json")
