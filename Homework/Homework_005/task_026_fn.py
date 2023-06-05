def st(a,b,c,r):    
    if c >= b:         
        return r
    r = a * r
    return st(a,b,c+1,r)  
    