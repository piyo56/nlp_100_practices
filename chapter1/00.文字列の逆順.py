#set fileencoding=utf-8
"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""
string="stressed" #逆順にする文字列
print (string[::-1])
###############################################
#   rev=""            #答えを入れる変数
#   for i in reversed(range(len(string))):
#   rev+=string[i]
#   print rev
