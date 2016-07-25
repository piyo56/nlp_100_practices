#set fileencoding=utf-8
"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""
with open("hightemp.txt","r") as f:
    print(len(f.readlines()))

