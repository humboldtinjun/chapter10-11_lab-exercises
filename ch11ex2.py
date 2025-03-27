#write a line of code that appends he value 6 to the end of the second list in t
list0 = [1, 2, 3]
list1 = [4, 5]
t = (list0, list1)

t[1].append(6) # it accesses the second element of the tuple and appends 6 to it
print(t)
# Output: ([1, 2, 3], [4, 5, 6])

d = {t: 'this tuple contains two lists'}
