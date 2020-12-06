# プロジェクト概要
"""
・米国式日付を欧州式日付に変換する
---条件---
・カレントディレクトリで米国式日付をファイル名にもつすべてのファイルを探す
・見つけたら、欧州式に変える
"""

# 競プロのファイル整理に使える

import os
import re
import shutil     # https://docs.python.org/ja/3/library/shutil.html

def main():
  # 米国式日付のパターンにマッチングする正規表現を作成
  american_date_pattern = re.compile(r'''
    ^(.*?)                # 日付前のテキスト（最初に任意の文字列（0文字以上）、非貪欲マッチ）
    ((0|1)?\d)-             # 月を表す(?で二桁表記と一桁表記の両方に対応？)
    ((0|1|2|3)?\d)-         # 日を表す
    ((19|20)\d{2})          # 年を表す(1900年代, 2000年代のみ対応)
    (.*?)$                # 日付の後の全テキスト
  ''', re.VERBOSE)        # 正規表現の空欄（改行）とコメント許可
  # os.listdir() を呼び出し、カレントディレクトリの全ファイルを取り出す
  for amer_filename in os.listdir('.'):
    # 正規表現を用いて、ファイル名に日付があるか調べる
    mo = american_date_pattern.search(amer_filename)         # mo : Matching Object
    if mo == None:
      continue
    # 正規表現のグループごとに値を取り出す
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)
    # ファイル名を変更する
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    print('Renaming "{}" to "{}"...'.format(amer_filename, euro_filename))
    # shutil.move(amer_filename, euro_filename)

if __name__ == "__main__":
  main()