#########################################################################
# Orderd - Mutable - Duplicated allowed - Indexing - Slicing - Iterable #
#########################################################################
mylist=[1,2,3]
x = list("Hello")
x = list((1,2,3,4))
x = list(range(1,11))
x = list({10,20,30})
#-----------------------------
x = x * 2 #--> هيكررها مرتين
x + [15] 
#-----------------------------
mylist.append(5)
mylist.insert(3,4)
mylist.extend([6,7,8])
mylist.extend(x)
#-----------------------------
mylist.remove(8)
mylist.pop()  #--> اخر عنصر
mylist.pop(3)
#mylist.clear()
#-----------------------------
mylist.index(5)
mylist.count(7)
mylist.sort()
mylist.sort(reverse=True)
mylist.reverse()
len(mylist)
3 in mylist
#-----------------------------
mylist[5] 
mylist[-1]
mylist[1:4]
mylist[:6]
mylist[1:5:2]
mylist[::2]
#-----------------------------
nestedlist_or_matrix =[
    [1,2,3],
    [4,5,6]
]
nestedlist_or_matrix[0][1] #--> 2
nestedlist_or_matrix[0]    #--> [1,2,3]
#------------------------------