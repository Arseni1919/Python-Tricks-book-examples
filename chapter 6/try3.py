lst = [1, 2, 3, 4, 5]

# lst[start:end:step]
new_list = lst[1:3:1]
print(new_list)

new_list = lst[1:3]
print(new_list)

new_list = lst[::2]
print(new_list)

new_list = lst[::-1]
print(new_list)

lst.reverse()
print(lst)

del lst[:]
# lst.clear()
print(lst)