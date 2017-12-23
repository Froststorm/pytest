def arithmetic_sequence_elements(a,r,n):
    arr = []
    num = a
    for i in range(a,n+1):
        arr.append(num)
        num = num + r
    numstr = str(arr).strip('[]')    
    return numstr

print(arithmetic_sequence_elements(1,-3,10))