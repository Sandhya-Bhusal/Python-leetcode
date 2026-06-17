class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count=0
        result=""
        
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                count+=1
                if count>=n:
                    result=True
                else:
                    result=False
            if flowerbed[0]==1:
                if count>=n:
                    result=True
                else:
                    result=False

                
        else:
            if flowerbed[0]==0:
                if flowerbed[1]==0:
                    flowerbed[0]=1
                    count+=1

            for i in range(1,len(flowerbed)-1):

                if flowerbed[i]==0:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        count+=1
                
            if flowerbed[-1]==0:
                if flowerbed[-2]==0:
                    flowerbed[-1]=1
                    count+=1

            if count>=n:
                    result=True
            else:
                    result=False

        return result


        