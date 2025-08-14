#Creating the list my_list
my_list=[]

#apending the items to the list
my_list.append(10, 20, 30, 40)

#inserting the value 15 at the second position in the list
my_list.insert(1, 15)

#extending the list with another list
my_list.extend([50, 60, 70])

#removing the last item from the list
del(my_list[-1])

#arranging the list in ascending order
my_list.sort()

#Finding the index of the value 30 in the list
print(my_list.index(30))