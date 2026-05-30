# 1. 建立“密码本”：英文字母和数字的摩斯码对照表
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# 2. 编码函数：文字 -> 摩斯码


def text_to_morse(text):
    """将输入的文本转换为摩尔斯电码"""
    morse_code = []
    # 为了方便匹配，将输入文本全部转为大写
    for char in text.upper():
        if char == ' ':
            # 单词之间用 '/' 分隔
            morse_code.append('/')
        else:
            # 在字典中查找字符，找不到则用 '?' 代替
            morse_code.append(MORSE_CODE_DICT.get(char, '?'))
    # 用空格分隔每个字符的摩斯码，使其更易读
    return ' '.join(morse_code)

# 3. 解码函数：摩斯码 -> 文字


def morse_to_text(morse):
    """将摩尔斯电码转换回原始文本"""
    # 先创建一个反向的“密码本”，用于解码
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    # 用空格将摩斯码拆分成一个个独立的字符码
    words = morse.split(' ')
    decoded_chars = []
    for code in words:
        if code == '/':
            decoded_chars.append(' ')
        else:
            decoded_chars.append(reverse_dict.get(code, '?'))
    return ''.join(decoded_chars).title()


# --- 在这里输入你的浪漫告白，试试看！ ---
message = "我爱李草原"

print(f"原文本: {message}")
print(f"转换步骤: 先转换为拼音。\n")

# 提示：标准的摩斯码只支持英文字母和数字，不支持中文。
# 因此，我们需要先将中文转为拼音（这里手动操作一下，也可以在代码里用 pypinyin 库实现[reference:3]）。
pinyin_message = "wo ai li cao yuan"

print(f"拼音形式: {pinyin_message}")
encoded = text_to_morse(pinyin_message)
print(f"摩斯码: {encoded}")


while True:
    print("1. 显示所有")
    print("2. 添加")
    print("3. 查询")
    print("4. 平均分")
    print("5. 删除")
    print("0. 退出")
    choice == input("请输入选择：")
    if choice == "1":
    elif choice == "2":
    elif choice == "3":
    elif choice == "4":
    elif choice == "5":
    elif choice == "0":
        break

    students = []

zhang = {"姓名": "张三", "语文": 85, "数学": 92, "英语": 88}
students.append(zhang)
li = {"姓名": "李四", "语文": 78, "数学": 88, "英语": 90}
students.append(li)

for stu in students:
    print(stu["姓名"], stu["语文"], stu["数学"], stu["英语"])

name = input("姓名：")
chinese = int(input("语文"))
math = int(input("数学:"))
english = int(input("英语:"))
new_stu = {"姓名": name, "语文": chinese, "数学": math, "英语": english}
students.append(new_stu)

search_name = input("输入要查询的姓名:")
for stu in students:
    if stu["姓名"] == search_name:
        print(stu)

total_ch = 0
for stu in students:
    total_ch += stu["语文"]
avg_ch = total_ch / len(students)

del_name = input("输入要删除的姓名：")
for i, stu in enumerate(students):
    if stu["姓名"] == del_name:
        del students[i]
