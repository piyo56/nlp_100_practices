#!/bin/sh
#11. $B%?%V$r%9%Z!<%9$KCV49(B
#$B%?%V(B1$BJ8;z$K$D$-%9%Z!<%9(B1$BJ8;z$KCV49$;$h!%3NG'$K$O(Bsed$B%3%^%s%I!$(Btr$B%3%^%s%I!$$b$7$/$O(Bexpand$B%3%^%s%I$rMQ$$$h!%(B

if test $# -eq 1; then
	sed -e "s/\t/\ /g" $1
fi
