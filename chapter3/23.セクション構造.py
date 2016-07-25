#set fileecoding=utf-8
"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""
import re
sections=re.findall(r"(=.*=)\n", open("aboutUK.txt").read())
answer={re.sub(r"=* ?| ?=*","",section):int(section.count("=")/2-1) for section in sections}

print("[section]:[level]")
for key, value in answer.items():
    print("{0}:{1}".format(key, value))


#extract=[re.match(pattern,line.strip("\n")).group(1) for line in open("aboutUK.txt") if re.match(pattern, line)!=None]
#print({section.replace("=",""):int(section.count("=")/2-1) for section in extract})

"""
なんで=と単語の間に空白入ってたり入ってなかったりすんだろう
全角文字が入っていると{0:24s}:{1:2d}でうまく揃えられない
"""
