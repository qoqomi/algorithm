shop_menus = ["만두","떡볶이","오렌지","순대"]
shop_orders = ["만두","튀김","단무지"]

#  순차 탐색
def is_available_to_order(menus,orders):
 menus.sort()

 for order in orders:
  if order not in menus:
    return False    
 return True



result = is_available_to_order(shop_menus,shop_orders)

print(result)







