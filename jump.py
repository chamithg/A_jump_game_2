class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def run( array,step_count,pos):
        
            if step_count == len(array)-1:
                return True
            for i in range(array[pos]): 
                run (array,step_count = step_count +i +1, pos = pos+i+1)
                
            return False
        
        return run(nums,0,0)
        
        
        
obj = Solution()

nums = [2,3,1,1,4]

print(obj.jump(nums))