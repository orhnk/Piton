#!/usr/bin/env python3

import sys
path = sys.argv[1]

file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != ".ptn":
    print("transpiler can just open .ptn files (piton files)");
    quit()

tr_eng = [
        ("değilse eğer", "elif"),
        ("olarak", "as"),
        ("aktar", "import"),
        ("değilse", "else"),
        ("eğer", "if"),
        ("yaz", "print"),
        ("dene", "try"),
        ("hariç", "except"),
        ("tanımla", "def"),
        ("sınıf", "class"),
        ("döndür", "return"),
        ("aralık", "range"),
        ("ilet", "yield"),
        ("dan", "from"),
        ("devam", "continue"),
        ("uzunluk", "len"),
        ("ile", "with"),
        ("değil", "not"),
        ("dır", "is"),
        ("içinde", "in"),
        ("için", "for"),
        ("iddia", "assert"),
        ("geç", "pass"),
        ("veya", "or"),
        ("Doğru", "True"),
        ("Yanlış", "False"),
        ("iken", "while"),
        ("ver", "raise"),
        ("ve", "and"),
        ("Hiç", "None"),
        ("kır", "break"),
        ("aç", "open"),
]

content = f.read()
for (tr, eng) in tr_eng:
    content = content.replace(tr , eng);
exec(content)
