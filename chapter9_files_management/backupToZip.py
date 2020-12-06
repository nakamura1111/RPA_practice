#! python3
# backupToZip.py

# プロジェクト概要
"""
・作業プロジェクトを時系列順に連番をつけて圧縮保存しておきたい
---条件---
・
"""

import os
import zipfile

def backup_to_zip(folder):
  '''フォルダ全体をzipファイルとしてバックアップする'''
  # 絶対パス表記
  folder = os.path.abspath(folder)

  # ファイル名を決定する（連番を振る）
  num = 1
  while True:
    zip_filename = os.path.basename(folder) + '_' + str(num) + '.zip'     # フォルダの名前（パスの末尾）に連番を振る
    if not os.path.exists(zip_filename):
      break
    num = num + 1
  
  # zipファイルの作成
  print( 'Creating {}...'.format(zip_filename) )
  backup_zip = zipfile.ZipFile(zip_filename, 'w')

  # フォルダツリーを渡り歩いて、フォルダ内の全てのファイルをリストアップ・圧縮する
  for foldername, subfolders, filenames in os.walk(folder):
    # print(foldername, subfolders, filenames)
    print('Adding files in {}...'.format(foldername))
    backup_zip.write(foldername)
    for filename in filenames:
      new_base = os.path.basename(folder) + '_'
      if filename.startswith(new_base) and filename.endswith('.zip'):
        continue
      backup_zip.write(os.path.join(foldername, filename))
  backup_zip.close()
  print('Done.')

def main():
  backup_to_zip('sample')

if __name__ == "__main__":
  main()