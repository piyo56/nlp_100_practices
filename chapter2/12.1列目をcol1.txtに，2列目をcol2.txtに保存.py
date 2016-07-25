#set fileencoding=utf-8
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

"""
with open("hightemp.txt") as f1, open("col1.txt","w") as f2, open("col1.txt","w") as f3:
    cols=list(zip(*[row.split("\t") for row in f1]))
    f2.write("\n".join(cols[0]))
    f3.write("\n".join(cols[1]))
