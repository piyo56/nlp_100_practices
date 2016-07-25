#set fileencoding=utf-8
"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
word1="パトカー"
word2="タクシー"
ans="".join([c1+c2 for c1,c2 in zip(word1,word2)])
print (ans)
