dishes =['яичница', 'стейк', 'салат']

import xml.etree.ElementTree as ET
tree = ET.parse('recipes.xml')
root = tree.getroot()

def get_shop_list_by_dishes(dishes, person_count):
 for dish in dishes:
  for ingridient in cook_book[dish]:
   new_shop_list_item = dict(ingridient)
   new_shop_list_item['quantity'] *= person_count
   if new_shop_list_item[] not in dishes:
     dishes[new_shop_list_item['ingredient_name']] = new_shop_list_item
   else:
     dishes[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
 return dishes

def print_stop_list(dishes):
  for shop_list_item in dishes.values():
    print('{ingredient_name} {quantity} {si}'.format(""shop_list_item
	
def create_shop_list():
  person_count= int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека: ').split(',  ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)

create_shop_list()