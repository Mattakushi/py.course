array = input("Enter num array here: ")
list = array.split(' ')
set = set()
for x in list:
    if list.count(x) > 1:
        set.add(x)
print(set)
