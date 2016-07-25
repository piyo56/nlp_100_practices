#set fileencoding=utf-8
"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ.
"""
import json

article=[json.loads(line) for line in open("jawiki-country.json")]
print(type(article))
print(len(article))
for i in range(len(article)):
    print(article[i]['title'])

#print(text)
#print(json.dumps(text, sort_keys=True, ensure_ascii=False, indent=4))
#print(text["text"])
