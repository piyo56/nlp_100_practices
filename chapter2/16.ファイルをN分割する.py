#set fileencoding=utf-8
"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import sys,math
assert len(sys.argv)==2, "[usage]: python 16.ファイルをN分割する.py [N]"

text=[line for line in open("hightemp.txt","r")]
unit=math.ceil(len(text)/int(sys.argv[1]))

for i in range((int(sys.argv[1]))):
    with open("file"+str(i+1)+".txt","w") as f:
        f.write("".join(text[i*unit:(i+1)*unit]))
