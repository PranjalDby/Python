def reverse_String(string):
    if(string == ""):
        return ""
    
    return string[-1:] + reverse_String(string[:len(string)-1])

def is_palindrome(string):
    if(len(string) == 0 or len(string) == 1):
        return True
    
    if(string[:1] == string[-1:]):
        return is_palindrome(string[1:len(string)-1])
    
    return False

def dec_tobin(number,result):
    if number == 0:
        return result
    else:
        result.append(number % 2)
        return dec_tobin(number // 2,result)
s = "Pranjal is good boy"
ss = "kudos"
# print(reverse_String(s))
print(is_palindrome(ss))
# 233 // 2
print(dec_tobin(6,[]))