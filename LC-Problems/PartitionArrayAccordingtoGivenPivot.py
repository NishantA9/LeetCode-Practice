class Solution(object):
    def pivotArray(self, nums, pivot):
        first, mid, last = [], [], []
        for num in nums: # Loop through each number and group based on comparison with pivot
            if pivot > num:
                first.append(num) # Less than pivot
            elif pivot == num:
                mid.append(num) # Equal to pivot
            else:
                last.append(num) # Greater than pivot
        return first + mid + last # Combine the three lists in order: less → equal → greater