def orderd_sequential_search(search_list,item):
        pos = 0
        found = False
        stop = False
        while pos < len(search_list) and not found and not stop:
            if search_list[pos] == item:
                found = True
               
            if search_list[pos] > item:
                stop = True
        else:
            pos = pos + 1
        return found
print orderd_sequential_search([11,22,3,44,5,66],0)
print orderd_sequential_search([11,22,3,44,5,66],3)
