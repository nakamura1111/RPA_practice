#! python3
import webbrowser, sys, requests, bs4, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='top_web_pages_auto_display.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる 
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()

project_info = """
\n---プロジェクト概要---
・googleの上位検索を複数タブで表示する
\n---条件---
・あるフォルダ内の指定の拡張子ファイルの指定の正規表現を検索する
----------今後実装---------
・検索履歴の保存
・
\n---使い方--- 
・python3 top_web_pages_auto_display.py [search_words] ---> 検索して表示する
-------今後実装--------
・python3 top_web_pages_auto_display.py ---> クリップボードの内容について検索&表示
-----------------------\n
"""

def main():
  if len(sys.argv) < 2:
    print(project_info)
    print('\nplease input search_word\n')
    return
  # コマンドライン引数を取得し検索ページをリクエストする
  google_search_url = 'https://www.google.co.jp/search'
  params = { 'q': ' '.join(sys.argv[1:]) }
  logging.debug( 'params : {}'.format(params) )
  res = requests.get(google_search_url, params=params)
  res.raise_for_status()
  logging.debug( 'res info : {}'.format(res.url) )
  # デバッグ用
  # save_file = open('example.html', 'wb')
  # for chunk in res.iter_content(100000):
  #   save_file.write(chunk)
  # save_file.close()
  # 結果を全て取得
  search_soup = bs4.BeautifulSoup(res.text)
  logging.debug( 'res text : {}'.format(search_soup.text[:1000]) )
  link_elems = search_soup.select(".kCrYT > a")    # .g > .rc > .yuRUbf > a
  logging.debug( 'the number of links  : {}'.format(len(link_elems)) )
  # 検索結果をブラウザで開く
  num_open = min(5, len(link_elems))
  for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))

  # 検索履歴保存


if __name__ == "__main__":
  main()

