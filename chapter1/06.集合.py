#set fileencoding=utf-8
"""
06. 集合
paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
word1="paraparaparadise"
word2="paragraph"
#単語bi-gram
X=set([word1[i:i+2] for i in range(len(word1)-1)])
Y=set([word2[i:i+2] for i in range(len(word2)-1)])

print ("X="+str(X))
print ("Y="+str(Y))
print ("和集合:"+str(X|Y))
print ("差集合:"+str(X-Y))
print ("積集合:"+str(X&Y))
if 'se' in X:
    print("'se'はXに含まれるよ")
if 'se' in Y:
    print("'se'はYに含まれるよ")
