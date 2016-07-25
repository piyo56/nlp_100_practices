#set fileendoing=utf-8
"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""
sentence="I am an NLPer"

#文字bi-gram
charGram=[sentence[i:i+2] for i in range(len(sentence)-1)]

#単語bi-gram
words=[word.strip(".,") for word in sentence.split()] #文字に分解
wordGram=["-".join(words[i:i+2]) for i in range(len(words)-1)]

print (charGram)
print (wordGram)
"""
[original code]
words=sentence.split()
wordGram=[words[i]+"-"+words[i+1] for i in range(len(words)-1)]
"""
