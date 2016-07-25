#set fileencoding=utf-8
"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
#line.split("\t")[0]がどうにも気持ち悪い
col1=[line.split("\t")[0] for line in open("hightemp.txt")]
count={word:col1.count(word) for word in col1}
for word,freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
    print(freq, word, sep="\t")
#Pythonの辞書(dict型)をvalue値でソート - プログラミング工場 / Python http://blog.livedoor.jp/yawamen/archives/51492355.html
