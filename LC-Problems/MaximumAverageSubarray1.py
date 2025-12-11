class Solution:
    def findMaxAverage(self, nums, k):
        windowSum = sum(nums[:k])  # sum of first k elements
        maxSum = windowSum  # track the maximum window sum
        for i in range(k, len(nums)):  # slide window over remaining elements
            windowSum += nums[i]-nums[i-k]  # add new element, remove old one
            maxSum = max(maxSum, windowSum)  # update max if current window is larger
        return maxSum/k  # return the average of the max sum