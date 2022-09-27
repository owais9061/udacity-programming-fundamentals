# here we can also use max but the logic behind max is the code
# we have written below

def biggest(a,b,c):
    if a>b :
        return a
    else:
        b
    if a > b: # agr a jo hai wo B se bara hai
        if a > c: #indented inside a>b which means it will only hapen if a>b Mtb ke a apka c se bhi bara
            return a
        else: # neglect b
             return c #till here it means c is greater than & equal to a and a is greater than b
    else:
        if b > c: # b>=a
            return b
        else: # c>= b >= a
            return c
        
print(biggest('a','b','c'));



# def biggest(a,b,c):
#     if 3 > 2:
#         if 3 > 1: #indented inside a>b which means it will only hapen if a>b
#             return 3
#         else:
#              return 1 #till here it means c is greater than & equal to a and a is greater than b
#     else:
#         if 2 > 1: # b>=a
#             return 2
#         else: # c>= b >= a
#             return 1
        
# print(biggest('a','b','c'));