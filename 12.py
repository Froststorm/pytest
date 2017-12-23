#from datetime import datetime
import timeit

def timing():
    n= 55555555555555
    m = 9999999999999999999999

    

    if n and m in range(1,999999999999999999999999999999999):
        return True
    
    else:
        return False
    
        


print(timeit.timeit(timing))
