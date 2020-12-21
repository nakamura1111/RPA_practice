#! python3
import logging, openpyxl, glob
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='log.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
# logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）

project_info = """
\n---プロジェクト概要---
・
\n---条件---
・
\n---使い方--- 
・
-----------------------\n
"""

def main():
  # # ファイル作成
  # wb = openpyxl.Workbook()
  # sheet = wb.active
  # sheet.title = 'initial_sheet'
  # wb.save('example.xlsx')

  # ファイル閲覧
  wb = openpyxl.load_workbook('example.xlsx')
  logging.debug(type(wb))
  sheet_names = wb.sheetnames
  for sheet_name in sheet_names:
    sheet = wb[sheet_name]
    logging.debug('the name of instance : {} - the class of sheet : {} - sheet title : {}'.format(sheet, type(sheet), sheet.title))
  logging.debug('active sheet : {}'.format(wb.active))

  # セル閲覧
  sheet = wb['initial_sheet']
  cell = sheet['A1']
  logging.debug('the name of instance : {} - the class of cell : {}'.format(cell, type(cell)))
  logging.debug('{}(row:{}, column:{}) have {}'.format(cell.coordinate, cell.row, cell.column, cell.value))

  # 



if __name__ == "__main__":
  main()