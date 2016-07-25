#set fileencoding=utf-8
"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""
import re
text=re.search(r"\{\{基礎情報 国\n\|((.*\n)*)\}\}", open("aboutUK.txt").read()).group(1)
templates=[re.split(r" = ", line.strip("\n")) for line in re.split(r"\n\|", text)]
#内部リンクをテキストに変換
for index,value in enumerate(templates):
	#[[記事名#節名|表示文字]]を表示文字に変換
	templates[index][1]=re.sub(r"\[\[[^\[\:]*\#[^\[]*\|([^\[]*)\]\]","\\1",value[1])
	#[[記事名|表示文字]]を表示文字に記事名に変換
	templates[index][1]=re.sub(r"\[\[[^\[\:]*\|([^\[]*)\]\]","\\1",value[1])
	#[[記事名]]を記事名に変換
	templates[index][1]=re.sub(r"\[\[([^\[\:\|]*)\]\]","\\1",value[1])
answer={template[0]:re.sub("\n|\'","",template[1]) for template in templates}

print("[field名]:[値]")
for key, value in answer.items():
	print("{0}:{1}".format(key, value))
"""
[[記事名]]
[[記事名|表示文字]]
[[記事名#節名|表示文字]]
"""
