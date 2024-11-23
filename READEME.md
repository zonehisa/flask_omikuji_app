https://edu.next-revolution.net/882100947/doc/14_flask_basic/06_flask_omikuji/01.md

Flask おみくじWebアプリを作成しよう
http://127.0.0.1:8000/omikuji にアクセスした時、

今日の運勢は ...と大吉!!もしくは、吉や凶...と表示するアプリを作成してみます。


準備
今回は flask_omikuji_app をプロジェクトとし、作業をしていきます。


pythonフォルダー直下のweb_appフォルダーの中に、flask_omikuji_appフォルダーを作成します。

下記のコマンドでも OK です。

$ mkdir -p ~/camp/python/web_app/flask_omikuji_app
Copy
flask_omikuji_appディレクトリに移動します。

$ cd ~/camp/python/web_app/flask_omikuji_app
Copy
pwdコマンドで現在の作業ディレクトリがflask_omikuji_appであるか確認します。

$ pwd
# Mac
/Users/ユーザー名/camp/python/web_app/flask_omikuji_app

# Windows
/home/ユーザー名/camp/python/web_app/flask_omikuji_app
Copy
仮想環境を作成し切り替えます。

プロジェクトフォルダーはcamp/python/web_app/flask_omikuji_app、プロジェクト名はflask_omikuji_appです。

こちらの手順に従って仮想環境の作成と、切り替えを行ってください。


完成イメージ

  camp/
  ├── ...
  └── python/
      └── web_app/
+         └── flask_omikuji_app/
+             └── .venv
Copy

リポジトリの準備をしましょう。

Gitの初期化
.gitignoreに.venvを記述
ファイルをステージング（git add）
first commit（git commit）
リモートリポジトリを作成
紐付け（git remote）
リモートリポジトリにプッシュ（git push）

プロジェクト直下に、新規ファイル（ファイル名:app.py）を作成してください。
また、Flaskをインストールしてください。

$ pip install flask
Copy

流れ
プロジェクト直下にtemplatesディレクトリを作成
templatesディレクトリに、新規ファイル（ファイル名:omikuji.html）を作成
/omikujiのルーティングを作成
omikuji.htmlで固定値の結果表示
おみくじ部分を作成
手順を解説していきます。

まずは大吉が表示されるようにしてみましょう。

/omikujiのルーティングを追加

app.py

+ from flask import Flask, render_template
+ 
+ app = Flask(__name__)
+ 
+ 
+ # おみくじアプリルーティング
+ @app.route("/omikuji")
+ def omikuji():
+     # 変数を作成
+     result = "大吉!!"
+     # テンプレートでresult変数を使用する
+     return render_template("omikuji.html", result=result)
+ 
+ 
+ if __name__ == "__main__":
+     app.run(port=8000, debug=True)
Copy

omikuji.htmlで固定値の結果表示

変数を利用できるようにするには {{ }}で変数を囲む

omikuji.html

+ <!DOCTYPE html>
+ <!-- ここは日本語対応に -->
+ <html lang="ja">
+ <head>
+     <meta charset="UTF-8">
+     <meta name="viewport" content="width=device-width, initial-scale=1.0">
+     <title>Omikuji</title>
+ </head>
+ <body>
+     <p>今日の運勢は ... {{ result }} </p>
+ </body>
+ </html>
Copy

ブラウザで実行してみましょう。

【実行結果】
http://127.0.0.1:8000/omikujiにアクセスした時に今日の運勢は ... 大吉!!と表示


大吉!!の表示
あとはresultを大吉、吉、凶に振り分けるようにできれば完成です。


おみくじ部分を作成

resultをrandom.choiceを使って大吉、吉、凶に振り分けます

app.py

+ import random
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  
  @app.route("/omikuji")
  def omikuji():
-     # 変数を作成
-     result = "大吉!!"
+     # random.choiceを使って大吉、吉、凶に振り分ける
+     result = random.choice(["大吉!!", "吉", "凶..."])
      # テンプレートでresult変数を使用する
      return render_template("omikuji.html", result=result)
  
  
  if __name__ == "__main__":
      app.run(port=8000, debug=True)
Copy

実行結果を確認してみましょう。

【実行結果】
http://127.0.0.1:8000/omikujiにアクセスした時(リロードでも可)にランダムで大吉、吉、凶が選択され表示される


おみくじ結果のランダム表示
これで、レンダーテンプレートを作って、出力結果を出せるようになりました。



if文を使っておみくじの実行結果によってコメントを変更しよう
イメージとしては、大吉が出た時はやったね！、吉の時はまあまあ、凶のときは残念をコメントを表示します。


大吉のコメント
まずは、大吉のときだけコメントが出るようomikuji.htmlにif文を記述します。
HTMLに制御構文を記述する時は、{% %}で囲む必要があります。
({{ }}は表示する場合、{% %}は表示しない場合と覚えると楽です。) また、if文の終了時にはかならずendifを記述します。

omikuji.html

  <!DOCTYPE html>
  <html lang="ja">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Omikuji</title>
  </head>
  <body>
      <p>今日の運勢は ... {{ result }}</p>
+ 
+     <!-- もしresult変数が大吉だった時はやったねの表示 -->
+     {% if result == "大吉!!" %}
+         <p>やったね！</p>
+     {% endif %}
+ 
  </body>
  </html>
Copy

実行結果を確認してみましょう。
複数回リロードして、大吉とそれ以外のときの表示の違いを確認してください。

【実行結果】
大吉のときだけコメントの出現


おみくじ大吉だけコメント

吉・凶のコメント
吉→まあまあ、凶→ざんねん！のコメントが表示されるようにomikuji.htmlに追加をしてください。

omikuji.html(記述例)

  <!DOCTYPE html>
  <html lang="ja">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Omikuji</title>
  </head>
  <body>
      <p>今日の運勢は ... {{ result }}</p>
  
      {% if  result == "大吉!!" %}
          <p>やったね！</p>
+     {% elif result == "吉" %}
+         <p>まあまあ</p>
+     {% elif result == "凶..." %}
+         <p>ざんねん！</p>
      {% endif %}
  
  </body>
  </html>
Copy
【実行結果】
大吉、吉、凶でコメントの変更


おみくじ結果別コメント
確認できたらコミットしましょう。
