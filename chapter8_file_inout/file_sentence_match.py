#! python3
import sys, shelve, logging, re, os, pprint
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='file_sentence_match.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる 
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
# logging.disable(logging.DEBUG)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()

project_info = """
---プロジェクト概要---\n
・正規表現検索\n
---条件---\n
・あるフォルダ内の指定の拡張子ファイルの指定の正規表現を検索する\n
---使い方--- 
---------現在作成中-------------
・python3 file_sentence_match.py save                                                            正規表現をシェルフ保存
・python3 file_sentence_match.py search [search_folder] [regex_keyword]  正規表現を使って検索
・python3 file_sentence_match.py list                                                            正規表現を表示(キーのみ)
・python3 file_sentence_match.py del                                                             正規表現を削除
・python3 file_sentence_match.py del_all                                                         正規表現を全削除
-----------------------\n
"""

def create_regex_sentence(input):
  result = "r'''\n"
  for tmp in input:
    result = result + tmp + '\n'
  result = result + "'''"
  logging.debug(result)
  return result

def main():
  regex_shelve = shelve.open('regex')
  logging.debug(sys.argv)
  if len(sys.argv) < 2:
    print(project_info)
    print("what's mode?")
  # save モード
  elif sys.argv[1] == 'save':
    print('--------\n正規表現入力\n 開始は「start」、終了は「stop」と入力\n 複数行表記可能、コメントあり(「re.VERBOSE」オプションつき)\n-------------\n\n')
    new_regex_input = []
    new_regex_input.append(input())
    if new_regex_input[0] == 'start':
      i = 0
      while new_regex_input[i] != 'stop':
        new_regex_input.append(input())
        i += 1
      print('入力完了')
      new_regex_input.pop(0)
      new_regex_input.pop(-1)
      regex_sentence = create_regex_sentence(new_regex_input)
      new_regex = re.compile(regex_sentence, re.VERBOSE)
      print('この正規表現の名前を入力してください')
      new_regex_name = input()
      regex_shelve[new_regex_name] = new_regex_input
      print('保存しました')
      keys = regex_shelve.keys()
      values = regex_shelve.values()
      logging.debug('{key : value}')
      for key, value in zip(keys, values):
        logging.debug('"{}" : "{}"'.format(key, value))
    else:
      print('やり直し')
  # search モード
  elif sys.argv[1] == 'search':
    if len(sys.argv) == 4:
      os.chdir(sys.argv[2])
      search_dir = os.getcwd()
      logging.debug('current dir : {}'.format(search_dir))
      regex_sentence = create_regex_sentence(regex_shelve[sys.argv[3]])
      search_target_regex = re.compile(regex_sentence, re.VERBOSE)
      logging.debug(search_target_regex.search('aastdaa'))
      logging.debug(search_target_regex)
      extension_regex = re.compile('\.cpp$')
      for foldername, subfolders, filenames in os.walk(search_dir):
        logging.debug('searching  {}  folder ...'.format(foldername))
        for filename in filenames:
          if extension_regex.search(filename) != None:
            file_abspath = os.path.join(foldername, filename)
            logging.info('open filename : {}'.format(file_abspath))
            search_file = open(file_abspath, 'r')
            contents = search_file.readlines()
            for i, content in enumerate(contents):
              mo = search_target_regex.search(content)
              if mo != None:
                print('{} 行目 : {}'.format(i+1, content))
            search_file.close()
    else:
      print(project_info)
      print('search mode : input error')
    


  elif sys.argv[1] == 'list':
    pass
  elif sys.argv[1] == 'del':
    pass
  elif sys.argv[1] == 'del_all':
    is_delete_all = ''
    while (is_delete_all != 'yes') & (is_delete_all != 'no'):
      print('正規表現を全削除しますか？(input「yes」or「no」)')
      is_delete_all = input()
      if is_delete_all == 'yes':
        regex_shelve.clear()
        print('削除しました')
      elif is_delete_all == 'no':
        print('削除しませんでした')
      else: 
        print('yes か no を入力してください')
  else: 
    print(project_info)
    print("what's mode?")
  
  regex_shelve.close()

if __name__ == '__main__':
  main()


