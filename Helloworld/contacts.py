import json


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["email"])


class ContactManager:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    self.contacts.append(Contact.from_dict(i))
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            data = []
            for c in self.contacts:
                data.append(c.to_dict())
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_contact(self):
        name = input("Please type the name")
        try:
            number = input("Please type the number")
            email = input("Please type the email")
        except ValueError:
            print("输入错误, 请重新输入")
            return
        self.contacts.append(Contact(name, number, email))
        self.save_data()
        print("联系人添加完成")

    def show_all(self):
        if len(self.contacts) == 0:
            print("暂无联系人数据")
            return
        print("name phone email")
        print("_" * 25)
        for s in self.contacts:
            print(f"{s.name} {s.phone} {s.email}")

    def search_contacts(self):
        name = input("请输入联系人姓名")

        for s in self.contacts:
            if s.name == name:
                print(f"name:{s.name} , phont:{s.phone}, email:{s.email}")
                return

        print(f"没有找到联系人:{name}")

    def delete_contacts(self):
        name = input("请输入需要删除的姓名")

        for s in self.contacts:
            if s.name == name:
                self.contacts.remove(s)
                self.save_data()
                print(f"已删除联系人：{name}")
                return
        print(f"没找到联系人:{name}")

    def edit_contact(self):
        name = input("请输入需要修改的联系人姓名")

        for s in self.contacts:
            if s.name == name:
                new_phone = input("请输入新电话")
                new_email = input("请输入新邮箱")

                s.phone = new_phone
                s.email = new_email
                self.save_data()
                return
        print(f"没有找到联系人：{name}")


def main():
    manager = ContactManager()

    while True:
        print("\n==== Contact Management System ====")
        print("1. Show all contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Please selecct: ")

        if choice == "1":
            manager.show_all()
        elif choice == "2":
            manager.add_contact()
        elif choice == "3":
            manager.search_contacts()
        elif choice == "4":
            manager.edit_contact()
        elif choice == "5":
            manager.delete_contacts()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


main()
