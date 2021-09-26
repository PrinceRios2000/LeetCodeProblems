class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        [0,1,2,4,5,7]
        
        '''
        # If nums is empty, return an empty array
        if not nums:
            return []
        
        res = []
        expected_num = nums[0]
        start_num = nums[0]
        
        for num in nums:
            if num != expected_num:
                if start_num != expected_num-1:
                    res.append(str(start_num) + '->' + str(expected_num-1))
                else:
                    res.append(str(start_num))
                start_num = num
                
            expected_num = num + 1
            
        if start_num != expected_num-1:
            res.append(str(start_num) + '->' + str(expected_num-1))
        else:
            res.append(str(start_num))  
        
        return res