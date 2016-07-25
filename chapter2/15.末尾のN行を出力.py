#set fileencoding=utf-8
"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""
import sys
assert len(sys.argv)==2, "[usage]: python 14.先頭からN行を出力.py [N]"
with open("hightemp.txt") as f:
    print("".join(f.readlines()[-int(sys.argv[1]):]), end="")

#f=open("hightemp.txt")
#for i in range(int(sys.argv[1])):
#    f.seek(2,i)
#    print(f.readline(),end="")
#f.close()
