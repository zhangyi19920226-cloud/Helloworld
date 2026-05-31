import json
import os


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age


class Course:
    def __init__(self, subject):
        self.subject = subject


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"学生 {student.name} 添加成功")

    def search_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        s = self.search_student(student_id)
        if s:
            self.students.remove(s)
            print(f"学生 {s.name} 已删除")
        else:
            raise ValueError(f"找不到学号 {student_id} 的学生")

    def save(self, filename):
        data = [{"student_id": s.student_id, "name": s.name, "age": s.age}
                for s in self.students]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("保存成功")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.students = [
            Student(d["student_id"], d["name"], d["age"]) for d in data]


def main():
    manager = GradeManager()

    while True:
        print("\n===== 学生管理系统 =====")
        print("1.添加学生")
        print("2.查找学生")
        print("3.删除学生")
        print("4.保存数据")
        print("5.加载数据")

        choice = input("请选择：")

        if choice == "1":
            sid = input("学号:")
            name = input("姓名：")
            age = int(input("年龄："))
            manager.add_student(Student(sid, name, age))
        elif choice == "2":
            sid = input("学号:")
            s = manager.search_student(sid)
            print(f"找到：{s.name}" if s else "未找到")
        elif choice == "3":
            sid = input("学号：")
            try:
                manager.delete_student(sid)
            except ValueError as e:
                print(e)
        elif choice == "4":
            manager.save("students.json")
        elif choice == "5":
            manager.load("students.json")
        elif choice == "0":
            break


main()
