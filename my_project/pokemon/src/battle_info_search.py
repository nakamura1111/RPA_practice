#! python3
import webbrowser, logging
from selenium import webdriver        # この記述法が通例である理由を調べよう
                                      # webdriver を開けない時 :  https://qiita.com/apukasukabian/items/77832dd42e85ab7aa568
# seleniumのバックグラウンド起動：https://watlab-blog.com/2019/08/18/selenium-chrome-background/
# import chromedriver_binary                  # パスを通すためのコード
# from selenium.webdriver.chrome.options import Options # オプションを使うために必要

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='top_web_pages_auto_display.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる 
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()
# LogRecord属性(formatの記述について)：https://docs.python.org/ja/3/library/logging.html#logrecord-attributes

project_info = """
\n---プロジェクト概要---
・
\n---条件---
・
\n---使い方--- 
・
-----------------------\n
"""

class InfosPkmnsFromWeb():
  """"""
  browser = None
  pkmns = None
  
  def __init__(self, pkmns):
    # webドライバーをバックグラウンド表示
    # option = Options()                          # オプションを用意
    # option.add_argument('--headless')           # ヘッドレスモードの設定を付与
    # self.browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)   # Chromeを準備(optionでヘッドレスモードにしている）
                                                                               # type chromedriver コマンドで chrome driver の格納先がわかる
    self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    # 表示対象を格納
    self.pkmns = pkmns

  def display_pokemons_from_poketetsu(self):
    """"""
    for pkmn in self.pkmns:
      # 基礎情報ページへ遷移
      self.browser.get('https://yakkun.com/')
      ele = self.browser.find_element_by_class_name('search')
      ele.send_keys(pkmn)
      ele = self.browser.find_element_by_xpath("//button[@value='zukan']").click()
      # print(ele.get_attribute('value'))
      # webブラウザに表示
      webbrowser.open(self.browser.current_url)
    # browser.close()
      
  def display_damage_calc(self):
    """"""
    
    
  def display_pokemons_from_database(self):
    """"""
    # https://swsh.pokedb.tokyo/pokemon/show/[図鑑番号]-00?season=14&rule=0

# メイン
if __name__ == "__main__":
  print('\n--------\nStart\n----------\n')
  # ポケモン二体入力
  pkmn_input = []
  while len(pkmn_input)!=2:
    print('対面しているポケモンを入力（全角スペース区切り）')
    pkmn_input = input().split()
  print('入力完了： {}'.format(pkmn_input))
  # インスタンスの作成
  infos_pkmns = InfosPkmnsFromWeb(pkmn_input)
  # 二体のポケモンの情報表示（ポケ徹）
  infos_pkmns.display_pokemons_from_poketetsu()
  # 使用率情報を出力
  infos_pkmns.display_pokemons_from_database()
  # ダメージ計算サイトの出力
  infos_pkmns.display_damage_calc()
  print('--------\nFinish\n----------\n')