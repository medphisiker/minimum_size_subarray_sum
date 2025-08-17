from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        window_sum = nums[0]
        window_len = 1
        min_window_len = len(nums) + 1

        while right < len(nums):
            if window_sum < target:
                right += 1

                if right == len(nums):
                    break

                window_sum += nums[right]
            else:
                window_len = right - left + 1

                if window_len < min_window_len:
                    min_window_len = window_len

                if left < right:
                    window_sum -= nums[left]
                    left += 1
                else:
                    right += 1

                    if right == len(nums):
                        break

                    window_sum += nums[right]

        # Если такого подмассива нет, верните 0.
        if min_window_len == len(nums) + 1:
            min_window_len = 0

        return min_window_len
