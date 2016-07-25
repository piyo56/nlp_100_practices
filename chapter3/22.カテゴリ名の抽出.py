#set fileencoding=utf-8
"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
import re
answer=re.findall(\[\[Category:(.*)\]\] ,open("aboutUK.txt").read())
for element in answer:
    print(element)

#pattern=re.compile(r"\[\[Category\:([^\|]*)(.*)\]\]")
#print([re.search(pattern, line).group(1) for line in open("aboutUK.txt") if re.search(pattern, line)!=None])

"""
\をいれないとダメな文字を忘れてハマるのが辛い
"""
