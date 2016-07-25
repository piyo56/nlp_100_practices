#!/bin/sh
#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

if test $# -eq 1; then
	sed -e "s/\t/\ /g" $1
fi
