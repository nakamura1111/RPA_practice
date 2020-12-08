#! python3
import webbrowser, sys, requests, bs4, logging
from selenium import webdriver        # この記述法が通例である理由を調べよう
                                      # webdriver を開けない時 :  https://qiita.com/apukasukabian/items/77832dd42e85ab7aa568
from selenium.webdriver.common.keys import Keys # from を使うと省略したいオブジェクト表記の指定ができる
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='selenium_try.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる 
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
# logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()


"""
webDriver オブジェクト のメソッド(elementの探索, webElement オブジェクトの作成)
|- find_element_*
|- find_elements_*
|- *_by_class_name()
|- *_by_css_selector()
|- *_by_id()
|- *_by_link_text()
|- *_by_partial_link_text()
|- *_by_name()
|- *_by_tag_name()
|- ...

|- back() forward() refresh() quit() -- 戻る、進む、再読み込み、ウィンドウ閉じる
"""
"""
webElementオブジェクト の属性・メソッド 
|- tag_name -- タグ(div とか a とか)
|- get_attribute()
|- text
|- clear() -- 入力フォームの値の消去
|- is_displayed()
|- is_enabled() -- input要素が使えるか否か
|- is_selected() -- checkboxやradiobutton要素について
|- location -- 要素のページ上の座標を表示
|- click()
|- send_keys() -- フォームへの入力
|- submit() -- 「フォームの何かの要素を指定していれば」、送信ボタンを押す
"""
"""
selenium.webdriver.common.keys.Keys (Keys) の属性
|- DOWN, UP, LEFT, RIGHT -- 矢印キー
|- ENTER, RETURN -- 特殊なキーも大文字フルネームで記述
"""

project_info = """
\n---プロジェクト概要---
・
\n---条件---
・
\n---使い方--- 
・
\n-------今後実装--------
・
-----------------------\n
"""

def main():
  browser = webdriver.Chrome('/usr/local/bin/chromedriver')                # type chromedriver コマンドで chrome driver の格納先がわかる
  # ↑ webDriver オブジェクトが取得できた
  logging.debug( 'class of webdriver : {}'.format(type(browser)) )
  browser.get("https://google.co.jp")




if __name__ == "__main__":
  main()

