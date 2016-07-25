#set fileencoding=utf8
"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    #1 英小文字ならば(219 - 文字コード)の文字に置換
    #2 その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
def cipher(string):
    return ''.join(chr(219-ord(c)) if 'a'<=c<='z' else c for c in string)

#def cipher(string):
#    ans=""
#    for char in string:
#        if 97 <= ord(char) <= 123:
#            ans+=chr(219-ord(char))
#        else:
#            ans+=char
#    return ans

if __name__=="__main__":
    sentence="Hello, world!"
    ciphertext=cipher(sentence)
    print (sentence)
    print (ciphertext)
    print (cipher(ciphertext)) 
