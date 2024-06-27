def unique_list(l):
    x = []
    for a in l:
        if a not in x: 
            x.append(a)
    return x

print(unique_list([7, 5, 5, 5, 6, 1, 2, 2]))  
