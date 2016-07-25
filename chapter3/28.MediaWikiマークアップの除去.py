#set fileencoding=utf-8
"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""
import re
text=re.search(r"\{\{基礎情報 国\n\|((.*\n)*)\}\}", open("aboutUK.txt").read()).group(1)
templates=[re.split(r" = ", re.sub(r"\n","",line)) for line in re.split(r"\n\|", text)]
for index,value in enumerate(templates):
    #[[記事名#節名|表示文字]]を表示文字に変換
    templates[index][1]=re.sub(r"\[\[[^\[\:]*\#[^\[]*\|([^\[]*)\]\]","\\1",value[1])
    #[[記事名|表示文字]]を表示文字に記事名に変換
    templates[index][1]=re.sub(r"\[\[[^\[\:]*\|([^\[]*)\]\]","\\1",value[1])
    #[[記事名]]を記事名に変換
    templates[index][1]=re.sub(r"\[\[([^\[\:\|]*)\]\]","\\1",value[1])
    #ファイルのマークアップを削除し、ファイル名のみに変換
    templates[index][1]=re.sub(r"\[\[ファイル:([^\|]*)\|.*\]\]"," \\1 ",value[1])
    #<ref>var</ref>をvarに変換
    templates[index][1]=re.sub(r"<ref>(.*)<\/ref>"," \\1 ",value[1])
    #<ref name="var"/>をvarに変換
    templates[index][1]=re.sub(r"<ref name=\"(.*)\" ?\/?>","\\1",value[1])
    #外部リンクのマークアップを削除し、urlのみに変換
    templates[index][1]=re.sub(r"\[([^\[\]\|]*)\]"," \\1 ",value[1])
    #箇条書き**は\t- に変換
    templates[index][1]=re.sub(r"\*\*","\t- ",value[1])
    #箇条書き*は- に変換
    templates[index][1]=re.sub(r"\*","- ",value[1])
    #最後に<br>タグを\nに変換
    templates[index][1]=re.sub(r"<br ?/>","\n",value[1])

answer={template[0]:re.sub("\'","",template[1]) for template in templates}

print("[field名]:[値]")
for key, value in answer.items():
    print("{0}:{1}".format(key, value))
