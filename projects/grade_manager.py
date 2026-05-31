import csv


def load_data():
    students = []

    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                "姓名": row["姓名"],
                "语文": int(row["语文"]),
                "数学": int(row["数学"]),
                "英语": int(row["英语"])
            })

    return students


def show_all(students):
    if len(students) == 0:
        print("暂无学生数据")
        return

    print("姓名 语文 数学 英语")
    print("_" * 25)
    for s in students:
        print(f"{s['姓名']}  {s['语文']}  {s['数学']}  {s['英语']}")


def add_student(students):
    name = input("请输入姓名：")

    try:
        chinese = int(input("请输入语文成绩: "))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
    except ValueError:
        print("成绩必须是整数！")
        return

    students.append({"姓名": name, "语文": chinese, "数学": math, "英语": english})
    save_data(students)
    print(f"已添加学生：{name}")


def save_data(students):
    with open("students.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["姓名", "语文", "数学", "英语"])
        writer.writeheader()
        writer.writerows(students)


def search_student(students):
    name = input("请输入学生姓名:")

    for s in students:
        if s["姓名"] == name:
            print(f"姓名：{s['姓名']}  {s['语文']}  {s['数学']}  {s['英语']}")
            return

    print(f"没有找到学生:{name}")


def calc_average(students):
    total_chinese = 0
    for s in students:
        total_chinese += s["语文"]

    avg_chinese = total_chinese / len(students)
    total_math = 0
    for m in students:
        total_math += m["数学"]

    avg_math = total_math / len(students)
    total_english = 0
    for e in students:
        total_english += e["英语"]
    avg_english = total_english / len(students)
    print(f"语文平均分：{avg_chinese:.1f}")
    print(f"数学平均分：{avg_math:.1f}")
    print(f"英语平均分：{avg_english:.1f}")


def delete_student(students):
    name = input("请输入要删除人的姓名:")

    for s in students:
        if s['姓名'] == name:
            students.remove(s)
            save_data(students)
            print(f"已删除学生:{name}")
            return

    print(f"没有找到学生: {name}")


students = load_data()
while True:
    print("\n==== Student performance management system ====")
    print("1.Show all student scores")
    print("2.Add new student")
    print("3.search student")
    print("4.Calculate the average score for each course")
    print("5.delete student")
    print("0.exit")

    choice = input("Please select:")

    if choice == "1":
        show_all(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        calc_average(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "0":
        print("see ya!")
        break
    else:
        print("Invalid options,please enter again.")
