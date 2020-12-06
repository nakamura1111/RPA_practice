#! python3
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='log.log')      # 初期設定 -> logging.debug() でログのターミナル表示ができる
                    # 変数「level」以上のログを表示, ログの表示形式の作成（ログの発生時間 - ログのレベル - ログの内容（メッセージ））, ログファイルの出力(ターミナルには出力されなくなる)
logging.disable(logging.CRITICAL)       # ログの無効化（以下のログを表示しなくなる）
logging.debug('プログラム開始')

def factorial(n):
  logging.debug('factorial({})開始'.format(n))
  total = 1
  for i in range(1, n+1):     # 1 から n までループ
    total *= i
    logging.debug('i = {}, total = {}'.format(i, total))
  logging.debug('factorial({})終了'.format(n))
  return total

def main():
  try:
    num = 1
    if num == 0:
      print('0徐算エラーが起こると...')
      num = 30 / 0
    elif num == 1:
      print('自作エラーが起こると...')
      raise Exception('dummy error')
  except ZeroDivisionError:
    print('exceptの処理を実行する（0徐算）')
  except Exception:           # 全部のエラーに引っかかる可能性あり 最後に回したほうがよさそう
    print('exceptの処理を実行する（自作エラー）')

  # トレースバッグ：エラー時に発生、関数の往来・エラー内容を表示
  # コールスタック：トレースバッグの並びのこと

  # assert [条件式], [Falseのときに表示する内容]
  # 「assert」 はプログラマの失敗対策
  # ユーザの失敗は例外で処理

  # assertの無効化 -> python3 コマンドで -O オプションを使用

  print(factorial(5))
  logging.debug('プログラム終了')       # プログラマ宛ての表示物
  # 重要度によって使い分ける debug() -> info() -> warning() -> error() -> critical()

if __name__ == '__main__':
  main()