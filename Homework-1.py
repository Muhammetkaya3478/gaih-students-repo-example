import random

my_list=[[37,57,79],[11,13,17],[19,23,29]]


for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print ("{} ".format(my_list[i][j]),end='') # end='' ifadeleri yan yana yazar.
    print("\n")