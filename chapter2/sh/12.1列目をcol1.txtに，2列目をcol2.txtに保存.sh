#!/bin/sh
#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

if test $# -eq 1; then
	cut -f 1 $1 > col1.txt
	cut -f 2 $1 > col2.txt
fi
