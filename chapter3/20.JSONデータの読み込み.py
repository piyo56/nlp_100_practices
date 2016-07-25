#set fileencoding=utf-8
"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ.
"""
import json
#jsonの読み込み(注:一行ずつ)　構造は辞書("text","title")
json_data=[json.loads(line) for line in open("jawiki-country.json")]
article={data["title"]:data["text"] for data in json_data}
print(article["イギリス"])
