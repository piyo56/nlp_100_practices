#set fileencoding=utf-8
"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""
from random import shuffle

sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
def typo(word):
    middle=list(word[1:-1])
    shuffle(middle)
    return word[0]+''.join(middle)+word[-1]
print(' '.join(typo(w) if len(w)>4 else w for w in sentence.split()))

"""
[original code]
import sys,random,itertools

sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

#文を単語に分解
words=[word.strip(".,") for word in sentence.split()]

for idx,word in enumerate(words):
    ret=""
    L=len(word)
    #5文字以上なら処理
    if 4<L:
        #最初は確定
        ret+=word[0]
        #並べ替えパターンを全てリストに
        perm=list(itertools.permutations(list(word[1:L-1]),L-2))
        #乱数生成
        rnd=random.randint(0,len(perm)-1)
        #並びのなかからランダムにピック
        ret+="".join(perm[rnd])
        #最後も確定
        ret+=word[L-1]
        
        words[idx]=ret
print (words)
"""
