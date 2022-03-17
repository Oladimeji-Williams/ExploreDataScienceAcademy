def isPalindrome(a):
    if len(a)==0 or len(a)==1:
        return True
    elif a[0]==a[-1]:
        return isPalindrome(a[1:-1])
    else:
        return False
    
    
    
if __name__ == '__main__':
    print(isPalindrome("racecar"))