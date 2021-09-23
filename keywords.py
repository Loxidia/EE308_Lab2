import re


def read_text():
    file = open(r"C:\\Download\test.txt", "r", encoding="UTF-8")
    txt = file.read()
    for ch in '!#$%&()+,-.:;<=>?@[\\]^_{|}~':
        txt = txt.replace(ch, " ")
    file.close()
    return txt


def filter():
    txt = read_text().replace("else if", "elseif")
    separator = [r'//.*', r'\/\*(?:[^\*]|\*+[^\/\*])*\*+\/', r'".*"']
    for sp in separator:
        wordlist = re.split(sp, txt)
        txt = ""
        for word in wordlist:
            txt = txt + word
    wordlist = txt.split()
    return wordlist


words = filter()
filterwords = []


def main_counter():
    keywords = {"auto", "break", "case", "char", "const",
                "continue", "default", "do", "double", "else",
                "enum", "extern", "float", "for", "goto",
                "if", "int", "long", "register", "return",
                "short", "signed", "sizeof", "static", "struct",
                "switch", "typedef", "union", "unsigned",
                "void", "volatile", "while", "elseif"
                }
    counts = {}
    cnt = 0
    for word in words:
        if len(word) == 1 or (word not in keywords):
            continue
        counts[word] = counts.get(word, 0) + 1
        filterwords.append(word)
        cnt = cnt + 1
    cnt = cnt + counts.get("elseif", 0)
    print("total num: {}".format(cnt))
    return counts


def switchcase(counts):
    num = counts.get("switch", 0)
    print("switch num: {}".format(num))
    if num == 0:
        print("case num: {}".format(num))
        return
    count = []
    flag = -1
    for word in words:
        if word == "switch":
            count.append(0)
            flag += 1
        elif word == "case":
            count[flag] += 1
        else:
            continue
    print("case num: ", end="")
    print(" ".join(str(x) for x in count))


def ifelse():
    stack = []
    if_else_num = 0
    if_elseif_else_num = 0
    for word in filterwords:
        if word == "if":
            stack.append(word)
        elif word == "elseif" and stack[-1] != "elseif":
            stack.append(word)
        elif word == "else":
            if stack[-1] == "if":
                stack.pop()
                if_else_num += 1
            elif stack[-1] == "elseif":
                stack.pop()
                stack.pop()
                if_elseif_else_num += 1
    print("if-else num: {}".format(if_else_num))
    if level == '4':
        print("if-elseif-else num: {}".format(if_elseif_else_num))


level = input()


def count():
    if '1' <= level <= '4':
        counts = main_counter()
    if '2' <= level <= '4':
        switchcase(counts)
    if '3' <= level <= '4':
        ifelse()


count()
