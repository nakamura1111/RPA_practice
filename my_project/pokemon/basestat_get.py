import requests, bs4, logging, webbrowser
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(pathname)s\n   %(message)s', filename='pokemon.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
# logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# LogRecord属性(formatの記述について)：https://docs.python.org/ja/3/library/logging.html#logrecord-attributes
logging.debug('start function')

def base_stat_get():
  res = requests.get('https://yakkun.com/swsh/stats_list.htm')
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text)
  basic_stat_tag = soup.select('.table')
  print(tag.children)
  # table_file.write()
  # table_file.close()






base_stat_get()