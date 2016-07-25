#set fileecoding=utf-8
"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""
import re,json,sys
"""
(注)valueには<br>や<ref>などのhtmlタグの他、"\n"も含まれる
{{基礎情報 国
|[field]=[value]
|[field]=[value]
        ・
        ・
        ・
|[field]=[value]
}}
"""
#該当部分(基礎情報)を取り出す
text=re.search(r"\{\{基礎情報 国\n\|((?:.*\n)*)\}\}", open("aboutUK.txt").read()).group(1)
#[field]=[value]のカタマリを取り出して、[field]と[value]のgroupオブジェクトをリスト化
templates=[re.split(r" = ", line) for line in re.split(r"\n\|", text)]
#[field]:[value]の辞書作成
answer={template[0]:re.sub("\n","",template[1]) for template in templates}

print("[field名]:[値]")
for key, value in answer.items():
    print("{0}:{1}".format(key, value))

"""
#print([[re.match(pattern, line).group(1), re.match(pattern, line).group(2)] for line in open("aboutUK.txt") if re.match(pattern, line)!=None]) 
これが最悪。なぜなら\nで区切るとおかしくなるから。そもそも*でリストとして並べようとしているのはわかるが、値として続いているのに、<br>で区切り、さらに\nで区切るとかガイキチデータ構造なんじゃないかと

そもそも正規表現(.*)が行をまたげないのにも関わらず、valueが複数行にまたがっているのがネック(おかしくね!?)
"""

