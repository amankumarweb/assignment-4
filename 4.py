pieces = 0

while pieces <= 200: 
    if pieces % 5 == 2 and pieces % 6 == 3 and pieces % 7 == 2: 
        print(pieces) 
        break 
    pieces += 1
