def to_weird_case(string):
    Bean=""
    F=True
    for char in string:
        if F :    
            Bean += char.upper()
            F=False
        else :
            Bean += char.lower()
            F=True
        if char == ' ' :
            F=True
        
    return Bean
    
    
    
bean=to_weird_case("BEANS ARE GOOD")   
print(bean)