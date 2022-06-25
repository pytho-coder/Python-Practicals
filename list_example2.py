"""
add elements in list 

there are 3 techniques we can add elements in existing list 

1) append() 
2) extend() 
3) insert() 


1) append() :add element in existing list 

syntax : 

list_var.append(element)

"""
shopping_list = []
print(shopping_list)

product = input("Enter product : ")
shopping_list.append(product)

print(shopping_list)
