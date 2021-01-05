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
    key_pkmn = self.__replace_pkmn_name(key_pkmn)
    # ポケモン種族値の取得
    for pkmn in self.pkmns_name_tag:
      if (len(key_pkmn) == 1) & (pkmn.contents == key_pkmn):
        logging.debug( 'children element : {}, keyword : {}'.format(pkmn.contents, key_pkmn) )
        return self.__get_base_stat(pkmn, key_pkmn)
      elif (len(key_pkmn) == 2) & (len(pkmn.contents) == 3):
        if (key_pkmn[0] == pkmn.contents[0]) & (key_pkmn[1] == pkmn.contents[2].contents[0]):
          logging.debug( 'children element : {}, keyword : {}'.format(pkmn.contents, key_pkmn) )
          return self.__get_base_stat(pkmn, key_pkmn)
    logging.debug('Not Match... ,  search pokemon : {}'.format(key_pkmn))
    return 'Not Match'
  
  def __replace_pkmn_name(self, key_pkmn):
    if 'A' in key_pkmn:
      return [key_pkmn.replace('A', ''), '(アローラのすがた)']
    elif 'G' in key_pkmn:
      return [key_pkmn.replace('G', ''), '(ガラルのすがた)']
    elif '霊' in key_pkmn:
      return [key_pkmn.replace('霊', ''), '(れいじゅうフォルム)']
    elif 'ロトム' in key_pkmn:
      return ['ロトム', '({})'.format(key_pkmn)]
    else:
      return [key_pkmn]
  
  def __get_base_stat(self, tag_key_pkmn, key_pkmn):
    tag_parent = tag_key_pkmn.parent
    base_stat = [tag_key_pkmn.contents]
    for i in range(6):
      tag_parent = tag_parent.next_sibling
      base_stat.append(tag_parent.contents[0])
      if len(base_stat)==7:
        break
    return base_stat


# 単体動作確認用
if __name__ == "__main__":
  base_stat = BaseStat()
  ans = base_stat.search('フシギバナ')
  if ans != 'Not Match':
    print('base status of {} is {}'.format(ans[0][0], ans[1:]))
  else:
    print(ans)
 