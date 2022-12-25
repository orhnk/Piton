#!/usr/bin/env python3

import sys
path = sys.argv[1]
print(path)

file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != ".ptn":
    print("transpiler can just open .ptn files (piton files)");
    quit()


content = f.read()
content = content.replace("değilse eğer", "elif")
content = content.replace("olarak", "as")
content = content.replace("aktar", "import")
content = content.replace("değilse", "else")
content = content.replace("eğer", "if")
content = content.replace("yaz", "print")
content = content.replace("dene", "try")
content = content.replace("hariç", "except")
content = content.replace("tanımla", "def")
content = content.replace("sınıf", "class")
content = content.replace("döndür", "return")
content = content.replace("aralık", "range")
content = content.replace("ilet", "yield")
content = content.replace("dan", "from")
content = content.replace("devam", "continue")
# content = content.replace("", "")
# content = content.replace("", "")
# content = content.replace("", "")
# content = content.replace("", "")
# content = content.replace("", "")
# content = content.replace("", "")
content = content.replace("uzunluk", "len")
content = content.replace("ile", "with")
content = content.replace("değil", "not")
content = content.replace("dır", "is")
content = content.replace("içinde", "in")
content = content.replace("için", "for")
content = content.replace("iddia", "assert")
content = content.replace("geç", "pass")
content = content.replace("veya", "or")
content = content.replace("Doğru", "True")
content = content.replace("Yanlış", "False")
content = content.replace("iken", "while")
content = content.replace("ver", "raise")
content = content.replace("ve", "and")
content = content.replace("Hiç", "None")
content = content.replace("kır", "break")
içerik = content.replace("aç", "open")
exec(içerik)
