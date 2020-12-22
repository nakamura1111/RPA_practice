import openpyxl, os

def search_excel_files():
  # ユーザフォルダへ移動
  user_name = os.environ.get('USER')
  os.chdir( os.path.join('/Users', user_name) )
  file_full_path = None
  for foldername, subfolders, files in os.walk(os.getcwd()):
    # ファイルの名前を調べる
    for filename in files:
      if filename == 'pokemon_battle_record.xlsx':
        file_full_path = os.path.join(foldername, filename)
        break
    if file_full_path != None:
      break
  return file_full_path