#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
if test $# -eq 2; then
	split -l $1 $2
fi
