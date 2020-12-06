#! python3
# プロジェクト概要
'''
・強いパスワードかどうかを確認する
-------条件--------
・強いパスワード：8文字以上、大文字・小文字・数字を一文字以上含む
-------使い方--------
・python3 strong_password.py [password]       --> [password] が強力かどうかを出力 
'''

import sys, re

def main():
  password = sys.argv[1]
  
  strong_pass_pattern_length = re.compile(r'''^[0-9a-zA-Z]{8,}''')
  strong_pass_pattern_num = re.compile(r'''
    ^([a-zA-Z]*?)
    ([0-9]+?)
    (.*)$
  ''', re.VERBOSE)
  strong_pass_pattern_small_char = re.compile(r'''
    ^([0-9a-zA-Z]*?)
    ([a-z]+?)
    (.*)$
  ''', re.VERBOSE)
  strong_pass_pattern_large_char = re.compile(r'''
    ^([0-9a-zA-Z]*?)
    ([A-Z]+?)
    (.*)$
  ''', re.VERBOSE)

  if strong_pass_pattern_length.search(password) == None:
    print('{} では文字数が足りません（8文字以上）'.format(password))
  elif strong_pass_pattern_num.search(password) == None:
    print('{} には数字が含まれていません'.format(password))
  elif strong_pass_pattern_small_char.search(password) == None:
    print('{} には小文字のアルファベットが含まれていません'.format(password))
  elif strong_pass_pattern_large_char.search(password) == None:
    print('{} には大文字のアルファベットが含まれていません'.format(password))
  else:
    print('{} は強いパスワードです'.format(password))


if __name__ == '__main__':
  main()