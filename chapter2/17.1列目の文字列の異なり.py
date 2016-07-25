#set fileencoding=utf-8
"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""
with open("hightemp.txt") as f:
    print(set([line.split("\t")[0] for line in f]))
