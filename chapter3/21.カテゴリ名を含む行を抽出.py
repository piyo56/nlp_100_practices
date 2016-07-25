#set fileencoding=utf-8
"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
import re
answer=re.findall(r".*Category.*",open("aboutUK.txt").read())
for element in answer:
    print(element)

#print([line for line in open("aboutUK.txt") if re.search(pattern, line)!=None])
#text=[list(filter(lambda line: line.find("Category")>=0,open("aboutUK.txt","r")))]
"""
多くのpythonのfindを解説しているwebページでは、見つかった場合は1を、見つからなかった場合には-1を返すと解説していたが、違った。
python3のドキュメントを読むと、見つかった場合にはその単語の開始位置のインデックス(複数ある場合には最小のもの)が返るらしい。引っかかった悔しい。

"""
