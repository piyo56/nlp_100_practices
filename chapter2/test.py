#set fileencoding=utf-8
#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

if __name__=="__main__":
    col1=open("col1.txt","w")
    col2=open("col2.txt","w")
    for line in open("hightemp.txt"):
        list=line.split("\t")
        col1.write(list[0]+"\n")
        col2.write(list[1]+"\n")
    col1.close()
    col2.close()
