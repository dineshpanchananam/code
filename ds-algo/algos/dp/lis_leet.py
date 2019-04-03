class Solution(object):
  def findLengthOfLCIS(self, nums):
    dp = [1] * len(nums)
    for i in xrange(1, len(nums)):
      if nums[i] > nums[i-1]:
        dp[i] = dp[i-1] + 1
    return max(dp)