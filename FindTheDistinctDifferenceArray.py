### FIND THE DISTINCT DIFFERENCE ARRAY 

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #this will hold the count of distinct elements from the start up to i
        prefix =[0]*n
        #this sill hold the count of distinct elements from i+1 to the end
        suffix=[0]*n

        #lets go from left to right and keep track of how many unique elements we have seen
        seenPrefix = set()
        for i in range(n):
            #add the value because we have already seen it
            seenPrefix.add(nums[i])
            prefix[i]=len(seenPrefix)

        #now we are going from right to left, but this time we are interested in the number of distinct values after i
        seenSuffix=set()
        for i in range(n-1,-1,-1):
            #coun of unique elements after it
            suffix[i]=len(seenSuffix)
            seenSuffix.add(nums[i])

        #finally, we calculate the result, for each i, we are going to substract the suffix count from the prefix count
        diff=[prefix[i]-suffix[i] for i in range(n)]
        return diff
