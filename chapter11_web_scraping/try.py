#! python3

import webbrowser, pyperclip
import urllib.parse         # URLエンコーディング（パーセントエンコーディング）https://note.nkmk.me/python-urllib-parse-quote-unquote/
import requests             # response オブジェクト入門 : https://note.nkmk.me/python-requests-usage/
                            # requests モジュールについて : https://requests.readthedocs.io/en/master/
                            # html解析に正規表現は使わない http://stackoverflow.com/a/1732454/1893164/
import bs4                  # parserを明示的に指定しようという話 : https://hideharaaws.hatenablog.com/entry/2016/05/06/175056
                            # 


def main():
  # # google map
  # address = pyperclip.paste()
  # webbrowser.open( 'https://www.google.com/maps/place/' + urllib.parse.quote(address) )

  # # wikipedia
  # search_word = pyperclip.paste()
  # webbrowser.open( 'https://ja.wikipedia.org/wiki/' + urllib.parse.quote(search_word) )

  # # リクエストを送信(レスポンスを得る)
  # res = requests.get('https://github.com/oreilly-japan/automatestuff-ja')
  # res.raise_for_status()
  # save_file = open('example.html', 'wb')
  # for chunk in res.iter_content(100000):
  #   save_file.write(chunk)
  # save_file.close()

  # HTML をパースする
  example_file = open('example.html')
  example_soup = bs4.BeautifulSoup(example_file)
  # print(type(example_soup))
  #print(example_soup.select('title'))# print(example_soup.select('#author'))# print(example_soup.select('.slogan'))# print(example_soup.select('body strong'))# print(example_soup.select('p > strong'))# print(example_soup.select('a[href]'))# print(example_soup.select('input[type="button"]'))
  elems = example_soup.select('p')
  #print(len(elems))#print(type(elems[1]))#print(elems[0].getText())#print(elems[0])#print(elems[1].attrs)
  



  

if __name__ == "__main__":
  main()

