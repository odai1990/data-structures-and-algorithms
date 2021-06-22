def multi_bracket_validation(input):    
    all_brackets=[]
    dic={'}':'{',']':'[',')':'('}
    
    for i in input:
        if i=='{' or i== '(' or i=='[':
            all_brackets.append(i)            
        else:
            if len(all_brackets) == 0:               
                return False
                
            else:
                if i==')' or i==']' or i=='}':
                    temp=all_brackets[len(all_brackets)-1]
                    if temp != dic[i]:                        
                        return False
                    all_brackets.pop(len(all_brackets)-1)

    if len(all_brackets) == 0: 
        return True
    else:
        return False







