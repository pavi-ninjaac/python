from copy  import copy
from copy import deepcopy

#when we have a mutable dt inside a mutable dt
four_sided = {
    "name": "A 4 Sided Die",
    "options": [1, 2, 3, 4]
}

def changeDie(die):
    die["name"] = "A 6 sided die"
    die["options"].append(5)
    die["options"].append(6)
    return die

new_die = changeDie(four_sided)
print(four_sided)
print(new_die) #it was changing the original so we need to do copy


four_sided = {
    "name": "4 Sided Die",
    "options": [1, 2, 3, 4]
}

def changeDie(die):
    die = copy(die)
    die["name"] = "A 6 sided die"
    die["options"].append(5)
    die["options"].append(6)
    return die

new_die = changeDie(four_sided)
print(four_sided)
print(new_die)    #this was still changin the inside list

#so we need to do the deeo copy


four_sided = {
    "name": "4 Sided Die",
    "options": [1, 2, 3, 4]
}

def changeDie(die):
    die = deepcopy(die)
    die["name"] = "A 6 sided die"
    die["options"].append(5)
    die["options"].append(6)
    return die

new_die = changeDie(four_sided)
print(four_sided)
print(new_die) #looks good


#slicing values

l = [1,2,3,4,5]
l3 = l
l2 = l[:]
l4 = l.copy()
print(l is l2) #flase
print(l is l3) #true 
print(l is l4) #flase