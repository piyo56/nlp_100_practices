#set fileencoding=utf-8
"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

sentence ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#単語に分解
words=[word.strip(".,") for word in sentence.split()]

#先頭の1文字(または2文字)と、その単語のインデックスを対応付ける辞書を作成
link={}
for i,v in enumerate(words,1):
    length=1 if i in [1,5,6,7,8,9,15,16,19] else 2
    link.update({v[:length]:i})
print(link)

#単語に分解
#words=[word.strip(".,") for word in sentence.split()]
#link={}
#for i,v in enumerate(words,1):
#    length=1 if i in [1,5,6,7,8,9,15,16,19] else 2
#    link.update({v[:length]:i})

