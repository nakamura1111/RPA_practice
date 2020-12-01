# プロジェクト概要
"""
・テキストから電話番号、メールアドレスを抽出するプログラム
---条件---
・クリップボードからテキストを取得する
・クリップボードに出力する
"""
# クリップボードに文字列のコピー（pyperclipモジュールを使用）
# 正規表現の作成
# マッチした全ての文字列の取得（見つからなかった、エラーメッセージを出力）
# クリップボードに貼り付け

import re, pyperclip

def main():
  # url用の正規表現の作成
  url_regex = re.compile(r'''(
    ((http|https)://)   # スキーム(プロトコル含む)
    ([a-zA-Z0-9\.-]+/)     # ホスト名、ドメイン
    ([a-zA-Z0-9\._/]+)   # ディレクトリ
  )''', re.VERBOSE)

  # クリップボードのテキストを検索
  text = str(pyperclip.paste())
  matches = []
  for groups in url_regex.findall(text):
    matches.append(groups[0])
    # print(groups)

  # 検索結果をクリップボードに貼り付ける
  if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました：\n' + '\n'.join(matches))
  else:
    print('このページにURLはありません')

if __name__ == "__main__":
  main()