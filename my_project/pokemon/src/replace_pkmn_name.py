from pkmn_name_replace_list import *

def replace_pkmn_name(pkmn):
  for key in pkmn_name_replace_list:
    if key==pkmn:
      return pkmn_name_replace_list[key]
  return pkmn

# メイン
if __name__ == "__main__":
  print(replace_pkmn_name('バンギラス'))