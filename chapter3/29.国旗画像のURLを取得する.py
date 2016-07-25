#set fileencoding=utf-8
"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""
import re, json, urllib.request, urllib.parse
#aboutUK.txtから国旗画像のurlだけ取り出す
flag_url=re.search(r"\|国旗画像 = (.*)", open("aboutUK.txt").read()).group(1)

#Web APIで国旗画像のurlを取得
url="http://en.wikipedia.org/w/api.php?"
params=urllib.parse.urlencode({
        "format":"json",
        "action":"query",
        "prop":"imageinfo",
        "iiprop":"url",
        "titles":"Image:{0}".format(flag_url),
        })
response=urllib.request.urlopen(url+params)
json_text=response.read()
json_data=json.loads(json_text.decode("utf-8"))
print(json_data["query"]["pages"]["23473560"]["imageinfo"][0]["url"])

"""
b"{
    "batchcomplete":"",
    "query":{
        "normalized":[{"from":"Image:Flag of the United Kingdom.svg","to":"File:Flag of the United Kingdom.svg"}],
        "pages":{
            "23473560":{
                "pageid":23473560,
                "ns":6,
                "title":"File:Flag of the United Kingdom.svg",
                "imagerepository":"local",
                "imageinfo":[{
                    "url":"https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg",
                    "descriptionurl":"https://en.wikipedia.org/wiki/File:Flag_of_the_United_Kingdom.svg"
                }]
            }
        }
    }
}
"
"""
