a,b = input().split(" ")

def problem(a,b) :
    a = int(a)
    b = int(b)
    if a > b :
        print (">")
    
    elif a < b :
        print ("<")
    
    elif a==b :
        print ("==")
    
    return

problem(a,b)
