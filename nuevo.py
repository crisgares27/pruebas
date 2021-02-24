#PI = 3.14
#print("pi", PI)
#PI = 3
#print("change pi", PI)

#first_number = 1
#second_number = first_number + 1
#print(first_number)
#print(second_number)

#first_letter = "h"
#second_lettter = first_letter + "o"
#print(first_letter)
#print(second_lettter)


#COPIES
#FIRST_LIST = [1, 2, 3]
#second_list = FIRST_LIST[:]#cuando se dejan solo los dos puntos me copiatodo lo de la lista
#second_list.pop()
#print(FIRST_LIST)
#print(second_list)

carlos = {"name": "Carlos", "company": "Envera", "age": 20}
laura = dict()
#copy
laura["company"] = carlos["company"]
laura["age"] = carlos["age"]
laura["name"] = carlos["name"]
#change
laura["name"] = "laura"
print(carlos)
print(laura)
carlos["surname"] = "alvez"
print(carlos)
print(laura)

