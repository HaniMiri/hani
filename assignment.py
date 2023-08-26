
# def calc_area (length = float(input("Enter a length :")),width = float(input("Enter a width :"))) :
#     q=length * width
#     return q
#
# print(calc_area())

# def even_odd(x = int(input("Enter a num :"))):
#     if x%2== 0:
#         print(f"{x} is even ")
#     else:
#         print(f"{x} is odd ")
#
# even_odd()

#def check_number(x=int(input("Enter a num :"))):
#  if x>=1500 and x<=2700:
#      if x%5==0 and x%7==0:
#          print("the number is valid number")
#      else:
#          print ("the number is not valid")
#  else:
#      print("the number is not valid")
#check_number()


def discount_code(total_amount):
    if total_amount >= 1000:
        return "DISCOUNT20"
    elif 500 <= total_amount <= 999:
        return "DISCOUNT10"
    else:
        return "NO_DISCOUNT"


# def neg_num(x=int(input("Enter a num :"))):
#     if x<0:
#         print(x)
#     else:
#         print(x*-1)
#
# neg_num()


def discounted (price=int(input("Enter a price :")),is_member=(int(input("Enter 0 if not member and 1 if is member :")))):
    if is_member:
        discount=price*(10/100)
        return discount
    elif is_member== False:
        discount = 0
        return discount
print("the discount ",discounted())