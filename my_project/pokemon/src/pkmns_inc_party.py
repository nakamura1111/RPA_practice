import openpyxl, os

class PkmnsIncParty():
  """ """
  __pkmns = []
  # def __init__(self):

  def input(self, pkmn_input):
    index_p = -1
    for i, dictionary in enumerate(self.__pkmns):
      if pkmn_input['name'] == dictionary['name']:
        index_p = i
        break
    if index_p == -1:
      self.__add_pkmn(pkmn_input['name'])
      index_p = len(self.__pkmns) - 1
    self.__add_num(index_p, pkmn_input)
    return

  def __add_pkmn(self, pkmn_new):
    self.__pkmns.append( {'name': pkmn_new, 'cnt_in_party': 0, 'cnt_first_use': 0, 'cnt_secont_use': 0} )
    return
  
  def __add_num(self, index_p, pkmn_input):
    self.__pkmns[index_p]['cnt_in_party'] += 1
    if pkmn_input['use_order']==1:
      self.__pkmns[index_p]['cnt_first_use'] += 1
    if pkmn_input['use_order']==2:
      self.__pkmns[index_p]['cnt_secont_use'] += 1
    return
    
  def output_all(self):
    return self.__pkmns
  
  # 連想配列のソート：https://qiita.com/yousuke_yamaguchi/items/23014a3c8d8beb8ba073
  def sort_by_num_in_party(self):
    return sorted(self.__pkmns, key=lambda x:x['cnt_in_party'], reverse=True)
    






