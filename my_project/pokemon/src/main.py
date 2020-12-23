import openpyxl, logging, os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(pathname)s - %(message)s', filename='log/battle_record.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()
# LogRecord属性(formatの記述について)：https://docs.python.org/ja/3/library/logging.html#logrecord-attributes

from basestat_get import BaseStat
from pkmns_inc_party import PkmnsIncParty
from search_excel_files import *

project_info = """
\n---プロジェクト概要---
・
\n---条件---
・
\n---使い方--- 
・
-----------------------\n
"""

def battle_record():
  # # ファイル検索
  # excel_file_full_path = search_excel_files()
  # if excel_file_full_path == None:
  #   print('--- No file ---')
  #   return
  # ファイルを開く
  workbook = openpyxl.load_workbook( '/Users/nakamurakoyo/Desktop/pokemon_battle_record.xlsx' )
  logging.debug('\'pokemon_battle_record.xlsx\' sheet is {}'.format(workbook.get_sheet_names()))
  print('--------\nOpened File\n----------\n')

  # データ読み込みとデータ操作
  read_sheet = workbook.get_sheet_by_name('S13')
  i_btl = 0
  pkmns_from_excel = PkmnsIncParty()
  while read_sheet['C{}'.format(7*i_btl+2)].value != None:  
    for i_pkmn in range(6):
      num_low = 7*i_btl+2+i_pkmn
      pkmn_input = {'name': None, 'is_first_use': False, 'is_second_use': False}
      pkmn_input['name'] = read_sheet['C{}'.format(num_low)].value
      if read_sheet['D{}'.format(num_low)].value == 1:
        pkmn_input['is_first_use'] = True
      if read_sheet['D{}'.format(num_low)].value == 2:
        pkmn_input['is_second_use'] = True
      pkmns_from_excel.input(pkmn_input)
    i_btl += 1
  logging.debug('the kind of pokemons : {}'.format( len(pkmns_from_excel.output_all()) ) )
  # logging.debug('{}'.format( pkmns_from_excel.output_all() ) )
  print('\n--------\nInputted Data\n----------\n')

  # 種族値読み込み
  base_stat_all = BaseStat()

  # 書き込みとセーブ
  write_sheet = workbook.get_sheet_by_name('S13_statistics')
  for i, pkmn_info in enumerate( pkmns_from_excel.sort_by_num_in_party() ):
    dnm = pkmn_info['num_in_party']
    if dnm < 2:
      break
    write_sheet['A{}'.format(i+2)] = pkmn_info['name']
    frst = float(pkmn_info['first_use'])
    scnd = float(pkmn_info['second_use'])
    write_sheet['B{}'.format(i+2)] = dnm
    write_sheet['C{}'.format(i+2)] = round( (frst+scnd)/dnm*100, 1 )
    write_sheet['D{}'.format(i+2)] = round( frst/dnm*100, 1 )
    write_sheet['E{}'.format(i+2)] = round( scnd/dnm*100, 1 )
    bs = base_stat_all.search  ( pkmn_info['name'] )
    for j in range(6):
      write_sheet.cell(column=j+6, row=i+2).value = int(bs[j+1]) 

  workbook.save('/Users/nakamurakoyo/Desktop/pokemon_battle_record_copy.xlsx')
  print('--------\nSaved\n----------\n')

# メイン
if __name__ == "__main__":
  print('\n--------\nStart\n----------\n')
  battle_record()
  print('--------\nFinish\n----------\n')