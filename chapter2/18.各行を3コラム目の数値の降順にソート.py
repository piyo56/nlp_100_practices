#set fileencoding=utf-8
"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""
data=[line.split("\t") for line in open("hightemp.txt")]

for line in sorted(data, key=lambda x: float(x[2]), reverse=True):
    print("\t".join(line), end="")

"""
Python でリストのソートまとめ - akiyoko blog http://akiyoko.hatenablog.jp/entry/2014/09/26/235300
Pythonで2次元配列の静的確保と動的確保 - sonickun.log http://sonickun.hatenablog.com/entry/2014/06/13/132821
"""
