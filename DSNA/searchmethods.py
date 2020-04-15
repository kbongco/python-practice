#write an algorithim to search for an employee id 

def search_id(eid,ele):
    i = 0 
    found = False

    while i < len(eid) and not found:
        if eid[i] == ele:
            found = True
            print('Found!')

        else:
            print('Not Found')

