list1 = ['hello', '2', 'world', ',!__@', '222']
list2 = ['13444', '155954', '123', '2']
text = 'To add a new remote, use the git remote add command on the terminal, in the directory your'
list3 = text.split()
def array_trim(a):
    new_list = []
    for i in range(len(a)):
        if len(a[i]) <= 3:
            new_list.append(a[i])
    a = new_list
    return a

print(array_trim(list1))
print(array_trim(list2))
print(array_trim(list3))