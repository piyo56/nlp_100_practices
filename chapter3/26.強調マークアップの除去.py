#set fileencoding=utf-8
"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""
import re
text=re.search(r"{\{\基礎情報 国\n\|((.*\n)*)\}\}", open("aboutUK.txt").read()).group(1)
templates=[re.split(r" = ", line.strip("\n")) for line in re.split(r"\n\|", text)]
#正規表現で'を消す(置換)
answer={template[0]:re.sub(r"\'","",template[1]) for template in templates}

print("[field名]:[値]")
for key, value in answer.items():
    print("{0}:{1}".format(key, value))

#pattern1=re.compile(r"\{\{基礎情報 国\n\|((.*\n)*)\}\}")
#pattern2=re.compile(r"\n\|")
#pattern3=re.compile("\'")
