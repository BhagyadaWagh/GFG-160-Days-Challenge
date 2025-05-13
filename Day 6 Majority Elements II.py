class Solution:
    def findMajority(self, arr):
        n = len(arr)
        e1, e2 = -1 , -1
        c1, c2 = 0 , 0
        
        for e in arr:
            if e1 == e:
                c1 += 1
                
            elif e2 == e:
                c2 += 1
                
            elif c1 == 0:
                e1 = e
                c1 += 1
                
            elif c2 == 0:
                e2 = e
                c2 += 1
                
            else:
                c1 -= 1
                c2 -= 1
                
        result = []
        c1 , c2 = 0 , 0
        for e in arr:
            if e1 == e:
                c1 += 1
                
            if e2 == e:
                c2 += 1
                
        if c1 > n/3:
            result.append(e1)
            
        if c2 > n/3:
            result.append(e2)
            
        if len(arr) == 2 and result[0] > result[1]:
            result[0] , result[1] = result[1] , result[0]
        
        return sorted(result)
