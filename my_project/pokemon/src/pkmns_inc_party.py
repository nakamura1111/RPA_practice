import openpyxl, os

class PkmnsIncParty():
  """ """
  pkmns = []
  # def __init__(self):

  def input(self, pkmn_input):
    index_p = -1
    for i, dictionary in enumerate(self.pkmns):
      if pkmn_input['name'] == dictionary['name']:
        index_p = i
        break
    if index_p == -1:
      self.add_pkmn(pkmn_input['name'])
      index_p = len(self.pkmns) - 1

    self.add_num(index_p, pkmn_input)
    
    return

  def add_pkmn(self, pkmn_new):
    self.pkmns.append( {'name': pkmn_new, 'num_in_party': 0, 'first_use': 0, 'second_use': 0} )
    return
  
  def add_num(self, index_p, pkmn_input):
    self.pkmns[index_p]['num_in_party'] += 1
    if pkmn_input['is_first_use']:
      self.pkmns[index_p]['first_use'] += 1
    if pkmn_input['is_second_use']:
      self.pkmns[index_p]['second_use'] += 1
    return
    
  def output_all(self):
    return self.pkmns
  
  # 連想配列のソート：https://qiita.com/yousuke_yamaguchi/items/23014a3c8d8beb8ba073
  def sort_by_num_in_party(self):
    return sorted(self.pkmns, key=lambda x:x['num_in_party'], reverse=True)
    






