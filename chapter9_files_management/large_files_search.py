#! python3

import logging, sys, os
logging.basicConfig(level=logging.DEBUG , format=' %(asctime)s - %(levelname)s - %(message)s', filename='large_files_search.log')  # 初期設定 -> logging.debug() でログのターミナル表示ができる 
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
# logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()

project_info = """
\n---プロジェクト概要---
・容量の大きなファイルを見つける
\n---条件---
・コードに記載のフォルダより探索を行う。
・100MBより大きいファイルを表示する。
\n---使い方--- 
・python3 large_files_search.py ---> 全ファイルを検索して、大きいファイルを表示
-----------------------\n
"""

def main():
  search_folders = ['Desktop', 'Documents', 'Downloads', 'Movies', 'Music', 'Pictures', 'Public']
  for search_folder in search_folders:
    # 各フォルダへ移動
    user_name = os.environ.get('USER')
    logging.debug('user_name : {}'.format(user_name))
    os.chdir( os.path.join('/Users', user_name, search_folder) )
    logging.debug('current dir : {}'.format( os.getcwd() ))
    large_files = []
    # 探索を行う
    for foldername, subfolders, files in os.walk(os.getcwd()):
      logging.info('searching {} ...'.format(foldername))
      # ファイルを見つけたら、ファイルの大きさを調べる
      for filename in files:
        file_full_path = os.path.join(foldername, filename)
        file_size = os.path.getsize(file_full_path)
        # ファイル容量が大きかったら、リストに格納
        if file_size > 100_000_000:
          large_files.append({'file_path': file_full_path, 'file_size': file_size})
    # 容量の大きいファイルを表示
    logging.info('the number of large files : {}'.format( len(large_files) ))
    for large_file in large_files:
      print('file : {}, filesize: {}'.format( large_file['file_path'], large_file['file_size'] ))

if __name__ == "__main__":
  main()