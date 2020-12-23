import requests, bs4, logging, webbrowser
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(pathname)s\n   %(message)s', filename='log/basestat_get.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
# logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# LogRecord属性(formatの記述について)：https://docs.python.org/ja/3/library/logging.html#logrecord-attributes
logging.debug('start function')

class BaseStat():
  """ """
  res = None
  soup = None
  pkmns_name_tag = None

  def __init__(self):
    # WEBページの取得
    self.res = requests.get('https://yakkun.com/swsh/stats_list.htm')
    self.res.raise_for_status()
    self.soup = bs4.BeautifulSoup(self.res.content)
    # タグの取得
    # base_stat_table = soup.select(".table")
    self.pkmns_name_tag = self.soup.select("a[class='black']")
    logging.debug( 'num pokemon : {}'.format( len(self.pkmns_name_tag) ) )
  
  def search(self, key_pkmn):
    # ポケモン名の前処理
    
    # ポケモン種族値の取得
    for pkmn in self.pkmns_name_tag:
      if pkmn.contents[0] == key_pkmn:
        logging.debug( 'children element : {}, keyword : {}'.format(pkmn.contents, key_pkmn) )
        parent_tag = pkmn.parent
        base_stat = [pkmn.contents]
        for i in range(6):
          parent_tag = parent_tag.next_sibling
          base_stat.append(parent_tag.contents[0])
          if len(base_stat)==7:
            break
        return base_stat
    return 'Not Match'

# base_stat = BaseStat()
# ans = base_stat.search('フシギバナ')
# if ans != 'Not Match':
#   print('base status of {} is {}'.format(ans[0][0], ans[1:]))
 