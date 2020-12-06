#! python3

# プロジェクト概要
project_info = """
---プロジェクト概要---\n
・マルチクリップボード（クリップボードのテキストの保存・復元）\n
---使い方---\n
・python3 mcb.py save [keyword]     [keyword]をキーとして、クリップボードの内容を保存\n
・python3 mcb.py copy [keyword]     [keyword]に紐づけられたバリュー（クリップボードの内容）をクリップボードにコピー\n
・python3 mcb.py list               全[keyword]をクリップボードにコピー\n
・python3 mcb.py delete [keyword]   [keyword]がキーとなっている情報を削除\n
・python3 mcb.py delete_all         全情報の削除\n
"""

# コマンドライン引数を調べる
# 引数に応じた作業を行う（save, copy, list）

import shelve, pyperclip, sys

def main():
  mcb_shelf = shelve.open('mcb')
  mcb_shelf['blank'] = ''
  # sys.argvからコマンドライン引数を読み出す
  # mcb.py コマンドの誤入力
  if len(sys.argv) == 1:
    print(project_info)
  else:
    mcb_shelf_keys = str(list(mcb_shelf.keys()))
    # mcb.py コマンドの list オプション
    if sys.argv[1].lower() == 'list':
      pyperclip.copy(mcb_shelf_keys)
      print('クリップボードにキーワードを出力しました\nキーワード : {}'.format(mcb_shelf_keys))
    # mcb.py コマンドの save オプション
    elif sys.argv[1].lower() == 'save':
      mcb_shelf[sys.argv[2]] = pyperclip.paste()
      print('クリップボードの内容を {} とラベリングして保存しました'.format(sys.argv[2]))
      print( '{} : {}'.format(sys.argv[2], mcb_shelf[sys.argv[2]]) )
    # mcb.py コマンドの copy オプション
    elif sys.argv[1].lower() == 'copy':
      try:
        pyperclip.copy(mcb_shelf[sys.argv[2]])
        print('{} に紐づけられた内容をクリップボードに出力しました'.format(sys.argv[2]))
        print(sys.argv[2], mcb_shelf[sys.argv[2]])
      except KeyError:
        print('{} に紐づけられた内容はありません'.format(sys.argv[2]))
        print('キーワード : {}'.format(mcb_shelf_keys))
    elif sys.argv[1].lower() == 'delete':
      try:
        mcb_shelf.pop(sys.argv[2])
        print('{} の内容を削除しました'.format(sys.argv[2]))
      except KeyError:
        print('{} に紐づけられた内容はありません'.format(sys.argv[2]))
        print('キーワード : {}'.format(mcb_shelf_keys))
    elif sys.argv[1].lower() == 'delete_all':
      is_delete_all = ''
      while (is_delete_all != 'yes') & (is_delete_all != 'no'):
        print('全削除しますか？(input「yes」or「no」)')
        is_delete_all = input()
        if is_delete_all == 'yes':
          mcb_shelf.clear()
          mcb_shelf['blank'] = ''
          print('全情報を削除しました')
        elif is_delete_all == 'no':
          print('削除しませんでした')
        else: 
          print('yes か no を入力してください')
    # mcb.py コマンドの誤入力
    else:
      print(project_info)

  mcb_shelf.close()

if __name__ == "__main__":
  main()
