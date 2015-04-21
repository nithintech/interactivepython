def sequential_search(lis,item):
    i = 0
    match = False
    while i < len(lis) and not match:
        if lis[i] == item:
            match = True
        else:
            i = i + 1
    return match
print sequential_search([11,22,3,44,5,66],3)
print sequential_search([11,22,3,44,5,66],77)
