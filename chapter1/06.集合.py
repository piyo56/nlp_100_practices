#set fileencoding=utf-8
"""
06. $B=89g(B
paraparaparadise"$B$H(B"paragraph"$B$K4^$^$l$kJ8;z(Bbi-gram$B$N=89g$r!$$=$l$>$l(B, X$B$H(BY$B$H$7$F5a$a!$(BX$B$H(BY$B$NOB=89g!$@Q=89g!$:9=89g$r5a$a$h!%$5$i$K!$(B'se'$B$H$$$&(Bbi-gram$B$,(BX$B$*$h$S(BY$B$K4^$^$l$k$+$I$&$+$rD4$Y$h!%(B
"""
word1="paraparaparadise"
word2="paragraph"
#$BC18l(Bbi-gram
X=set([word1[i:i+2] for i in range(len(word1)-1)])
Y=set([word2[i:i+2] for i in range(len(word2)-1)])

print ("X="+str(X))
print ("Y="+str(Y))
print ("$BOB=89g(B:"+str(X|Y))
print ("$B:9=89g(B:"+str(X-Y))
print ("$B@Q=89g(B:"+str(X&Y))
if 'se' in X:
    print("'se'$B$O(BX$B$K4^$^$l$k$h(B")
if 'se' in Y:
    print("'se'$B$O(BY$B$K4^$^$l$k$h(B")
