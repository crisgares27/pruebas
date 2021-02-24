#GIVE A LIST WITH ITEMS
#GIVEN A LIST OF QUANTITY OF EACH ITEM
#when buy an element quit a number ub the element
#when buy all quantity of an item
#delete item from de list
#continue until the list is empty

items = ["banana", "apples", "eggs", "bread", "yogurt"]
quantity = [3, 2, 6, 1, 4]

#buy banana
banana_position = items.index("banana") # position 0
quantity[banana_position] = quantity[banana_position] - 1
print(quantity[banana_position])

#buy banana
#banana_position = items.index("banana") # position 0
quantity[banana_position] = quantity[banana_position] - 1
print(quantity[banana_position])

#buy banana
#banana_position = items.index("banana") # position 0
quantity[banana_position] = quantity[banana_position] - 1
print(quantity[banana_position])

items.remove("banana")
print(items)

###best way

buying_list = [{"item": "bananas", "quantity": 3},
               {"item": "apple", "quantity": 2}]

#buy banana

bananas = buying_list[0]["item"]
quantity = buying_list[0]["quantity"]

print("buying", bananas)
print("quantity", quantity)
buying_list[0]["quantity"] = quantity - 1
