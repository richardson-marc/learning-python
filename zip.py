# this packs 2 lists into tuples
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']

for item in zip(mylist1,mylist2):
    print(item)