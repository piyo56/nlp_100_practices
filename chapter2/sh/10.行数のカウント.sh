#!/bin/sh
#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．

if test $# -eq 1; then
	wc -l $1
fi
