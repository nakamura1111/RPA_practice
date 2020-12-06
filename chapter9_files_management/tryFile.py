# プロジェクト概要
"""
・問題集の作成
---条件---
・都道府県に関する4択問題（47問）
・生徒数35人に合わせ、4択の順番・問題の順番をランダムにする。
・問題集・解答集ともにテキストファイルで書き出す。
"""

import os
import shutil     # https://docs.python.org/ja/3/library/shutil.html
import zipfile

main_dir = os.path.split(os.path.abspath(__file__))[0]
# quiz_dir = os.path.join(main_dir, 'quiz')
# answer_dir = os.path.join(main_dir, 'answer')

def main():
  # shutil.copy( os.path.join(main_dir, "renameDates.py"), os.path.join(main_dir, "renameDatas.py") )
  # shutil.move()
  # os.chdir()
  # os.unlink( os.path.join(main_dir, "renameDates.py") )   # ファイル削除
  # os.rmdir()          # 空ディレクトリの削除
  # shutil.rmtree()     # 中身と共にディレクトリ削除
  # send2trash.send2trash()   # ファイルフォルダをゴミ箱へ移動(別途モジュールのインストールが必要(pipなど))
  # デバッグとして、printでファイルパスを確認してから使用すべし

  # os.walk() ： 
  # for foldername, subfolders, filenames in os.walk(main_dir):
  #   print('カレントディレクトリ ' + foldername)
  #   for subfolder in subfolders:
  #     print('サブフォルダ ' + os.path.join(foldername, subfolder))
  #   for filename in filenames:
  #     print('ファイル ' + os.path.join(foldername, filename))
  #   print(' ')

  # zipファイル読み取り
  example_zip = zipfile.ZipFile('sample_1.zip')        # open() に相当
  file_folder_list = example_zip.namelist()
  # print(file_folder_list)
  for file_folder in file_folder_list:
    # print('file or folder path : ' + file_folder )
    spam_info = example_zip.getinfo( file_folder )
    print(spam_info.filename)
    print('file size (uncompress) : {}'.format(spam_info.file_size) )
    print('file size (compress) : {}'.format(spam_info.compress_size) )
  example_zip.close()

  # ZipFileオブジェクトに関するメソッド
  # example_zip.extractall()        # zipファイル展開, 引数で展開先を指定できる
  # example_zip.extract()           # zipファイル内の特定のファイルを展開

  # zipファイルの作成・編集
  # new_zip = zipfile.ZipFile('new.zip', 'w')             # 第二引数の指定で書き込みモードや追加モードにする
  # new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
  # new_zip.close()








  # # 問題集・解答集のフォルダ作成
  # if not os.path.exists(quiz_dir):
  #   os.makedirs(quiz_dir)
  # if not os.path.exists(answer_dir):
  #   os.makedirs(answer_dir)
  # # 問題集・解答集の作成
  # for file_num in range(35):
  #   # 問題集・解答集のファイル作成
  #   quiz_file = open( os.path.join( quiz_dir, 'capitalquiz{}.txt'.format(file_num+1) ), 'w' )
  #   answer_key_file = open( os.path.join( answer_dir, 'capitalquiz_answers{}.txt'.format(file_num+1) ), 'w')
  #   # 問題集のヘッダー作成
  #   quiz_file.write('名前：\n\n日付：\n\n')
  #   quiz_file.write( (' '*20) + '都道府県県庁所在地クイズ(問題番号{})'.format(file_num+1) )
  #   quiz_file.write('\n\n')
  #   # 都道府県の順番をシャッフルする
  #   prefectures = list(capitals.keys())
  #   random.shuffle(prefectures)
  #   # 問題を作成する
  #   for question_num in range(len(prefectures)):
  #     # 正答の県庁所在地を格納
  #     correct_answer = capitals[prefectures[question_num]]
  #     # 誤答を3つ格納
  #     wrong_answers = list(capitals.values())
  #     del wrong_answers[wrong_answers.index(correct_answer)]
  #     wrong_answers = random.sample(wrong_answers, 3)
  #     # 四択をまとめ、シャッフル
  #     answer_options = wrong_answers + [correct_answer]
  #     random.shuffle(answer_options)

  #     # 問題集：問題と選択肢の書き出し
  #     quiz_file.write('{}. {}の県庁所在地は？\n'.format(question_num+1, prefectures[question_num]))
  #     for i in range(4):
  #       quiz_file.write(' {}. {}\n'.format('ABCD'[i], answer_options[i]))
  #     quiz_file.write('\n')
  #     # 解答集：正解の書き出し
  #     answer_key_file.write(' {}. {}\n'.format(question_num+1, 'ABCD'[answer_options.index(correct_answer)]))
  #     quiz_file.write('\n')
  #   # ファイルを閉じる
  #   quiz_file.close()
  #   answer_key_file.close()

if __name__ == "__main__":
  main()