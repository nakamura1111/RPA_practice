# 正規表現：https://docs.python.org/ja/3/howto/regex.html
import re

def main():
  # Regexオブジェクトの作成 
  mobile_phone_num_regex = re.compile(r'\d{3}-\d{4}-\d{4}')
  message = '明日090-1111-1111に電話してください。090-2222-2222でもいいです。'
  mobile_phone_num = mobile_phone_num_regex.findall(message)           # cf match(), search(), findall(), finditer()
  # print(mobile_phone_num_regex.search(message))
  for num in mobile_phone_num:
    print('電話番号抽出： ' + num)
  
  pokemon_base_stat_regex = re.compile(r'(\d{1,3})-(\d{1,3})-(\d{1,3})-(\d{1,3})-(\d{1,3})-(\d{1,3})')
  pokemon_base_stat = pokemon_base_stat_regex.search('100-100-100-100-100-100')     # Match オブジェクトを返す
  h, a, b, c, d, s = pokemon_base_stat.groups()
  print(h, a, b, c, d, s)

if __name__ == "__main__":
  main()