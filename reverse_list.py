l = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(l):  
    l.reverse()
    for i in l:
        if type(i) == list:
            i.reverse()
    print(l)

reverse(l)
