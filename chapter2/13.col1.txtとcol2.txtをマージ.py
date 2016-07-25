#set fileencoding=utf-8
"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""
with open("col1.txt") as f1, open("col2.txt") as f2, open("output.txt","w") as f3:
	f3.write("".join([c1.strip("\n")+"\t"+c2 for c1,c2 in zip(f1,f2)]))
