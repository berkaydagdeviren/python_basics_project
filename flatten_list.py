l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(l):  
    flatten_l = []
    for sublist in l:
        if type(sublist) == list:
            for item in sublist:
                if type(item) == list:
                    flatten_l.append(' '.join([str(i).strip('[]') for i in item]))
                else:
                    flatten_l.append(item)
        else:
            flatten_l.append(sublist)
    print(flatten_l)       
flatten(l)
