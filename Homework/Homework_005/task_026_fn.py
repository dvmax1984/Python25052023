def st(a,b,count,result):    
    
    if count >= b:         
        return result
    
    
    result = a * result

    return st(a,b,count+1,result)  
    