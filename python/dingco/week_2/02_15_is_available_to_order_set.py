shop_menus = ["만두","떡볶이","오렌지","순대","순대"]
shop_orders = ["만두","튀김","단무지"]

# 순차 탐색
# 집합 자료형 -> 중복 허용하지 않는다
def is_available_to_order(menus,orders):
 menu_set = set(menus) # O(n)

 for order in orders: # O(M)
  if order not in menu_set:
    return False    
 return True



result = is_available_to_order(shop_menus,shop_orders)

print(result)







