#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
if test $# -eq 1; then
	cut -f 1 $1 | sort | uniq
fi

