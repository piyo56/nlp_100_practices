#set fileencoding=utf-8
"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ.
確認にはheadコマンドを用いよ．
"""
import sys
assert len(sys.argv)==2, "[usage]: python 14.先頭からN行を出力.py [N]"
with open("hightemp.txt") as f:
    print("".join(f.readlines()[:int(sys.argv[1])]), end="")

#text=[line for line in open("hightemp.txt","r")]
#print("".join(text[:int(sys.argv[1])]),end="")
