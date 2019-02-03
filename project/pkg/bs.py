"""
Module is bs implentation 
Author 
Date 
Modified by 
"""

def binary_search(l,key):
    """
    binary search fun takes list and key as input return True of key present else return false
    """
    if l:        
        mid = len(l) // 2    
        if key == l[mid]:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid],key)    
        else:
            return binary_search(l[mid+1:],key)

    else:
        return False

def main():    
    l = [10,20,30,40,50,60,70,80]
    l.sort()
    key = 100
    print(binary_search(l,key))
    
s = "Python sample string"
if __name__ == '__main__':
    
    main()
    