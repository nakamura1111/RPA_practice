import openpyxl, logging, os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(pathname)s - %(message)s', filename='log/battle_record.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
# 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()
# LogRecord属性(formatの記述について)：https://docs.python.org/ja/3/library/logging.html#logrecord-attributes

from pkmns_inc_party import PkmnsIncParty
from search_excel_files import *

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

  # ファイル操作
  read_sheet = workbook.get_sheet_by_name('S13')
  i_btl = 0
  pkmns_from_excel = PkmnsIncParty()
  while read_sheet['C{}'.format(7*i_btl+2)].value != None:  
    for i_pkmn in range(6):
      num_law = 7*i_btl+2+i_pkmn
      pkmn_input = {'name': None, 'is_first_use': False, 'is_second_use': False}
      pkmn_input['name'] = read_sheet['C{}'.format(num_law)].value
      if read_sheet['D{}'.format(num_law)].value == 1:
        pkmn_input['is_first_use'] = True
      if read_sheet['D{}'.format(num_law)].value == 2:
        pkmn_input['is_second_use'] = True
      pkmns_from_excel.input(pkmn_input)
    i_btl += 1
  logging.debug('the kind of pokemons : {}'.format( len(pkmns_from_excel.output_all()) ) )
  # logging.debug('{}'.format( pkmns_from_excel.output_all() ) )
  print('\n--------\nInputted Data\n----------\n')

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
  workbook.save('/Users/nakamurakoyo/Desktop/pokemon_battle_record_copy.xlsx')
  print('--------\nSaved\n----------\n')