import json


class Book:
    def __init__(self, book_id, book_name, book_author, can_borrow=True):
        self.book_id = book_id
        self.name = book_name
        self.author = book_author
        self.can_borrow = can_borrow


class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.name = member_name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"书名{book.name}添加成功")

    def add_member(self, member):
        self.members.append(member)
        print(f"会员名{member.name}添加成功")

    def find_book(self, book_id):
        for s in self.books:
            if s.book_id == book_id:
                return s
        return None

    def find_member(self, member_id):
        for s in self.members:
            if s.member_id == member_id:
                return s
        return None

    def borrow_book(self, member_id, book_id):
        s = self.find_book(book_id)
        m = self.find_member(member_id)
        if not s:
            raise ValueError(f"找不到书号 {book_id} 的书")
        if not m:
            raise ValueError(f"找不到会员 {member_id}")
        if not s.can_borrow:
            raise ValueError(f"《{s.name}》已经被借走了")
        m.borrowed_books.append(s)
        s.can_borrow = False
        print(f"{m.name}借走了《{s.name}》")

    def return_book(self, member_id, book_id):
        s = self.find_book(book_id)
        m = self.find_member(member_id)
        if not s:
            raise ValueError(f"找不到书号 {book_id} 的书")
        if not m:
            raise ValueError(f"找不到会员 {member_id}")
        if s not in m.borrowed_books:
            raise ValueError(f"{m.name}没有借过《{s.name}》")
        m.borrowed_books.remove(s)
        s.can_borrow = True
        print(f"{m.name}归还了《{s.name}》")

    def save(self, filename):
        data = {
            "books": [
                {"book_id": s.book_id, "book_name": s.name,
                 "book_author": s.author, "can_borrow": s.can_borrow}
                for s in self.books
            ],
            "members": [
                {"member_id": s.member_id, "member_name": s.name,
                 "borrowed_book_ids": [b.book_id for b in s.borrowed_books]}
                for s in self.members
            ]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("保存成功")

    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [
                Book(d["book_id"], d["book_name"],
                     d["book_author"], d["can_borrow"])
                for d in data["books"]
            ]
            self.members = [
                Member(d["member_id"], d["member_name"])
                for d in data["members"]
            ]
            for i, m in enumerate(self.members):
                for book_id in data["members"][i]["borrowed_book_ids"]:
                    book = self.find_book(book_id)
                    if book:
                        m.borrowed_books.append(book)
            print("加载成功")
        except FileNotFoundError:
            print(f"文件 {filename} 不存在，无法加载数据")


def main():
    lib = Library()

    while True:
        print("\n===== 图书管理系统 =====")
        print("1.添加图书")
        print("2.添加会员")
        print("3.借阅图书")
        print("4.归还图书")
        print("5.保存数据")
        print("6.加载数据")
        print("0.退出系统")

        choice = input("请输入选择: ")

        if choice == "1":
            bookid = input("请输入书号：")
            bookname = input("请输入书名：")
            bookauthor = input("请输入作者：")
            lib.add_book(Book(bookid, bookname, bookauthor))
        elif choice == "2":
            memberid = input("请输入会员号：")
            membername = input("请输入会员名：")
            lib.add_member(Member(memberid, membername))
        elif choice == "3":
            memberid = input("请输入会员号：")
            bookid = input("请输入书号：")
            try:
                lib.borrow_book(memberid, bookid)
            except ValueError as e:
                print(e)
        elif choice == "4":
            memberid = input("请输入会员号：")
            bookid = input("请输入书号：")
            try:
                lib.return_book(memberid, bookid)
            except ValueError as e:
                print(e)
        elif choice == "5":
            lib.save("library.json")
        elif choice == "6":
            lib.load("library.json")
        elif choice == "0":
            break


main()
