################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 4
# Question 4
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
#
################################################################################


import sys

def main():
    m = ["algotihm", "programminglanguages", "systemsprogramming"]
    n = ["computergraphics", "cprogramming","oop"]
    k=4
    
    print "\n"
    #print "m:", m
    #print "n:", n
    book = find_kth_book_2(m,n,k)   
    print k, "th element:", book
    #Output: oop
    print "\n\n"
    
    k=6
    #print "m:", m
    #print "n:", n 
    book = find_kth_book_2(m,n,k)
    print k, "th element:", book
    #Output: systemsprogramming
    print "\n"
    
    
def find_kth_book_2(m, n, index):
    if not n and not m:
        return None
    elif not n:
        if len(m)>=index:
            return m[index-1]
        else:
            return None
    elif not m:
        if len(n)>=index:
            return n[index-1]
        else:
            return None
    elif len(n)+len(m) < index:
        return None
    else:    
        return find_kth_book_2_helper(m, n, index)


################################################################################
#
# Bakilacak eleman sayisi her seferinde k-1 kadar azaltilarak islem yapildi.
# Karmasikligi k'dir. 
#
################################################################################
def find_kth_book_2_helper(m, n, index):
    k = -1;
    result = []*(len(m)*len(n))
    i, j = 0, 0
    while i < len(m) and j < len(n):
        #print "result:", result, "\tk:", k
        if cmp(m[i], n[j]) <= 0:
            #print "append", m[i]
            result.append(m[i])
            k+=1
            i+=1
        else:
            #print "append", n[j]
            result.append(n[j])
            k+=1
            j+=1
            
        if k == index-1:
            return result[k]
 
    while i < len(m):
        #print "append", m[i]
        result.append(m[i])
        i+=1
        k+=1
        if k == index-1:
            return result[k]
 
    while j < len(n):
        #print "append", n[j]
        result.append(n[j])
        j+=1
        k+=1
        if k == index-1:
            return result[k]
    
    
if __name__ == "__main__":
    main()
