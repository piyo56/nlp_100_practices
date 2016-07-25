#set fileecoding=utf-8
"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""
import re
answer=re.findall(r"(?:File|ファイル):([^\|]*)\|", open("aboutUK.txt").read())

for element in answer:
    print(element)

#answer=re.findall(r"(?:File|ファイル):([^\|]*)\|", open("aboutUK.txt").read())
#pattern=re.compile(r"(File|ファイル):([^\|]*)\|")
#print([re.search(pattern,line).group(2) for line in open("aboutUK.txt") if re.search(pattern, line)!=None])

"""
これもファイルだったりFileだったりする
"""
