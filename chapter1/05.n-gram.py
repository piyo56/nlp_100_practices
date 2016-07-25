#set fileendoing=utf-8
"""
05. n-gram
$BM?$($i$l$?%7!<%1%s%9!JJ8;zNs$d%j%9%H$J$I!K$+$i(Bn-gram$B$r:n$k4X?t$r:n@.$;$h!%$3$N4X?t$rMQ$$!$(B"I am an NLPer"$B$H$$$&J8$+$iC18l(Bbi-gram$B!$J8;z(Bbi-gram$B$rF@$h!%(B
"""
sentence="I am an NLPer"

#$BJ8;z(Bbi-gram
charGram=[sentence[i:i+2] for i in range(len(sentence)-1)]

#$BC18l(Bbi-gram
words=[word.strip(".,") for word in sentence.split()] #$BJ8;z$KJ,2r(B
wordGram=["-".join(words[i:i+2]) for i in range(len(words)-1)]

print (charGram)
print (wordGram)
"""
[original code]
words=sentence.split()
wordGram=[words[i]+"-"+words[i+1] for i in range(len(words)-1)]
"""
